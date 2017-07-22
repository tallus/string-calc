#!/usr/bin/env python
# encoding: utf-8
"""
copyright (c) 2017 Paul Munday.
All rights reserved
..codeauthor::Paul Munday <paul@paulmunday.net>

String Calc Kata
"""

# Imports from Standard Library
import re

# Imports from Third Party Modules

# Local Imports

# Setup

# Constants

# Data Structure Definitions


# Private Classes and Functions


# Public Classes and Functions
def str_add(numbers):
    """
    Return the sum of numbers

    :param numbers: 0 or more numbers, separated by a comma
    :type numbers: str
    :returns: sum of numbers
    :rtype: int
    """
    numbers = re.split(",|\n", numbers)
    numbers = [int(number.strip()) for number in numbers if number]
    return sum(numbers)
