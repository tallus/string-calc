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
DELIMIT_MATCH = re.compile("^//.\n")

# Private Classes and Functions
def _get_delim(string):
    """
    Split string into delimitor and reminder.

    Default delimitator will be added to delimitator if found,
    or used in place if not
    """
    delim = ",|\\n"
    match = _has_delim(string)
    if match:
        pattern = match.group(0)
        new_delim = pattern.lstrip('//').strip()
        # TODO add other special chars
        if new_delim in [
                '|', '*', '+', '.', '[', '['
        ]:
            new_delim = '\\' + new_delim
        delim = "{}|{}".format(delim, new_delim)
        string = string[len(pattern):]
    return delim, string


def _has_delim(string):
    """Return True if string contains delimitator at start"""
    return re.match(DELIMIT_MATCH, string)


# Public Classes and Functions


def str_add(numbers):
    """
    Return the sum of numbers

    :param numbers: 0 or more numbers, separated by a comma
    :type numbers: str
    :returns: sum of numbers
    :rtype: int
    """
    delim, numbers = _get_delim(numbers)
    print delim, type(delim)
    numbers = re.split(delim, numbers)
    numbers = [int(number.strip()) for number in numbers if number]
    return sum(numbers)
