[![Python application](https://github.com/TTitscher/dynamic_cpp_module_py_load/actions/workflows/python-app.yml/badge.svg)](https://github.com/TTitscher/dynamic_cpp_module_py_load/actions/workflows/python-app.yml)


# dynamic_cpp_module_py_load

The purpose of this code is to play around with dynamic loading of c++ code at runtime that can be used to dynamically wrap fortran code.

The main idea is to define a c++ class that loads a shared library (given at runtime) and wraps
a pre-defined set of functions.

This class is then accessible in python via pybind11.

# how to:

[Follow the CI instructions](.github/workflows/python-app.yml)
