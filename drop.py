#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# Returns a list with n th elements removed from the left

# Use slice notation to remove the specified number of elements from the left


def drop(a, n=1):
    return a[n:]


if __name__ == "__main__":
    print(drop([1, 2, 3]))
    print(drop([1, 2, 3], 2))
    print(drop([1, 2, 3], 99))
