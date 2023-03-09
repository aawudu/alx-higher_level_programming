#!/usr/bin/python3
for foo1 in range(0, 10):
    for foo2 in range(foo1 + 1, 10):
        if foo1 == 8 and foo2 == 9:
            print("{}{}".format(foo1, foo2))
        else:
            print("{}{}".format(foo1, foo2), end=", ")
