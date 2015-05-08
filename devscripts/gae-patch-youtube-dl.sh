#!/bin/bash

for f in **/*.py *.py; do
    python "${ROOT}/devscripts/gae-clean-imports.py" "$f"
done
