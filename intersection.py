#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 두 자료형에 존재하는 값을 반환 하세요

# Returns a list of elements that exist in both lst1 and lst2

# Create a set from a passed list, the use the built-in set operator & to only keep values
# contained in both lists., then transform the set back into a list.


def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))


if __name__ == "__main__":
    lst1 = [1, 2, 3, 4, 5]
    lst2 = [4, 5, 6, 7, 8]
    print(intersection(lst1, lst2))
