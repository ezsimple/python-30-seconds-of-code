#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# remove falsey values from a list
# use filter() to filter out falsey values ( False, None, 0, "" )


def compact(lst):
    return list(filter(None, lst))


if __name__ == "__main__":
    lst = [0, 1, False, 2, "", 3, "a", "s", 34]
    print(compact(lst))
