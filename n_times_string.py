#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 주어진 문자열을 n 번 반복해서 리턴하는 함수
# Return the given string s, n times concatenated using the * operator


def n_times_string(s, n):
    return s * n


if __name__ == "__main__":
    print(n_times_string("hello", 3))
