#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 라디언을 디그리로 변환하는 함수


from math import pi


def rads_to_degrees(radians):
    return radians * 180 / pi


if __name__ == "__main__":
    x = 18
    print(rads_to_degrees(x))
