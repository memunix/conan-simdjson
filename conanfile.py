from conans import ConanFile, CMake, tools
import shutil
import os

class SimdJsonConan(ConanFile):
    name        = "simdjson"
    version     = "0.2.1"
    license     = "MIT"
    author      = "toge.mail@gmail.com"
    url         = "https://bitbucket.org/toge/conan-simdjson/"
    description = "Parsing gigabytes of JSON per second"
    topics      = ("json", "simd")
    settings    = "os", "compiler", "build_type", "arch"
    generators  = "cmake"

    def source(self):
        tools.get("https://github.com/lemire/simdjson/archive/v{}.zip".format(self.version))
        shutil.move("simdjson-{}".format(self.version), "simdjson")

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_dir="simdjson", defs={"SIMDJSON_BUILD_STATIC": "ON"})
        cmake.build(target="simdjson")

    def package(self):
        self.copy("*.h",     dst="include", src="simdjson/include")
        self.copy("*.lib",   dst="lib",     keep_path=False)
        self.copy("*.dll",   dst="bin",     keep_path=False)
        self.copy("*.so",    dst="lib",     keep_path=False)
        self.copy("*.dylib", dst="lib",     keep_path=False)
        self.copy("*.a",     dst="lib",     keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["simdjson"]

