#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 리스트의 끝에서 n 번째까지의 값을 반환하는 함수
def take_n_right(lst, n=1):
    return lst[-n:] if n > 0 else []


if __name__ == "__main__":
    lst = [1, 2, 3, 4, 5]
    print(take_n_right(lst, 3))
    print(take_n_right(lst, 0))
    print(take_n_right(lst, -1))
