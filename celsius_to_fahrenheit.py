#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 섭씨온도를 화씨온도로 변환 하세요
def celsius_to_fahrenheit(celsius):
    return (celsius * 1.8) + 32


if __name__ == "__main__":
    lst = [18, 20, 23]
    for o in lst:
        print(celsius_to_fahrenheit(o))
