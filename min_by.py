#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 주어진 목록에서 최소값을 구하세요.
# map()과 fn, min()을 사용하세요.
# lambda x: x 는 x의 값을 리턴하는 함수입니다.


def min_by(lst, fn):
    return min(map(fn, lst))


if __name__ == "__main__":
    lst = [1, -2, 3, 4, 5]
    print(min_by(lst, lambda x: x))
    lst = [{"n": 4}, {"n": 2}, {"n": -8}]
    print(min_by(lst, lambda x: x["n"]))
