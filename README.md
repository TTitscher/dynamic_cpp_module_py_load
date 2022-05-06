# dynamic_cpp_module_py_load

Creates a python-wrapped c++ base class where the implementation can be changed at run time.

Just an adaptation of https://stackoverflow.com/questions/60799939/dynamically-linking-a-shared-library-from-a-pybind11-wrapped-code


# how to:

Make sure to have pybind installed

~~~sh
pip3 install pybind11
~~~

~~~sh
mkdir build && cd build
cmake -DPYTHON_EXECUTABLE=/usr/bin/python3 ..
make

python3 ../create_and_load_module.py
~~~

