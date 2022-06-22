#!/usr/bin/env python3
# -*- coding:utf-8 -*-


def capitalize_every_work(s):
    return s.title()  # 모든 단어의 첫글자를 대문자로
    # return s[0].title() + s[1:]  # 문맥의 첫글자만 대문자로


if __name__ == "__main__":
    lst = ["hello", "good morning"]
    for o in lst:
        print(capitalize_every_work(o))
