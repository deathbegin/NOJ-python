# T080, s8-10
import pandas as pd
import numpy as np

table = []
for i in range(9):
    t = list(input().split())
    table.append(t)
df = pd.DataFrame(table, columns=["Mon", "Group", "Sales"])
df[["Mon", "Sales"]] = df[["Mon", "Sales"]].astype(np.int64)

df_group = df.groupby(["Group"])["Sales"].sum()
print(df_group)
df_Mon = df.groupby(["Mon"])["Sales"].sum()
print(df_Mon)
