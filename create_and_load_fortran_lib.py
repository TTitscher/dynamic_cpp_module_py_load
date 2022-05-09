import sys, os

sys.setdlopenflags(os.RTLD_GLOBAL | os.RTLD_LAZY)
import subprocess


def write_code(msg="Greetings!"):
    with open("temp.cpp", "w") as f:
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

lib_path = "./my_tmp_lib.so"

p = subprocess.run(
    ["gcc","-shared", "-fpic" , "-c", "temp.cpp"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)
print(p)

p = subprocess.run(
    ["gcc", "-o", lib_path, "temp.o","-shared" , "-L.", "-lhello", "-lgfortran"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)
print(p.stderr)

import my_module

my_module.load_plugin("./my_tmp_lib.so").foo()
