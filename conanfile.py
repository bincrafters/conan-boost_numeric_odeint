from conans import ConanFile, tools, os

class BoostNumeric_OdeintConan(ConanFile):
    name = "Boost.Numeric_Odeint"
    version = "1.65.1"
    short_paths = True
    url = "https://github.com/bincrafters/conan-boost-odeint"
    description = "Please visit http://www.boost.org/doc/libs/1_65_1/libs/libraries.htm"
    license = "www.boost.org/users/license.html"
    lib_short_names = ["odeint"]
    requires =  "Boost.Array/1.65.1@bincrafters/stable", \
                      "Boost.Assert/1.65.1@bincrafters/stable", \
                      "Boost.Bind/1.65.1@bincrafters/stable", \
                      "Boost.Compute/1.65.1@bincrafters/stable", \
                      "Boost.Config/1.65.1@bincrafters/stable", \
                      "Boost.Core/1.65.1@bincrafters/stable", \
                      "Boost.Function/1.65.1@bincrafters/stable", \
                      "Boost.Fusion/1.65.1@bincrafters/stable", \
                      "Boost.Iterator/1.65.1@bincrafters/stable", \
                      "Boost.Math/1.65.1@bincrafters/stable", \
                      "Boost.Mpi/1.65.1@bincrafters/stable", \
                      "Boost.Mpl/1.65.1@bincrafters/stable", \
                      "Boost.Multi_Array/1.65.1@bincrafters/stable", \
                      "Boost.Numeric_Ublas/1.65.1@bincrafters/stable", \
                      "Boost.Preprocessor/1.65.1@bincrafters/stable", \
                      "Boost.Range/1.65.1@bincrafters/stable", \
                      "Boost.Static_Assert/1.65.1@bincrafters/stable", \
                      "Boost.Throw_Exception/1.65.1@bincrafters/stable", \
                      "Boost.Type_Traits/1.65.1@bincrafters/stable", \
                      "Boost.Units/1.65.1@bincrafters/stable", \
                      "Boost.Utility/1.65.1@bincrafters/stable"

                      #array3 assert1 bind3 compute14 config0 core2 function5 fusion5 iterator5 math8 mpi14 mpl5 multi_array6 numeric~ublas12 preprocessor0 range7 static_assert1 throw_exception2 type_traits3 units12 utility5
                      
    def source(self):
        boostorg_github = "https://github.com/boostorg"
        archive_name = "boost-" + self.version  
        for lib_short_name in self.lib_short_names:
            tools.get("{0}/{1}/archive/{2}.tar.gz"
                .format(boostorg_github, lib_short_name, archive_name))
            os.rename(lib_short_name + "-" + archive_name, lib_short_name)

    def package(self):
        for lib_short_name in self.lib_short_names:
            include_dir = os.path.join(lib_short_name, "include")
            self.copy(pattern="*", dst="include", src=include_dir)		

    def package_id(self):
        self.info.header_only()