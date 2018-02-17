#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools


class BoostNumeric_OdeintConan(ConanFile):
    name = "boost_numeric_odeint"
    version = "1.65.1"
    url = "https://github.com/bincrafters/conan-boost_numeric_odeint"
    author = "Bincrafters <bincrafters@gmail.com>"
    exports = ["LICENSE.md"]
    lib_short_names = ["odeint"]
    is_header_only = True

    def package_id_additional(self):
        self.info.header_only()

    requires = (
        "boost_package_tools/1.65.1@bincrafters/stable",
        "boost_array/1.65.1@bincrafters/stable",
        "boost_assert/1.65.1@bincrafters/stable",
        "boost_bind/1.65.1@bincrafters/stable",
        "boost_compute/1.65.1@bincrafters/stable",
        "boost_config/1.65.1@bincrafters/stable",
        "boost_core/1.65.1@bincrafters/stable",
        "boost_function/1.65.1@bincrafters/stable",
        "boost_fusion/1.65.1@bincrafters/stable",
        "boost_iterator/1.65.1@bincrafters/stable",
        "boost_math/1.65.1@bincrafters/stable",
        "boost_mpi/1.65.1@bincrafters/stable",
        "boost_mpl/1.65.1@bincrafters/stable",
        "boost_multi_array/1.65.1@bincrafters/stable",
        "boost_numeric_ublas/1.65.1@bincrafters/stable",
        "boost_preprocessor/1.65.1@bincrafters/stable",
        "boost_range/1.65.1@bincrafters/stable",
        "boost_static_assert/1.65.1@bincrafters/stable",
        "boost_throw_exception/1.65.1@bincrafters/stable",
        "boost_type_traits/1.65.1@bincrafters/stable",
        "boost_units/1.65.1@bincrafters/stable",
        "boost_utility/1.65.1@bincrafters/stable"
    )

    # BEGIN

    description = "Please visit http://www.boost.org/doc/libs/1_65_1"
    license = "BSL-1.0"
    short_paths = True
    build_requires = "boost_generator/1.65.1@bincrafters/stable"

    def package_id(self):
        getattr(self, "package_id_additional", lambda:None)()

    def source(self):
        with tools.pythonpath(self):
            import boost_package_tools  # pylint: disable=F0401
            boost_package_tools.source(self)
        getattr(self, "source_additional", lambda:None)()

    def build(self):
        with tools.pythonpath(self):
            import boost_package_tools  # pylint: disable=F0401
            boost_package_tools.build(self)
        getattr(self, "build_additional", lambda:None)()

    def package(self):
        with tools.pythonpath(self):
            import boost_package_tools  # pylint: disable=F0401
            boost_package_tools.package(self)
        getattr(self, "package_additional", lambda:None)()

    def package_info(self):
        with tools.pythonpath(self):
            import boost_package_tools  # pylint: disable=F0401
            boost_package_tools.package_info(self)
        getattr(self, "package_info_additional", lambda:None)()



    # END
