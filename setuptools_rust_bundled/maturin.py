from . import _wrapper
from typing import Optional, Mapping, Any

print("!! init maturin module")

try:
    import maturin
except ImportError:
    maturin = None


def build_wheel(wheel_directory, config_settings=None, metadata_directory=None) -> str:
    print("!! build_wheel called")
    assert maturin is not None
    return _wrapper(lambda: maturin.build_wheel(wheel_directory, config_settings, metadata_directory))

def build_sdist(sdist_directory, config_settings=None) -> str:
    print("!! build_sdist called")
    assert maturin is not None
    return _wrapper(lambda: maturin.build_sdist(sdist_directory, config_settings))

def get_requires_for_build_wheel(config_settings=None) -> list[str]:
    print("!! get_requires_for_build_wheel called")
    assert maturin is not None
    return _wrapper(lambda: maturin.get_requires_for_build_wheel(config_settings))

def prepare_metadata_for_build_wheel(metadata_directory, config_settings=None) -> str:
    print("!! prepare_metadata_for_build_wheel called")
    assert maturin is not None
    return _wrapper(lambda: maturin.prepare_metadata_for_build_wheel(metadata_directory, config_settings))

def get_requires_for_build_sdist(config_settings=None) -> list[str]:
    print("!! get_requires_for_build_sdist called")
    assert maturin is not None
    return _wrapper(lambda: maturin.get_requires_for_build_sdist(config_settings))

def build_editable(
    wheel_directory: str,
    config_settings: Optional[Mapping[str, Any]] = None,
    metadata_directory: Optional[str] = None,
) -> str:
    print("!! build_editable called")
    assert maturin is not None
    return _wrapper(lambda: maturin.build_editable(
        wheel_directory,
        config_settings,
        metadata_directory
    ))

prepare_metadata_for_build_editable = prepare_metadata_for_build_wheel
