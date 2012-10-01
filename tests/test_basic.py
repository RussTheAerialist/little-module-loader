import unittest
import types

import little_module_loader as lml

from test_module import TestParent

TEST_MODULE = "tests.test_module"

class BasicTest(unittest.TestCase):
    def test_find(self):
        """little.module_loader.find - nominal case"""
        ut = dict(lml.find(TEST_MODULE, lambda x: x.startswith("find_")))
        self.assertTrue(len(ut)>0)
        self.assertIsInstance(ut, types.DictType)
        self.assertIn('find_plugin', ut)
        self.assertIsInstance(ut['find_plugin'], types.ModuleType)
        
    def test_class_finder_default_predicate(self):
        """little.module_loader.class_finder - nominal case"""
        ut = dict(lml.class_finder(TEST_MODULE, TestParent))
        self.assertTrue(len(ut)>0)
        self.assertIsInstance(ut, types.DictType)
        self.assertIn('TestClass', ut)
        
        cut = ut['TestClass']()
        self.assertTrue(isinstance(cut, TestParent))
        self.assertTrue(cut.exists, "Incorrect object created: {name}".format(name=type(cut).__name__))
        
    def test_function_finder_default_predicate(self):
        """little.module_loader.function_finder - nominal case"""
        ut = dict(lml.function_finder(TEST_MODULE, 'main'))
        self.assertTrue(len(ut)>0)
        for (name, func) in ut.items():
            self.assertEqual(func.__name__, name)
            self.assertTrue(callable(func))
            self.assertTrue(func())