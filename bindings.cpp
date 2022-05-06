#include <pybind11/pybind11.h>

#include "Base.h"
#include "plugin_loader.h"

PYBIND11_MODULE(my_module, m) {
    pybind11::class_<Base, std::shared_ptr<Base>> base(m, "Base");

    base.def(pybind11::init<>());
    base.def("foo", &Base::foo);

    m.def("load_plugin", &load_plugin);
}

