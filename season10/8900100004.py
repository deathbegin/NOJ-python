from sympy import *
#lhopital

def getInput():
    s,x,x0=input().split(',')
    x=symbols(x)
    ex5(s,x,x0)


def ex5(s, x, x0):
    expr = sympify(s)
    expr = cancel(expr)
    expr_num, expr_den = fraction(expr)
    expr_num_eval, expr_den_eval = expr_num.subs(x, x0), expr_den.subs(x, x0)
    indeterminates = [(0, 0), (oo, oo), (-oo, oo), (oo, -oo), (-oo, -oo)]
    if (expr_num_eval, expr_den_eval) in indeterminates:
        return ex5(expr_num.diff(x) / expr_den.diff(x), x, x0)
    print(str(expr_num_eval / expr_den_eval))
    # print(str(expr_num_eval / expr_den_eval)=="oo")
    return str(expr_num_eval / expr_den_eval)

if __name__ == '__main__':
    getInput()