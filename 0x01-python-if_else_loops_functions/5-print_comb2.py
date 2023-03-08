#!/usr/bin/python3
for foo in range(0, 100):
    if foo == 99:
        print(f'{foo:0=2d}')
    else:
        print(f'{foo:0=2d}', end=',')
