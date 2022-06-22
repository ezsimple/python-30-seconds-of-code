#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# Returns the difference between two iterables

# Create a set from b as _b,
# then use list comprehension on a
# to only keey values not contained in the previousle create set, _b


def difference(a, b):
    _b = set(b)
    return [x for x in a if x not in _b]


if __name__ == "__main__":
    x = [1, 2, 3, 5, 7]
    y = [1, 2, 3, 4, 5]
    print(difference(x, y))
