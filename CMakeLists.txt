cmake_minimum_required(VERSION 3.5 FATAL_ERROR)
PROJECT(foobar)

# compile the "plugin"
SET(CMAKE_SHARED_LIBRARY_PREFIX "")
ADD_LIBRARY(Derived SHARED Derived.cpp)

# compile the bindings
find_package(pybind11 REQUIRED)

ADD_LIBRARY(_oxpy_lib STATIC bindings.cpp)
TARGET_LINK_LIBRARIES(_oxpy_lib ${PYTHON_LIBRARIES} pybind11::module)
SET_TARGET_PROPERTIES(_oxpy_lib PROPERTIES POSITION_INDEPENDENT_CODE ON)

pybind11_add_module(my_module SHARED bindings.cpp)
TARGET_LINK_LIBRARIES(my_module PRIVATE pybind11::module _oxpy_lib)
