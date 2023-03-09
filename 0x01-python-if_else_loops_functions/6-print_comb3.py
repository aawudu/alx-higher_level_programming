#!/usr/bin/python3
for foo1 in range(0, 10):
    for foo2 in range(0, 10):
        if foo1 == 8 & foo2 == 9:
            print("{}{}".format(foo1, foo2))
        elif foo1 < foo2:
            print("{}{}".format(foo1, foo2), end=', ')
