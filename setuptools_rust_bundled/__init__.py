import subprocess
import platform
import tempfile
from importlib.resources import files, as_file
import sysconfig
from pathlib import Path
import os
from typing import Iterable, List, Dict, Callable, Any, Optional


class LibraryPath:
    def __init__(self, paths: Iterable[str | os.PathLike]) -> None:
        self.paths: List[str] = [str(Path(p).expanduser().resolve()) for p in paths]
        self.system: str = platform.system()
        self._handles: List[object] = []
        self._old_env: Dict[str, Optional[str]] = {}

    def __enter__(self):
        if self.system == "Windows":
            if hasattr(os, "add_dll_directory"):
                for p in self.paths:
                    self._handles.append(os.add_dll_directory(p))
            else:
                self._extend_env("PATH")
        elif self.system == "Darwin":
            self._extend_env("DYLD_LIBRARY_PATH")
        else:
            self._extend_env("LD_LIBRARY_PATH")
        return self

    def __exit__(self, exc_type, exc, tb):
        for h in self._handles:
            try:
                h.close()
            except Exception:
                pass
        for key, val in self._old_env.items():
            if val is None:
                os.environ.pop(key, None)
            else:
                os.environ[key] = val

    def _extend_env(self, key: str):
        env = os.environ.get(key)
        self._old_env[key] = env
        if env is None:
            joined = os.pathsep.join(self.paths)
        else:
            joined = os.pathsep.join(self.paths + [env])
        os.environ[key] = joined


TEMPDIR = Path(tempfile.mkdtemp())


def _check_cargo(path: Path) -> bool:
    if (path / 'bin' / 'cargo').is_file():
        exe_path = path / 'bin' / 'cargo'
    elif (path / 'bin' / 'cargo.exe').is_file():
        exe_path = path / 'bin' / 'cargo.exe'
    else:
        return False
    try:
        subprocess.run([exe_path, "--version"], capture_output=True, check=True)
    except subprocess.CalledProcessError:
        return False
    return True


def _wrapper(f: Callable[[], Any]) -> Any:
    package_name = __name__.split(".")[0]
    data_dir = Path(sysconfig.get_path('data')) / package_name / "data"
    if platform.system() == "Windows":
        print(f"data files: {list(data_dir.glob('*'))}")
    for toolchain in data_dir.iterdir():
        with as_file(toolchain) as path:
            toolchain_name = toolchain.name
            if not _check_cargo(path):
                continue
            if platform.system() == "Darwin" and platform.machine().upper() in ["ARM64", "AARCH64"]:
                if toolchain_name.find("aarch64") == -1:
                    # x86_64 binary on arm64 macos
                    continue

            # os.environ["CARGO"] = str(path)
            if "CARGO_HOME" not in os.environ:
                os.environ["CARGO_HOME"] = str(TEMPDIR / "cargo")
            old_path = os.environ["PATH"]
            path_list = [str(path / 'bin'), str(TEMPDIR / "cargo" / "bin")]
            os.environ["PATH"] = f"{os.pathsep.join(path_list)}{os.pathsep + old_path if old_path is not None else ''}"
            rustlib_path = toolchain / "lib" / "rustlib" / toolchain_name / "lib"
            os.environ["RUSTFLAGS"] = f"-L {str(rustlib_path)}"
            with LibraryPath([str(toolchain / "lib")]):
                result = f()
            if old_path is None:
                os.environ.pop("PATH")
            else:
                os.environ["PATH"] = old_path
        return result
    raise RuntimeError("Cannot find Rust toolchain for this environment")
