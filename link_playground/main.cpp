#include <dlfcn.h>
#include <iostream>
#include <stdexcept>

void RunFromLib(char libName[], char funcName[]) {
    void* handle = dlopen(libName, RTLD_LAZY);
    if (!handle) {
        std::cerr << "Cannot open library " << libName << "!" << std::endl;
        throw std::runtime_error("error!");
    }

    typedef void (*func_t)();

    func_t func = (func_t)dlsym(handle, funcName);
    if (!func) {
        std::cerr << "Cannot load function " << funcName << "!" << std::endl;
        throw std::runtime_error("error!");
    }
    func();
}

int main(int argc, char** argv) {
    RunFromLib(argv[1], argv[2]);
    return 0;
}
