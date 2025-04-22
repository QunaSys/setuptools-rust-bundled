from . import _wrapper

try:
    import maturin
except ImportError:
    maturin = None


def build_wheel(wheel_directory, config_settings=None, metadata_directory=None):
    assert maturin is not None
    return _wrapper(lambda: maturin.build_wheel(wheel_directory, config_settings, metadata_directory))

def build_sdist(sdist_directory, config_settings=None):
    assert maturin is not None
    return _wrapper(lambda: maturin.build_sdist(sdist_directory, config_settings))

def get_requires_for_build_wheel(config_settings=None):
    assert maturin is not None
    return _wrapper(lambda: maturin.get_requires_for_build_wheel(config_settings))

def prepare_metadata_for_build_wheel(metadata_directory, config_settings=None):
    assert maturin is not None
    return _wrapper(lambda: maturin.prepare_metadata_for_build_wheel(metadata_directory, config_settings))

def get_requires_for_build_sdist(config_settings=None):
    assert maturin is not None
    return _wrapper(lambda: maturin.get_requires_for_build_sdist(config_settings))
