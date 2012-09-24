from setuptools import setup

setup(
    name = "little.module_loader",
    version = "0.1",
    packages = [ 'little.module_loader' ],
    namespace_packages = [ 'little' ],
    
    author = "Russell Hay",
    author_email = "me@russellhay.com",
    description = "A very simple module loader package for dynamically creating lists of modules, classes, and functions",
    license = "PSF",
    
    tests_require = [ "nose" ],
    test_suite = "tests", 
)