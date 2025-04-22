import subprocess
from importlib.resources import files, as_file
from pathlib import Path
from typing import Callable, Any
import os


def _check_cargo(path: Path) -> bool:
    if (path / 'bin' / 'cargo').is_file():
        exe_path = path / 'bin' / 'cargo'
    elif (path / 'bin' / 'cargo.exe').is_file():
        exe_path = path / 'bin' / 'cargo.exe'
    else:
        return False
    try:
        subprocess.run(f"{exe_path} --version", capture_output=True, check=True)
    except subprocess.CalledProcessError:
        return False
    return True


def _wrapper(f: Callable[[], Any]) -> Any:
    package_name = __name__.split(".")[0]
    data_dir = files(package_name)
    for toolchain in data_dir.iterdir():
        with as_file(toolchain) as path:
            if not _check_cargo(path):
                continue
            os.environ["CARGO"] = str(path)
            old_path = os.environ["PATH"]
            os.environ["PATH"] = f"{str(path / 'bin')}:{old_path}"
            result = f()
            os.environ["PATH"] = old_path
        return result
    raise RuntimeError("Cannot find Rust toolchain for this environment")
