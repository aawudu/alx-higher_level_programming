#!/usr/bin/python3
for cha in range(97, 122 + 1):
    if (cha == 113 or cha == 101):
        continue
    print("{}".format(chr(cha)), end='')
