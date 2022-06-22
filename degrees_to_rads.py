#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from math import pi

# Converts an angle from degrees to radians

# Use math.pi and the degrees to radians formula
# to convert the angle from degrees to radians


def degree_to_rads(deg):
    return (deg * pi) / 180.0


if __name__ == "__main__":
    lst = [30, 45, 60, 90]
    for x in lst:
        print(str(x) + " => " + str(degree_to_rads(x)))
