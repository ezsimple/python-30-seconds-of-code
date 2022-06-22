#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# Returns every nth element in a list

# Use [nth-1::nth] to create a new list that contains every nth element of the given list

# nth is step of elements


def every_nth(lst, nth):
    return lst[nth - 1 :: nth]


if __name__ == "__main__":
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(every_nth(lst, 2))
    print(every_nth(lst, 3))
