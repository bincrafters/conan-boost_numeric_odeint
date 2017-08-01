from conans import ConanFile, tools, os

class BoostNumeric_OdeintConan(ConanFile):
    name = "Boost.Numeric_Odeint"
    version = "1.64.0"
    generators = "txt"
    url = "https://github.com/boostorg/odeint"
    description = "Please visit http://www.boost.org/doc/libs/1_64_0/libs/libraries.htm"
    license = "www.boost.org/users/license.html"
    lib_short_name = "odeint"
    requires =  "Boost.Array/1.64.0@bincrafters/testing", \
                      "Boost.Assert/1.64.0@bincrafters/testing", \
                      "Boost.Bind/1.64.0@bincrafters/testing", \
                      "Boost.Compute/1.64.0@bincrafters/testing", \
                      "Boost.Config/1.64.0@bincrafters/testing", \
                      "Boost.Core/1.64.0@bincrafters/testing", \
                      "Boost.Function/1.64.0@bincrafters/testing", \
                      "Boost.Fusion/1.64.0@bincrafters/testing", \
                      "Boost.Iterator/1.64.0@bincrafters/testing", \
                      "Boost.Math/1.64.0@bincrafters/testing", \
                      "Boost.Mpi/1.64.0@bincrafters/testing", \
                      "Boost.Mpl/1.64.0@bincrafters/testing", \
                      "Boost.Multi_Array/1.64.0@bincrafters/testing", \
                      "Boost.Numeric_Ublas/1.64.0@bincrafters/testing", \
                      "Boost.Preprocessor/1.64.0@bincrafters/testing", \
                      "Boost.Range/1.64.0@bincrafters/testing", \
                      "Boost.Static_Assert/1.64.0@bincrafters/testing", \
                      "Boost.Throw_Exception/1.64.0@bincrafters/testing", \
                      "Boost.Type_Traits/1.64.0@bincrafters/testing", \
                      "Boost.Units/1.64.0@bincrafters/testing", \
                      "Boost.Utility/1.64.0@bincrafters/testing"

                      #array3 assert1 bind3 compute14 config0 core2 function5 fusion5 iterator5 math8 mpi14 mpl5 multi_array6 numeric~ublas12 preprocessor0 range7 static_assert1 throw_exception2 type_traits3 units12 utility5
                      
    def source(self):
        self.run("git clone --depth=50 --branch=boost-{0} {1}.git"
                 .format(self.version, self.url))

    def package(self):
        include_dir = os.path.join(self.build_folder, self.lib_short_name, "include")
        self.copy(pattern="*", dst="", src=include_dir)

    def package_id(self):
        self.info.header_only()