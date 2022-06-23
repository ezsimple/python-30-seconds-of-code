#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Checks if the given number falls within the given range

# Use arithmetic comparison to check if the given number is the specified range.
# If the second, end, is not specified, the range is considered to be from 0 to start


def in_range(n, start, end=0):
    # 조건식 풀이가 조금 까리한데 .... 이게 가독성이 좋은가는 의문?
    return start <= n <= end if end >= start else end <= n <= start


if __name__ == "__main__":
    print(in_range(3, 1, 4))
    print(in_range(5, 2, 4))
    print(in_range(5, 2))
