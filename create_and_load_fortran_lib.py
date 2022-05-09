import sys, os

sys.setdlopenflags(os.RTLD_GLOBAL | os.RTLD_LAZY)
import subprocess


def write_code(msg="Greetings!"):
    with open("temp_f.cpp", "w") as f:
        f.write(
            f"""
#include "Derived.h"

#include <iostream>

extern "C" {{
void hello_();
}}

Derived::Derived() {{}}
Derived::~Derived() {{}}

void Derived::foo() {{ hello_(); }}
"""
        )


write_code()

lib_path = "./my_tmp_f_lib.so"

p = subprocess.run(
    ["gcc", "-shared", "-fpic", "-c", "temp_f.cpp"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)

p = subprocess.run(
    ["gcc", "-o", lib_path, "temp.o", "-shared", "-L.", "-lhello", "-lgfortran"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)

import my_module

my_module.load_plugin(lib_path).foo()
