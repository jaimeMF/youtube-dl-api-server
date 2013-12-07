#!/bin/bash

set -e

if [ -z "$1" ]; then echo "ERROR: specify version like this: $0 0.9.10"; exit 1; fi
version=$1
gae_version=$(python -c "print('$version'.replace('.', '-'))")
echo "New version is $version (for GAE: $gae_version)"

read -p "Is it good, can I continue? (y/n) " -n 1
if [[ ! $REPLY =~ ^[Yy]$ ]]; then exit 1; fi
echo

echo "__version__ = '$version'" > youtube_dl_server/version.py
sed -i '' "s/^version: .*/version: $gae_version/" app.yaml
sed -i '' "s/version = \".*\"/version = \"$version\"/" setup.py

git add youtube_dl_server/version.py app.yaml setup.py
git commit -m "Release $version"
git tag $version

echo "Uploading to PyPI"
python setup.py sdist upload --sign

echo "Done."
