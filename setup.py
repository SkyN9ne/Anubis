#!/usr/bin/env python3
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
ext_modules = [
    Extension("ancrypt",  ["ancrypt.py"]),
]

setup(
    name = 'Ancrypt',
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules
)
