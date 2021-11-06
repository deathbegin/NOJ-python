a = int(input())
b = int(input())
c = input()
if ('+' == c):
    d = a+b
elif ('-' == c):
    d = a-b
elif ('*' == c):
    d = a*b
elif ('/' == c):
    d = a/b
elif ('//' == c):
    d = a//b
elif ('%' == c):
    d = a % b
elif ('**' == c):
    d = a**b
else:
    d = False
# ops = {'+': operator.add,
#        '-': operator.sub,
#        '*': operator.mul,
#        '/': operator.truediv,
#        '//': operator.floordiv,
#        '%': operator.mod,
#        '**': operator.pow}
if (d == False):
    print("ERROR")
else:
    print('{}{}{}{}{}'.format(a, c, b, "=", d))