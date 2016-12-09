cmake_minimum_required(VERSION 3.6)
project(cppSolutions)

set(CMAKE_CXX_STANDARD 11)

set(SOURCE_FILES main.cpp solution.cpp solution.h)
add_executable(cppSolutions ${SOURCE_FILES})