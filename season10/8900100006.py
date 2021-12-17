from sympy import *


def ex7():
    m,n=map(int,input().split(' '))
    listM = []
    for i in range(m):
        # t = sys.stdin.readline().strip()
        t = list(map(int,input().split(' ')))
        listM.append(t)
    # print(listM)
    # func=input()
    M = Matrix(listM)
    P, D = M.diagonalize()
    diags = [exp(D[i, i]) for i in range(M.shape[0])]
    res = P * diag(*diags) * P ** -1
    print(str(res))
    # print(str(res)=='Matrix([[-exp(-2) + 2*E, -2*exp(-2) + 2*E, 0], [-E + exp(-2), -E + 2*exp(-2), 0], [-E + exp(-2), -2*E + 2*exp(-2), E]])')
    return str(res)

if __name__ == '__main__':
    ex7()