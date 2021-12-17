from sympy import *


def ex4():
    s,a,b=input().split(',')
    a=int(a)
    b=int(b)
    expr = sympify(s)
    x = symbols('x')
    res = integrate(expr, (x, a, b)) / (b - a)
    print(str(res))
    # print(str(res)=="3*a/4 + c + 7/6")
    return str(res)

if __name__ == '__main__':
    ex4()