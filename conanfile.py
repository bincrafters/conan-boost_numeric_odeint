#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.69.0@bincrafters/testing")

class BoostNumeric_OdeintConan(base.BoostBaseConan):
    name = "boost_numeric_odeint"
    url = "https://github.com/bincrafters/conan-boost_numeric_odeint"
    lib_short_names = ["odeint"]
    header_only_libs = ["odeint"]
    b2_requires = [
        "boost_array",
        "boost_assert",
        "boost_bind",
        "boost_compute",
        "boost_config",
        "boost_core",
        "boost_function",
        "boost_fusion",
        "boost_iterator",
        "boost_math",
        "boost_mpi",
        "boost_mpl",
        "boost_multi_array",
        "boost_numeric_ublas",
        "boost_preprocessor",
        "boost_range",
        "boost_static_assert",
        "boost_throw_exception",
        "boost_type_traits",
        "boost_units",
        "boost_utility"
    ]
