#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# Counts the occurrences of a value in a list
# Increment a counter for every item in the list that has the given value and is of the same type


def count_occurrences(lst, val):
    return len([x for x in lst if x == val and type(x) == type(val)])


if __name__ == "__main__":
    lst = [1, 2, 1, 2, 2, 3, 8, 8, 8]
    print(count_occurrences(lst, 1))
