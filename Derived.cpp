#include "Derived.h"

#include <iostream>

Derived::Derived() {}
Derived::~Derived() {}

void Derived::foo() { std::cout << "Hey, it's Derived!" << std::endl; }
