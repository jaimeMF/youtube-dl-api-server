#!/bin/sh

root=$(pwd)
export root
GAE_DIR=./gae
BUILD_DIR=${GAE_DIR}/build
LIB_DIR=${GAE_DIR}/lib
GAE_REQ=${GAE_DIR}/gae_requirements.txt
CACHE_DIR=${GAE_DIR}/tmp/cache

mkdir -p "${LIB_DIR}"
mkdir -p "${BUILD_DIR}"
mkdir -p "${CACHE_DIR}"

echo "Downloading python packages"
cp requirements.txt "${GAE_REQ}"

pip install -r "${GAE_REQ}" --download-cache "${CACHE_DIR}" --no-install --build "${BUILD_DIR}" -U

echo "Copying python packages to ${LIB_DIR}"
cp -R "${BUILD_DIR}/youtube-dl/youtube_dl" "${LIB_DIR}"
cp -R "${BUILD_DIR}/flask/flask" "${LIB_DIR}"
cp -R "${BUILD_DIR}/Werkzeug/werkzeug" "${LIB_DIR}"
cp -R "${BUILD_DIR}/itsdangerous/itsdangerous.py" "${LIB_DIR}"

(
    cd "${LIB_DIR}/youtube_dl"
    echo 'Patching youtube_dl'
    "${root}/devscripts/gae-patch-youtube-dl.sh"
)

rm -rf "${BUILD_DIR}"

