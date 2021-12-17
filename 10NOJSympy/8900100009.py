from sympy import *


def ex10():
    x = symbols('x')  # x, c2, c1, c0, a, b = symbols('x,c2,c1,c0,a,b')
    p = sympify(input())  # p = c2*x**2+c1*x+c0
    if (Poly(p).degree() != 2):
        print("ERROR")
        return
    a, b = input().split()
    a, b = symbols('{} {}'.format(a, b)) #改动在和一行
    # a, b = sympify([a,b])
    na, nb = [p.subs(x, x0) for x0 in [a, b]]
    ma, mb = [p.diff(x).subs(x, x0) for x0 in [a, b]]
    la = ma*(x-a)+na
    lb = mb*(x-b)+nb
    x1 = solve((la-lb), x)
    area_a = integrate(p - la, (x, a, x1))
    area_b = integrate(p - lb, (x, x1, b))
    # x1 = [sympify(str(t)) for t in x1]  #所谓化简处理
    print(str(x1))  # 两切线交点
    # print(x1==[a/2+b/2])           #两切线交点
    print(str(simplify(area_a-area_b)))
    # print(simplify(area_a-area_b)==0)


if __name__ == '__main__':
    ex10()
