#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# Returns True if the list contains any duplicate values

# Use set() on the given list to remove all duplicate values
# Compare it's length with the length of the list
# to determine if there are duplicates

def has_duplicates(lst):
    return len(lst) != len(set(lst))


if __name__ == "__main__":
    x = [1, 2, 3, 4, 4, 5, 5, 5, 7, 8]
    y = [1, 2, 3, 4, 5, 6, 7, 8]
    print(has_duplicates(x))
    print(has_duplicates(y))
