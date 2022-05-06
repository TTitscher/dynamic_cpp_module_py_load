#pragma once
#include "Base.h"

struct Derived : public Base {
    Derived();
    virtual ~Derived();
    void foo() override;
};

extern "C" Base *make() { return new Derived(); }
