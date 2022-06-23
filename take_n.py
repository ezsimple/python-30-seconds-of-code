#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 주어진 목록으로, 앞에서 부터 n개의 값을 반환하는 함수
# n이 0일 경우에는 빈 리스트를 반환하는 함수
# n이 목록의 길이보다 클 경우에는 목록의 마지막 n개를 반환하는 함수


def take_n(lst, n=1):
    return lst[:n] if n > 0 else []


if __name__ == "__main__":
    lst = [1, 2, 3, 4, 5]
    print(take_n(lst, 3))
    print(take_n(lst, 0))
    print(take_n(lst, -1))
