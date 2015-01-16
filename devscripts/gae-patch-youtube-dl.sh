#!/bin/bash

for f in **/*.py *.py; do
    python "${root}/devscripts/gae-clean-imports.py" "$f"
done
