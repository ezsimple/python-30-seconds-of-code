#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# Filter out the non-unique values in a list

# Use a collections.Counter to get the count of each value in the list.
# Use list comprehension to create a list containing only the unique values

from collections import Counter


def filter_non_unique(lst):
    return [item for item, count in Counter(lst).items() if count == 1]


if __name__ == "__main__":
    lst = [1, 2, 3, 3, 4, 4, 5, 6]
    print(filter_non_unique(lst))
