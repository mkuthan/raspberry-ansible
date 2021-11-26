# Kodi build

Kodi in the distribution is usually outdated, it's better to compile and install fresh version from sources.
The compilation with all binary addons takes ~ 4 hours.

This setup supports hardware acceleration for H.264 and H.265/HEVC (8bit/10bit).

References: https://github.com/xbmc/xbmc/blob/master/docs/README.Linux.md

## Build dependencies

Install build dependencies:

```shell
apt-get build-dep kodi
```

## Kodi bin

Get the source code:

```shell
git clone -b Matrix https://github.com/xbmc/xbmc kodi
```

Create build directory:

```shell
mkdir kodi-build; cd kodi-build
```

Configure build:

```shell
cmake ../kodi -DCMAKE_INSTALL_PREFIX=/usr/local \
    -DCORE_PLATFORM_NAME=gbm \
    -DAPP_RENDER_SYSTEM=gles \
    -DENABLE_VAAPI=OFF \
    -DENABLE_VDPAU=OFF \
    -DENABLE_OPENGL=OFF \
    -DENABLE_PULSEAUDIO=OFF \
    -DENABLE_INTERNAL_FMT=ON \
    -DENABLE_INTERNAL_SPDLOG=ON
```

Build:

```shell
cmake --build . -- VERBOSE=1 -j$(getconf _NPROCESSORS_ONLN)
```

Install:

```shell
sudo make install
```

## In-tree binary add-ons

Build binary extensions:

```shell
cd kodi
```

```shell
sudo make -j$(getconf _NPROCESSORS_ONLN) -C tools/depends/target/binary-addons PREFIX=/usr/local
```

## Out-of-tree binary add-ons

```shell
git clone -b Matrix  https://github.com/xbmc/inputstream.adaptive.git
```

```shell
cmake -DCMAKE_INSTALL_PREFIX=/usr/local
make make -j$(getconf _NPROCESSORS_ONLN)
sudo make -j$(getconf _NPROCESSORS_ONLN) install
```
