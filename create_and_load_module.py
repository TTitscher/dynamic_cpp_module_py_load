import sys, os

sys.setdlopenflags(os.RTLD_GLOBAL | os.RTLD_LAZY)
import subprocess


def write_code(msg="Greetings!"):
    with open("temp.cpp", "w") as f:
        f.write(
            f"""
#include "../Derived.h"

#include <iostream>

Derived::Derived() {{}}
Derived::~Derived() {{}}

void Derived::foo() {{ std::cout << "{msg}" << std::endl; }}
"""
        )


write_code()

lib_path = "./my_tmp_lib.so"

p = subprocess.run(
    ["gcc", "-shared", "-fpic", "-o", lib_path, "temp.cpp"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)

import my_module

my_module.load_plugin("./my_tmp_lib.so").foo()
