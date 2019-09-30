## compile for local use:

conan create . memunix/stable

## use in CMakeLists.txt

conan_cmake_run(REQUIRES
        simdjson/0.2.1@memunix/stable
        BASIC_SETUP BUILD missing
        )
