#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 주어진 값들에서 최대값을 리턴하는 함수


from functools import reduce


def max_by(lst, key):
    return max(lst, key=key)


if __name__ == "__main__":
    lst = [1, 6, 3, 4, 5]
    print(max(lst, key=lambda x: x))
    print(lst)
    print(list(map(lambda x: x * 2, lst)))
    print(reduce(lambda x, y: x + y, lst))
    print(list(filter(lambda x: x % 2 == 0, lst)))
