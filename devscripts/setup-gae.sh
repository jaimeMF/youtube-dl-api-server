#!/bin/sh

root=$(pwd)

# Download the required libraries to lib/
BUILD_DIR=./build/gae-setup
LIB_DIR=./lib
echo "Downloading python packages"
pip install -r requirements.txt --download-cache tmp/cache --no-install --build "${BUILD_DIR}"

echo "Copying python packages to ${LIB_DIR}"
mkdir -p "${LIB_DIR}"
cp -R "${BUILD_DIR}/Paste/paste" "${LIB_DIR}"
cp -R "${BUILD_DIR}/youtube-dl/youtube_dl" "${LIB_DIR}"

(
    cd "${LIB_DIR}/youtube_dl"
    echo 'Patching youtube_dl'
    "${root}/devscripts/gae-patch-youtube-dl.sh"
)

rm -rf "${BUILD_DIR}"

