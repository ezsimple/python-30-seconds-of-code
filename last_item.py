#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 리스트의 마지막 값을 가져오는 함수

# Returns the last element of the list
# Use lst[-1] to return the last element of parameter list


def last(lst):
    return lst[-1]


if __name__ == "__main__":
    lst = [1, 2, 3, 4, 5]
    print(last(lst))
