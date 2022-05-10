import sys, os

sys.setdlopenflags(os.RTLD_GLOBAL | os.RTLD_LAZY)
import subprocess


def write_code():
    with open("temp_f.cpp", "w") as f:
        f.write(
            f"""
#include <iostream>

extern "C" {{
void hello_();
void param0()
{{
hello_();
}}
}}
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
    ["gcc", "-o", lib_path, "temp_f.o", "-shared", "-L.", "-lhello", "-lgfortran"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)
assert not p.stderr


import my_module

mat = my_module.LoadedMaterial(lib_path)
mat.param0()
