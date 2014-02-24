#!/bin/bash

# This modules are not availabe in GAE, we don't use any of the functions
# that required them
forbidden_cmodules="fcntl ctypes netrc ctypes"
for module in ${forbidden_cmodules}; do
    for f in **/*.py *.py; do
        sed -i '' "s/import ${module}/()# Removed ${module} import/g" "$f"
    done
done
