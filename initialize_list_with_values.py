#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 주어진 값으로 채워진 리스트를 만드세요

# Initializes and fills a list with the given value

# Use list comprehension and range() to generate a list of length equal to n,
# filled with the given value.
# Omit v to use 0 as the default value.


def initialize_list_with_values(n, v=0):
    return [v for i in range(n)]


if __name__ == "__main__":
    print(initialize_list_with_values(3, 1))
    print(initialize_list_with_values(5, 2))
    print(initialize_list_with_values(7, 3))
