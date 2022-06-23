#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Return all the elements in the list except the last one

# Use lst[0:-1] to return all but the last element of the list


def initial(lst):
    return lst[0:-1]  # 마지막 하나를 제외한 모든 요소를 리턴하는 함수


if __name__ == "__main__":
    lst = [1, 2, 3, 4, 5]
    print(initial(lst))
