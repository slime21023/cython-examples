from setuptools import Extension, setup
from Cython.Build import cythonize

ext_modules = [
    Extension(
        "shape",
        sources=["src/rect.pyx"],
        language="c++"
    )
]

setup(
    name="shape",
    ext_modules=cythonize(ext_modules)
)