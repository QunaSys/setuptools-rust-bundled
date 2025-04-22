

```
pip install setuptools wheel requests tomli
python setup.py sdist
python setup.py bdist_wheel
```

# Toolchain

| Tool     | Version |
|----------|----------|
| rustc    | 1.86.0   |
| cargo    | 0.87.0   |
| rust-std    | 1.86.0   |

# Arch

| Python platform tag | Rust target |
|------|------|
| manylinux_2_17_i686    | i686-unknown-linux-gnu |
| manylinux_2_17_x86_64  | x86_64-unknown-linux-gnu |
| manylinux_2_17_aarch64 | aarch64-unknown-linux-gnu |
| manylinux_2_17_armv7l  |  |
| manylinux_2_17_ppc64   | powerpc64-unknown-linux-gnu |
| manylinux_2_17_ppc64le | powerpc64le-unknown-linux-gnu |
| manylinux_2_17_s390x   | s390x-unknown-linux-gnu |
| musllinux_1_1_i686    |  |
| musllinux_1_2_x86_64  | x86_64-unknown-linux-musl |
| musllinux_1_2_aarch64 | aarch64-unknown-linux-musl |
| musllinux_1_1_armv7l  |  |
| musllinux_1_1_ppc64   |  |
| musllinux_1_1_ppc64le | powerpc64le-unknown-linux-musl |
| musllinux_1_1_s390x   |  |
| macosx_11_0_aarch64 | aarch64-apple-darwin |
| macosx_10_12_x86_64 | x86_64-apple-darwin |
| macosx_10_12_i686 | i686-apple-darwin |
| freebsd_12_0_x86_64 | x86_64-unknown-freebsd |
| freebsd_12_0_i686 | i686-unknown-freebsd |
| freebsd_12_0_aarch64 | aarch64-unknown-freebsd |
| freebsd_12_0_armv7l | armv7-unknown-freebsd |
| netbsd_9_0_i686 | i686-unknown-netbsd |
| netbsd_9_0_x86_64 | x86_64-unknown-netbsd |
| netbsd_9_0_aarch64 | aarch64-unknown-netbsd |
| netbsd_9_0_ppc | powerpc-unknown-netbsd |
