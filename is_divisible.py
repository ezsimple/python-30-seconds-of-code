#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 첫번째 숫자가 두번째 숫자로 나누어 떨어지는지 판별하세요.

# Checks if the first number is divisible by the second number

# Use the modulo operator(%) to check if the first number is divisible by the second number


def is_divisible(n, m):
    return n % m == 0


if __name__ == "__main__":
    print(is_divisible(3, 3))
    print(is_divisible(13, 3))
    print(is_divisible(12, 4))
