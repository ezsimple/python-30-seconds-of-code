#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 리스트의 모든 키를 리턴하는 함수


def keys_only(lst):
    return [key for key in lst]


if __name__ == "__main__":
    lst = {"a": 1, "b": 2, "c": 3}
    print(keys_only(lst))
