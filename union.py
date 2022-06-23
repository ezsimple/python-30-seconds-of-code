#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 주어진 두개의 목록에서 최소 1번 이상 있는 값을 반환하는 함수
def union(lst1, lst2):
    return list(set(lst1 + lst2))


if __name__ == "__main__":
    lst1 = [1, 2, 3, 4, 5]
    lst2 = [3, 4, 5, 6, 7]
    print(union(lst1, lst2))
