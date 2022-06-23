#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 리스트에서 첫번째 값을 제외한 나머지 값들을 리턴하는 함수
# 만약 목록의 갯수가 1개 이상일 경우에만 제외하고, 1개인 경우는 전부 반환하는 함수


def tail(lst):
    return lst[1:] if len(lst) > 1 else lst


if __name__ == "__main__":
    lst = [1, 2, 3, 4, 5]
    print(tail(lst))
    lst = [1]
    print(tail(lst))
