#第九题
from sympy import *


def ex9():
    m,n=map(int,input().split(' '))
    listM = []
    for i in range(m):
        t = list(map(int,input().split(' ')))
        listM.append(t)
    # print(listM)
    s = int(input()) #余项的幂次数
    M = Matrix(listM)
    x=symbols('x')
    P, D = M.diagonalize()
    diags = [exp(D[i, i]).series(x, 0, 10).removeO() for i in range(M.shape[0])]
    res = P * diag(*diags) * P ** -1
    res = res.evalf(5)
    print(str(res))
    # print(str(res)=="Matrix([[5.3012, 5.1659, 0], [-2.5829, -2.4476, 0], [-2.5829, -5.1659, 2.7183]])")
    
    # print(M.exp().evalf(5))
    # print(res==M.exp().evalf(5))
    
    return str(res)


if __name__ == '__main__':
    ex9()