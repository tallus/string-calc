#!/usr/bin/env python
# encoding: utf-8
"""
copyright (c) 2017 Paul Munday.
All rights reserved
..codeauthor::Paul Munday <paul@paulmunday.net>

Tests for string-calc
"""

# Imports from Standard Library
import random
import unittest

# Local Imports
from stringcalc.stringcalc import (_has_delim, str_add)

# Constants

# Helper Functions & Classes
def strgen(start=0, stop=100, num=20):
    """Return list of [num] random numbers between start and stop"""
    return [random.randrange(start, stop) for _ in range(num)]


# Tests
class StringCalcTests(unittest.TestCase):
    """Tests for str_add function and helpers"""
    # pylint: disable=R0904

    def test_null_input(self):
        """Test for null input (empty string)"""
        expected = 0
        result = str_add("")
        self.assertEqual(expected, result)

    def test_single_number(self):
        """Test single number as input"""
        expected = 1
        result = str_add("1")
        self.assertEqual(expected, result)

        expected = 10
        result = str_add("10")
        self.assertEqual(expected, result)

    def test_two_numbers(self):
        """Test for 2 number input"""
        expected = 3
        result = str_add("1, 2")
        self.assertEqual(expected, result)

        expected = 15
        result = str_add("11, 4")
        self.assertEqual(expected, result)

    def test_mutiple_postive_numbers(self):
        """Test for multi number input"""
        numbers = strgen()
        expected = sum(numbers)
        test_input = ",".join([str(n) for n in numbers])
        result = str_add(test_input)
        self.assertEqual(expected, result)

    def test_negative_numbers(self):
        """Test for multi number input, including negative numbers"""
        numbers = [1, 2, -4]
        expected = sum(numbers)
        test_input = ",".join([str(n) for n in numbers])
        result = str_add(test_input)
        self.assertEqual(expected, result)

    def test_two_numbers_new_line(self):
        """Test for 2 number input with new line separator"""
        expected = 3
        result = str_add("1\n2")
        self.assertEqual(expected, result)

    def test_mixed_delimitators(self):
        """Test for use  of , and new line as separators"""
        expected = 6
        result = str_add("1,2\n3")
        self.assertEqual(expected, result)

        expected = 6
        result = str_add("1\n2,3")
        self.assertEqual(expected, result)

        expected = 10
        # catch use of ', '
        result = str_add("1, 2,3\n4")
        self.assertEqual(expected, result)

    def test__has_delim(self):
        """Test to ensure delimators are identified correctly."""
        self.assertTrue(_has_delim("//;\n1;2"))
        self.assertTrue(_has_delim("//$\n1;2"))
        self.assertTrue(_has_delim("//$\n1$2"))
        self.assertFalse(_has_delim("/;\n1;2"))
        self.assertFalse(_has_delim("//\n1;2"))
        self.assertFalse(_has_delim("//@\1;2"))
        self.assertFalse(_has_delim("/;\1,2"))

    def test_mixed_defined_delimitators(self):
        """Test for use diffierent delimitators"""
        expected = 6
        result = str_add("//+\n1,2\n3")
        self.assertEqual(expected, result)

        # still works if defined delimitator not present
        expected = 6
        result = str_add("//+\n1,2\n3")
        self.assertEqual(expected, result)

        expected = 6
        result = str_add("1\n2,3")
        self.assertEqual(expected, result)

        expected = 10
        # catch use of ', '
        result = str_add("1, 2,3\n4")
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
