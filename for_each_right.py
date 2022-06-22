#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# Executes the provided function once for each list element
# starting from the end of the list

# Use a for loop in combination with slice notation to execute func for each element in lst
# starting from the last element of lst


def for_each_right(lst, func):
    for i in lst[::-1]:  # 역순으로 읽기 위해서 슬라이스 사용
        func(i)


if __name__ == "__main__":
    lst = [1, 2, 3, 4, 5, 6, 7, 8]
    for_each_right(lst, print)
