""" Provides a few functions for loading modules (and classes) from a package

    Examples
    ---------
    
    Finding modules based on filename::
    
        import little.module_loader
        parent = "petit"
        
        dict(little.module_loader.find(parent, lambda x: x.endswith("_subsystem.py")))
        # this returns a dictionary that maps name of module (without parent) and the actual module object
            
    Finding all classes that are subclasses of another class::
    
        dict(class_finder("petit.packets", Packet))
        # this returns a dictionary that maps the name of the class to the class object for instantiation
"""
import os.path as path
import types
from pkg_resources import resource_listdir
import importlib

def load_module(parent_package, module_name):
    try:
        full_module_name = "{parent_package}.{module_name}".format(parent_package=parent_package,
                                                           module_name=module_name)

        module = importlib.import_module(full_module_name)
        return module
    except ImportError,ex:
        print ex
        return None

def find(parent_package, predicate):
    for system in filter(predicate, resource_listdir(parent_package, '')):
        (module_name, ext) = path.splitext(system)
        if ext == ".py":
            retval = load_module(parent_package, module_name)
            if retval is not None:
                yield (module_name, retval)
                
def class_finder(parent_package, parent_class, predicate = lambda x: not x.endswith('__init__.py')):
    for (name, module) in find(parent_package, predicate):
        for x in [getattr(module, y) for y in dir(module)]:
            if types.TypeType == type(x) and issubclass(x, parent_class):
                yield (x.__name__, x)

def function_finder(parent_package, function_name, predicate = lambda x: not x.endswith('__init__.py')):
    for (name, module) in find(parent_package, predicate):
        for x in [getattr(module, y) for y in dir(module) if y == function_name]:
            if callable(x):
                yield(x.__name__, x)