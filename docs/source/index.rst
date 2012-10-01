.. Little Module Loader documentation master file, created by
   sphinx-quickstart on Mon Sep 24 15:26:51 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Little Module Loader's documentation!
================================================
   
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

Functions
=========

Finding Modules
---------------

.. autofunction:: little.module_loader.find

Finding Classes
----------------

.. autofunction:: little.module_loader.class_finder

Finding Functions
------------------

.. autofunction:: little.module_loader.function_finder

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

