import subprocess


def write_code(ret_val):
    with open("temp.cpp", "w") as f:
        f.write(
            f"""
#include <iostream>
extern "C" {{
    void param0(double* out)
    {{
        (*out) = 42;
    }}
}}
"""
        )

write_code(42)

lib_path = "./my_tmp_lib.so"

p = subprocess.run(
    ["g++", "-shared", "-fPIC", "-o", lib_path, "temp.cpp"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)
assert not p.stderr

import my_module

mat = my_module.LoadedMaterial(lib_path)
assert mat.param0() == 42.0;
