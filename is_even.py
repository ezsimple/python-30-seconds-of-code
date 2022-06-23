#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 주어진 숫자가 짝수일 경우 True, 아닌 경우 False를 리턴하는 함수

# Returns True if the given number is even, False otherwise

# Check whether a number is odd or even using the modulo(%) operator
# Returns True if the given number is even, False otherwise


def is_even(n):
    return n % 2 == 0


if __name__ == "__main__":
    print(is_even(3))
    print(is_even(4))
