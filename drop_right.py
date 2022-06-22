#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# Returns a list with n elements removed from the right

# Use slice notation to remove the specified number of elements from the right


def drop_right(a, n=1):
    return a[:-n]


if __name__ == "__main__":
    lst = [1, 2, 3]
    print(drop_right(lst))
    print(drop_right(lst, 2))
