#pragma once
#include <dlfcn.h>
#include <exception>
#include <iostream>
#include <string>

/*
 * Load a material following assumes that
 * `libname` is a shared library and includes
 *      void param0(double*);
 *      void eval(double*, double*);
 */

typedef void (*func_t)(double*);

class LoadedMaterial {
   public:
    LoadedMaterial(std::string libName) {
        _libHandle = dlopen(libName.c_str(), RTLD_LAZY);
        if (!_libHandle) {
            throw std::runtime_error("Cannot load " + libName + "!");
        }

        _f_param0 = (func_t)dlsym(_libHandle, "param0");
        if (!_f_param0) {
            throw std::runtime_error("Cannot load function 'param0' from " +
                                     libName + "!");
        }
    }

    double param0() {
        double out;
        _f_param0(&out);
        return out;
    }

   private:
    void* _libHandle;
    func_t _f_param0;
};
