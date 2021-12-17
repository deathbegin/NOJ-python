from sympy import *


def ex6():
    s,x=input().split(' ')
    x = symbols(x)
    expr = sympify(s)
    f = symbols('f', cls=Function)
    res = dsolve(expr, f(x))
    print(str(res))
    # print(str(res)=="Eq(f(x), (C1 + C2*x)*exp(x) + cos(x)/2)")
    return str(res)

if __name__ == '__main__':
    ex6()