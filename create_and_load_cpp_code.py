import subprocess


def write_code(msg="Greetings from c++!"):
    with open("temp.cpp", "w") as f:
        f.write(
            f"""
#include <iostream>
extern "C" {{
    void param0()
    {{
        std::cout << "{msg}" << std::endl;
    }}
}}
"""
        )

write_code("The parameter is 42.")

lib_path = "./my_tmp_lib.so"

p = subprocess.run(
    ["g++", "-shared", "-fPIC", "-o", lib_path, "temp.cpp"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)
assert not p.stderr

import my_module

mat = my_module.LoadedMaterial(lib_path)
mat.param0()
