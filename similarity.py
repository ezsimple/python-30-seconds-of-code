#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 두 리스트에 동일하게 존재하는 리스트를 반환하는 함수


def similar(list1, list2):
    return [i for i in list1 if i in list2]


if __name__ == "__main__":
    lst1 = [1, 2, 3, 4, 5]
    lst2 = [4, 5, 6, 7, 8]
    print(similar(lst1, lst2))
