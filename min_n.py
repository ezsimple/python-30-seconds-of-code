#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 리스트에서 작은 순서대로 정렬해서, n개 를 반환하는 함수
# sorted()를 사용하여 정렬하고, n개를 반환하는 함수

# Returns the n minimum elements from ther provided list
# If n is greater than or equal to the length of the list,
# then return the entire list (sorted in ascending order)

# Use sorted() to sort the list, [:n] to get the specified number of elements
# Omit the second argument n to get a one-element list


def min(lst, n=1):
    return sorted(lst)[:n]


if __name__ == "__main__":
    lst = [1, 2, 3, 4, 5]
    print(min(lst, 3))
