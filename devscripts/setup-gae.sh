#!/bin/sh

ROOT=$(pwd)
export ROOT
GAE_DIR=./gae
VENV=${GAE_DIR}/VENV
LIB_DIR=${GAE_DIR}/lib
GAE_REQ=${GAE_DIR}/gae_requirements.txt

mkdir -p "${LIB_DIR}"

if [ ! -d "${VENV}" ]; then
    echo "Creating virtualenv"
    virtualenv "${VENV}"
fi
. "${VENV}/bin/activate"

echo "Downloading python packages"
cp requirements.txt "${GAE_REQ}"

pip install -r "${GAE_REQ}" -U

echo "Copying python packages to ${LIB_DIR}"
SITE_PACKAGES=$(echo "${VENV}"/lib/*/site-packages)
cp -R "${SITE_PACKAGES}/youtube_dl" "${LIB_DIR}"
cp -R "${SITE_PACKAGES}/flask" "${LIB_DIR}"
cp -R "${SITE_PACKAGES}/werkzeug" "${LIB_DIR}"
cp -R "${SITE_PACKAGES}/itsdangerous.py" "${LIB_DIR}"

(
    cd "${LIB_DIR}/youtube_dl"
    echo 'Patching youtube_dl'
    "${ROOT}/devscripts/gae-patch-youtube-dl.sh"
)
