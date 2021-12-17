from sympy import *


def ex8():
    n = int(input())
    vars = symbols('x1:{}'.format(n+1))
    expr = sympify(input())
    vals = list(map(int,input().split()))

    f = lambdify([vars], expr, "numpy")
    import numpy
    res = f(vals)
    print("%.2f" % res)
    return


if __name__ == '__main__':
    ex8()
