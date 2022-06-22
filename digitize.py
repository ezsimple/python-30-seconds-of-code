#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# Convers a number to a list of digits

# Use map() combined with int
# on the string representaion of n
# and return a list from the result


def digitize(n):
    print(list(map(int, str(n))))  # int is function


if __name__ == "__main__":
    print(digitize("12301"))
