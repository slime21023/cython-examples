from setuptools import Extension, setup
from Cython.Build import cythonize

ext_modules = [
    Extension(
        "cqueue",
        sources=["src/queue.pyx","lib/queue.c"],
        include_dirs=["./lib"]
    )
]

setup(
    name="cqueue",
    ext_modules=cythonize(ext_modules)
)