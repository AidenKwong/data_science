import pandas as pd
import matplotlib.pyplot as plt

fig_size = (16, 9)

df = pd.read_csv("./dataset/sales_data.csv", parse_dates=["Date"])

# print(df.shape)
# print(df.columns)
# print(df.info())
# print(df.describe())
# print(df["Unit_Cost"].describe())

## Plot ##

# df["Unit_Cost"].plot(kind="box", vert=False, figsize=(16, 9))

# ax = df["Unit_Cost"].plot(kind="density", figsize=(16, 9))
# ax.axvline(df["Unit_Cost"].mean(), color="tab:red")
# ax.axvline(df["Unit_Cost"].median(), color="tab:green")

# ax = df["Unit_Cost"].plot(kind="hist", figsize=fig_size)
# ax.set_ylabel("Number of Sales")
# ax.set_xlabel("dollars")

# print(df["Age_Group"].value_counts())
# ax = df["Age_Group"].value_counts().plot(kind="pie", figsize=(9, 9))

# print(df.corr())


## Correlation ##
corr = df.corr()
fig = plt.figure(figsize=(9, 9))
plt.matshow(corr, fignum=fig.number, cmap="RdBu")
plt.xticks(range(len(corr.columns)), corr.columns, rotation=-45)
plt.yticks(range(len(corr.columns)), corr.columns)
plt.colorbar()

# df.plot(kind="scatter",x="")
plt.show()
