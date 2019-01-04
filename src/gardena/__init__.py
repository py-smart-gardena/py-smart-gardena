#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Gardena gateway library
"""

__version__ = "0.0.1"

from ._version import get_versions

__version__ = get_versions()["version"]
del get_versions
