# test_dagsterasset.py
"""
Tests for DagsterAsset module.
"""

import unittest
from dagsterasset import DagsterAsset

class TestDagsterAsset(unittest.TestCase):
    """Test cases for DagsterAsset class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DagsterAsset()
        self.assertIsInstance(instance, DagsterAsset)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DagsterAsset()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
