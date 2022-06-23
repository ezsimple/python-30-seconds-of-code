#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Create a list of as many as you have

# Initialize a list containing the numbers in the specified range
# where start and end are inclusive with their common difference of step

# Use list and rang() to generate a list of the appropriate length,
# filled with the desired values in the given range.
# Omit start to use 0 as the start value.
# Omit step to use 1 as the step value.


def initialize_list_with_range(start=0, end=0, step=1):
    return list(range(start, end + 1, step))  # +1에 주목
