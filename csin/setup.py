from setuptools import Extension, setup
from Cython.Build import cythonize

ext_modules = [
    Extension(
        "csin",
        sources=["src/sin.pyx"],
        # libraries=["m"]  # Unix-like specific
    )
]

setup(
    name="csin",
    ext_modules=cythonize(ext_modules)
)