#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 1. 여러줄로 나눠진 문장을 리스트로 반환하는 함수
# 2. trim 사용하여 공백을 제거하는 함수
# 3. 빈줄은 삭제하는 함수


def split_lines(text):
    return [line.strip() for line in text.splitlines() if line.strip()]


if __name__ == "__main__":
    text = """
    첫째 줄
    둘째 줄
    셋째 줄
    """
    print(split_lines(text))
