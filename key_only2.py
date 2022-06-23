#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 사전형에서 모든 키를 리스트로 반환하는 함수

# Returns a flat list of all the keys in a flat dictionary
# Use dict.keys() to return a list of all the keys in a dictionary
# Return a list() of the previous result


def keys_only(dic):
    return list(dic.keys())


if __name__ == "__main__":
    dic = {"a": 1, "b": 2, "c": 3}
    print(keys_only(dic))
