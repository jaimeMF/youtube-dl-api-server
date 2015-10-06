#!/bin/sh

ROOT=$(pwd)
export ROOT
GAE_DIR=./gae
VENV=${GAE_DIR}/VENV
LIB_DIR=${GAE_DIR}/lib
mkdir -p "${LIB_DIR}"
mkdir -p "${ROOT}/unzip"
wget "https://github.com/rg3/youtube-dl/archive/master.zip"
unzip "${ROOT}/master.zip" "youtube-dl-master/youtube_dl/*" -d "${ROOT}/unzip"
mv "${ROOT}/unzip/youtube-dl-master\youtube_dl" "${LIB_DIR}"

(
    cd "${LIB_DIR}/youtube_dl"
    echo 'Patching youtube_dl'
    "${ROOT}/devscripts/gae-patch-youtube-dl.sh"
)
rm "${ROOT}/master.zip"
rm -rf "${ROOT}/unzip/"