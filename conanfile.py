from conans import ConanFile, tools
import os

class Catch2Conan(ConanFile):
    name = "Catch2"
    license = "BSL-1.0 License"
    description = "A modern, C++-native, header-only, test framework for unit-tests, TDD and BDD."
    url = "https://github.com/catchorg/Catch2"

    # Settings and options
    settings = "os", "compiler", "arch"

    options = { "single_header":[True, False] }
    default_options = { "single_header":True }

    # Additional files to export
    exports_sources = ["premake5.lua"]

    # Iceshard conan tools
    python_requires = "conan-iceshard-tools/0.6.2@iceshard/stable"
    python_requires_extend = "conan-iceshard-tools.IceTools"

    def package_id(self):
        self.info.header_only()
        self.info.options.single_header = "Any"

    # Initialize the package
    def init(self):
        self.ice_init("none")

    def package(self):
        self.copy("LICENSE.txt", src=self._ice.out_dir)
        self.copy("*", src=os.path.join(self._ice.out_dir, "include"), dst=os.path.join("include", "catch2"))
        self.copy("*", src=os.path.join(self._ice.out_dir, "single_include"), dst="single_include")

    def package_info(self):
        self.cpp_info.debug = None
        self.cpp_info.release = None

        if self.options.single_header:
            self.cpp_info.includedirs = [ "single_include" ]

        else:
            self.cpp_info.includedirs = [ "include" ]
