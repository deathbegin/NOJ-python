from sympy import *
#第二题
def ex2():
    s = input()
    x = symbols('x')
    e = sympify(s)
    p = collect(expand(e), x, evaluate=False)
    # print(p)
    list = []
    for value in p.values():
        list.append(str(value))
    print(list)
    # print(list==['a**3', '3*a**2 + b**2', '3*a + 2*b', '2'])
    return list

if __name__ == '__main__':
    ex2()