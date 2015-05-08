#!/bin/sh
# Convert the Travis python version to a tox environment
TRAVIS_ENV=$1

case $TRAVIS_ENV in
    pypy*) echo "$TRAVIS_ENV";;
    *) echo py"$TRAVIS_ENV" | sed 's/\.//g';;
esac
