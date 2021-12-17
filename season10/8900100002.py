#第三题8900090002
from sympy import *

def ex3():
    n = int(input())
    vars = symbols('x1:{}'.format(n+1))
    eqs = []
    for i in range(n):
        expr = sympify(input())
        value = sympify(input())
        eqs.append(Eq(expr, value))
    # print(eqs, vars)
    res = solve(eqs, vars)
    print(str(res))
    # print(str(res) == "[(-1/2 + sqrt(3)/2, c1 - 3*sqrt(3)/2 + 3/2, -c1 - 5/2 + 5*sqrt(3)/2), (-sqrt(3)/2 - 1/2, c1 + 3/2 + 3*sqrt(3)/2, -c1 - 5*sqrt(3)/2 - 5/2)]")
    return res

if __name__ == '__main__':
    ex3()