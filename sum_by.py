#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 리스트에서 주어진 함수 fn 을 사용해서, 각각 mapping후 합계를 리턴하는 함수


def sum_by(lst, fn):
    return sum(map(fn, lst))


if __name__ == "__main__":
    lst = [1, 2, 3, 4, 5]
    print(sum_by(lst, lambda x: x * x))
