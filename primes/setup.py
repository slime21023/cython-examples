from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize(['src/primes.pyx'],  annotate=True) # enables generation of the html annotation file
)