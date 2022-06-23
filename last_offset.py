#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Moves the specified amount of elements to the end of the list

# Use lst[offset:] and lst[:offset] to get the two slices of the list
# and combine them before returning the result


def offset(lst, offset):
    return lst[offset:] + lst[:offset]


if __name__ == "__main__":
    lst = [1, 2, 3, 4, 5]
    print(offset(lst, 2))
