import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("dataset.txt", names=["date","p1","p2"])
# print(df.head())

# print(df.date.value_counts())
df0=df[df.date=="2016-07-03"]
d=1
# print(df0.p1.shift(d))
print(df.groupby(['date']).diff())
# print(df0.p1.shift(d).diff(1))
# plt.plot(df0.p1.diff(1))
# plt.plot(df0.p2.diff(1))
# plt.show()