cmake_minimum_required(VERSION 3.5 FATAL_ERROR)
PROJECT(foobar)

# compile the bindings
find_package(pybind11 REQUIRED)


pybind11_add_module(my_module SHARED bindings.cpp)
TARGET_LINK_LIBRARIES(my_module PRIVATE pybind11::module)
