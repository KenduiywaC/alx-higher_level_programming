#!/usr/bin/python3
a = 10
b = 5

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    result_add = add(a, b)
    result_sub = sub(a, b)
    result_mul = mul(a, b)
    result_div = div(a, b)

    print("10 + 5 =", result_add)
    print("10 - 5 =", result_sub)
    print("10 * 5 =", result_mul)
    print("10 / 5 =", result_div)
