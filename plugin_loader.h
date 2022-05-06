#pragma once
#include "Base.h"

#include <dlfcn.h>
#include <iostream>

typedef Base *make_base();

Base *load_plugin(char name[]) {
    void *handle = dlopen(name, RTLD_LAZY | RTLD_GLOBAL);
    const char *dl_error = dlerror();
    if (dl_error != nullptr) {
        std::cerr << "Caught an error while opening shared library: "
                  << dl_error << std::endl;
        return NULL;
    }
    make_base *entry = (make_base *)dlsym(handle, "make");

    return (Base *)entry();
}

