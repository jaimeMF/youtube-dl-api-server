#!/bin/bash

set -e

version=`python -m youtube_dl_server --version`
echo "New version is $version"

read -p "Is it good, can I continue? (y/n) " -n 1
if [[ ! $REPLY =~ ^[Yy]$ ]]; then exit 1; fi
echo

# TODO: create a GIT tag

echo "Uploading to PyPI"
python setup.py sdist upload --sign

echo "Done."
