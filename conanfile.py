#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/2.0.0@bincrafters/testing")


class BoostNumeric_OdeintConan(base.BoostBaseConan):
    name = "boost_numeric_odeint"
    version = "1.70.0"
    boost_source_repo = {'numeric_odeint': "odeint"}
