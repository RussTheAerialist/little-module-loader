little-module-loader
====================

a little library for loading modules dynamically

[![Build Status](https://secure.travis-ci.org/RussTheAerialist/little-module-loader.png)](http://travis-ci.org/RussTheAerialist/little-module-loader)

[![endorse](http://api.coderwall.com/russtheaerialist/endorsecount.png)](http://coderwall.com/russtheaerialist)

Example Usage
=============

Finding modules based on filename:

    import little.module_loader
    parent = "petit"
  
    # this returns a dictionary that maps name of module (without parent) and the actual module object
    dict(little.module_loader.find(parent, lambda x: x.endswith("_subsystem.py")))

Finding all classes that are subclasses of another class:
  
    # this returns a dictionary that maps the name of the class to the class object for instantiation
    dict(class_finder("petit.packets", Packet))

View the rest of the documentation here: http://packages.python.org/little.module_loader/