#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 딕셔너리의 모든값을 리스트로 반환하는 함수


def values_only(d):
    return list(d.values())


if __name__ == "__main__":
    d = {"a": 1, "b": 2, "c": 3}
    print(values_only(d))
