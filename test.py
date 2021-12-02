#T072, s8-2
import pandas as pd


def Op(x, y, op):
    if("plus" == op):
        return x*y
    elif("power" == op):
        return x**y
    elif("minux" == op):
        return x-y
    elif("divide" == op):
        if(0 == y):
            return "ERROR"
        return x/y
    elif("mutiply" == op):
        return x*y


n = int(input())
table = []
for i in range(n):
    t = list(input().split())
    table.append(t)
# print(table)

df = pd.DataFrame(table, columns=['Num1', 'Num2', 'Op'])
print(df)
df["result"] = df.apply(lambda x: Op(
    x['Num1'], x['Num2', x['Op']]), axis=1)
