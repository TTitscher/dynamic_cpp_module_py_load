#include <pybind11/pybind11.h>

#include "LoadedMaterial.h"

PYBIND11_MODULE(my_module, m) {
    pybind11::class_<LoadedMaterial> base(m, "LoadedMaterial");

    base.def(pybind11::init<std::string>());
    base.def("param0", &LoadedMaterial::param0);
}

