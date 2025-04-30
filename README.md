

```
pip install setuptools wheel requests tomli
python setup.py sdist
python setup.py bdist_wheel -p <platform>
```

# Toolchain

| Tool     | Version |
|----------|----------|
| rustc    | 1.86.0   |
| cargo    | 0.87.0   |
| rust-std    | 1.86.0   |

# Arch

| Python platform tag | Rust target | sdist install tested | maturin supported | setuptools supported |
|------|------|-----|-----|-----|
| manylinux_2_17_i686    | i686-unknown-linux-gnu | | | YES |
| manylinux_2_17_x86_64  | x86_64-unknown-linux-gnu | YES | YES | YES |
| manylinux_2_17_aarch64 | aarch64-unknown-linux-gnu | YES | YES | YES |
| manylinux_2_17_riscv64 | aarch64-unknown-linux-gnu | | | YES |
| manylinux_2_17_armv7l  | armv7-unknown-linux-gnueabihf | | | YES |
| manylinux_2_17_ppc64le | powerpc64le-unknown-linux-gnu | | | YES |
| manylinux_2_17_s390x   | s390x-unknown-linux-gnu | | | YES |
| macosx_11_0_arm64 | aarch64-apple-darwin | YES | YES | YES |
| macosx_10_12_x86_64 | x86_64-apple-darwin | YES | YES | YES |
| freebsd_14_2_release_amd64 | x86_64-unknown-freebsd | | | YES |
| netbsd_10_1_amd64 | x86_64-unknown-netbsd | | | YES |
