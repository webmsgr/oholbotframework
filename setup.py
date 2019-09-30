from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("ohol.pyx",languge_level=3)
)
