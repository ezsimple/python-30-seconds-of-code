#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 리스트에서 가장 많이 중복되는 값을 가져오는 함수
# set()과 list.count()를 활용하는 문제

# Returns the most frequent element in the list
# Use set() and list.count() to get the most frequent element in a list


def most_frequent(lst):
    # d = {}
    # for i in lst:
    #     if i in d:
    #         d[i] += 1
    #     else:
    #         d[i] = 1
    # return max(d, key=d.get)
    return max(set(lst), key=lst.count)


# 리스트에서 나온 횟수를 나타내는 함내
def frequency(lst):
    # d = {}
    # for i in lst:
    #     if i in d:
    #         d[i] += 1
    #     else:
    #         d[i] = 1
    # return d
    return {i: lst.count(i) for i in set(lst)}


if __name__ == "__main__":
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 7, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(lst)
    print(most_frequent(lst))
    print(frequency(lst))
