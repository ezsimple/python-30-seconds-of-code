#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# Convert Fahrenheit to Celsius

# Use the formula celsius = (fahrenheit - 32) / 1.8
# to convert from Fahrenheit to Celsius


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) / 1.8


if __name__ == "__main__":
    print(fahrenheit_to_celsius(77))
