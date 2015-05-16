#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys, os

# -- General configuration -----------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    'sphinxcontrib.httpdomain',
]

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'youtube-dl-api-server'
copyright = u'2013, Jaime Marquínez Ferrándiz'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = 'alpha'
# The full version, including alpha/beta/rc tags.
release = 'alpha'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']
