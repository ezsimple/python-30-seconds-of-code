#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# Filters out the unique values in a list

# Use a collections.Counter to get the count of each value in the list.

# Use list comprehension to create a list containing only the non-unique values

from asyncore import loop
from typing import Counter


def filter_unique(lst):
    # return Counter(lst).items()  # dict_items([(1, 1), (2, 1), (3, 1), (4, 1)])
    return [x for x, i in Counter(lst).items() if i > 1]


if __name__ == "__main__":
    lst = [1, 2, 3, 4, 4, 5, 5, 5, 7, 8]
    print(filter_unique(lst))
