#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 리스트에서 중간값을 가져오는 함수

# lst.sort()로 정렬하면 오름차순으로 정렬되어있으므로,
# lst[len(lst) // 2] 와 lst[len(lst) // 2 - 1]을 더해서 2로 나누면 중간값이 나옴
# len(lst) // 2 는 리스트의 길이를 2로 나누면 중간값이 나옴


def median(lst):
    lst.sort()  # 목록의 순서가 변경됩니다.
    if len(lst) % 2 == 0:
        return (lst[len(lst) // 2] + lst[len(lst) // 2 - 1]) / 2
    else:
        return lst[len(lst) // 2]


if __name__ == "__main__":
    lst = [1, 2, 3, 4, 5, 6]
    print(median(lst))
