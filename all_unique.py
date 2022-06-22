#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 주어진 리스트의 항목이 모두 unique한지 확인한다
# set & len 을 활용한 예제
def all_unique(lst):
    return len(lst) == len(set(lst))


if __name__ == "__main__":
    x = [1, 2, 3, 4, 5, 6]
    y = [1, 3, 5, 7, 2, 3]
    print(all_unique(x))
    print(all_unique(y))
