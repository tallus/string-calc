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
from stringcalc.stringcalc import str_add

# Constants

# Helper Functions & Classes
def strgen(start=0, stop=100, num=20):
    """Return list of [num] random numbers between start and stop"""
    return [random.randrange(start, stop) for _ in range(num)]


# Tests
class StringCalcTests(unittest.TestCase):
    """Tests for str_add function"""
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


if __name__ == "__main__":
    unittest.main()
