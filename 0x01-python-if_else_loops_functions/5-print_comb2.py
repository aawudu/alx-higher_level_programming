#!/usr/bin/python3
for foo in range(0, 100):
    if foo == 99:
        print("{}".format(foo))
    else:
        print("{:02}".format(foo), end=', ')
