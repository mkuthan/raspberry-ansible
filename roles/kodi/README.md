# Kodi build

References: https://github.com/xbmc/xbmc/blob/master/docs/README.Linux.md

## Build dependencies

Install build dependencies:

```shell
apt install cmake clang clang-format clang-tidy default-jre swig ccache \
libasound-dev libavahi-client-dev libbluetooth-dev libbluray-dev libcec-dev libiso9660-dev liblcms2-dev \
python3-dev libxslt1-dev libudev-dev libsmbclient-dev libplist-dev libmicrohttpd-dev  liblirc-dev \
libnfs-dev libass-dev libcurl4-openssl-dev libdav1d-dev libsndio-dev libcdio++-dev libtag1-dev \
libflatbuffers-dev libfmt-dev libfstrcmp-dev liblzo2-dev libssl-dev libspdlog-dev libsqlite3-dev \
libtinyxml-dev libegl1-mesa-dev libgbm-dev libdrm-dev libinput-dev libxkbcommon-dev libgif-dev \
libjpeg-dev libcap-dev libavcodec-dev libunistring-dev
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
    -DENABLE_PULSEAUDIO=OFF
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
