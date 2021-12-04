# T075, s8-5
import pandas as pd

n = int(input())
table = []
for i in range(5*n):
    t = list(input().split())
    table.append(t)
df = pd.DataFrame(table, columns=["Mon", "Part", "Num", "Price"])
print(df)

df_new = pd.pivot_table(df, index=["Mon", "Part"]).T
print(df_new)
