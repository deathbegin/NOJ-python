#第一题
from sympy import *

def ex1():
    a, b, c = symbols("a,b,c")
    e = Eq(a ** 2 + b ** 2, c ** 2)
    print(str(e))
    return str(e)

if __name__ == '__main__':
    ex1()