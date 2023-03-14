#!/usr/bin/python3
# 1-calculation.py
# Aisha Aawudu <awuduaisha@gmail.com>

if __name__ == "__main__":
    """Result  adds, mulptiplies, subtracts, and divides
    quotient of 10 and 5."""
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
