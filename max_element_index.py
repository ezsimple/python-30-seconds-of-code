#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 리스트에서 최대값을 가진 인덱스를 반환하는 함수
# Use max() and list.index() to get the maximum value in a list and return its index


def max_element_index(lst):
    return lst.index(max(lst))  # 값을 가지고 index를 찾는 함수 list.index()


# 리스트에서 최소값을 가진 인덱스를 반환하는 함을
def min_element_index(lst):
    return lst.index(min(lst))


if __name__ == "__main__":
    lst = [3, 2, 7, 4, 5]
    print(max_element_index(lst))
    print(min_element_index(lst))
