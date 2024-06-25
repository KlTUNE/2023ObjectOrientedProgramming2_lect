#!/usr/bin/env python
# -*- coding: utf-8 -*-

def lecture01_01() -> None:
    h={}
    h["ID"] = 'k22121'
    # implement me
    h["attributes"] = ("正木雄也", 20, "男性")
    print(h)
    print(h.keys())
    print(type(h.keys()))
    print(type(h["attributes"]))

    attr = h["attributes"]
    for e in attr:
        print(e)

    for e in attr:
        print(type(e))

if __name__ == '__main__':
    lecture01_01()