#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 리스트에서 랜덤하게 값을 가져오는 함수

from random import choice


def sample(list):
    return choice(list)


if __name__ == "__main__":
    lst = [1, 2, 3, 4, 5]
    print(sample(lst))
