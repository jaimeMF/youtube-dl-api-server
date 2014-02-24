#!/bin/sh

root=$(pwd)
GAE_DIR=./gae
BUILD_DIR=${GAE_DIR}/build
LIB_DIR=${GAE_DIR}/lib
GAE_REQ=${GAE_DIR}/gae_requirements.txt
CACHE_DIR=${GAE_DIR}/tmp/cache

mkdir -p "${LIB_DIR}"
mkdir -p "${BUILD_DIR}"
mkdir -p "${CACHE_DIR}"

echo "Downloading python packages"
python <<EOF > "${GAE_REQ}"
import sys
with open('requirements.txt', 'rt') as f:
    for line in f:
        if line.startswith('youtube_dl'):
            print(line)
EOF

pip install -r "${GAE_REQ}" --download-cache "${CACHE_DIR}" --no-install --build "${BUILD_DIR}" -U

echo "Copying python packages to ${LIB_DIR}"
cp -R "${BUILD_DIR}/youtube-dl/youtube_dl" "${LIB_DIR}"

(
    cd "${LIB_DIR}/youtube_dl"
    echo 'Patching youtube_dl'
    "${root}/devscripts/gae-patch-youtube-dl.sh"
)

rm -rf "${BUILD_DIR}"

