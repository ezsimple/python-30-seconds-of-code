#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 리스트에서 n개의 큰순서를 반환하는 함수

# Returns the n maximum elements from the provided list
# If n is greater than or equal to the length of the list, return the entire list

# Use sorted() to sort the list, [:n] to get the specified number of elements
# Omit the second argument n to get a one-element list

# sorted 함수는 기본값으로 오름차순으로 정렬하므로 reverse=True로 반대로 정렬하는 것이다
# [:n] 을 사용해서 n개의 값을 반환하는 함수


def max_n(lst, n):
    return sorted(lst, reverse=True)[:n]


if __name__ == "__main__":
    lst = [1, 3, 3, 4, 5]
    print(max_n(lst, 3))
