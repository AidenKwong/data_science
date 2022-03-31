from sys import flags
from matplotlib.pyplot import flag
import pandas as pd
import re

df = pd.read_csv("./dataset/Pokemon.csv")

# print(df)
# print(df.columns)
# print(df[["Name","Type 1","HP"]])
# print(df.iloc[2:6])
# print(df.iloc[2,3])

# print(df["Attack"].describe())
# print(df.sort_values("Attack",ascending=False)[["Name","Attack"]])
# print(df.sort_values(["Type 1","HP"],ascending=[1,0])[["Name","Type 1","HP"]])

# df["Attact Sum"] = df["Attack"]+df["Sp. Atk"]
# print(df[["Name","Attact Sum"]])

# df.to_csv("modified.csv",index=False)


# Filtering Data
# print(df.loc[df["Type 1"]=="Fire"])
# new_df = df.loc[
#     (df["Type 1"] == "Grass") & (df["Type 2"] == "Poison") & (df["HP"] > 70)
# ]
# new_df = new_df.reset_index(drop=True)
# print(df.loc[~df["Name"].str.contains("Mega")])
# print(df.loc[df["Type 1"].str.contains("fire|Grass", flags=re.I, regex=True)])


# Groupby

print(df.groupby(["Type 1"]).mean().sort_values("Defense", ascending=False))


# for index , row in df.iterrows():
#     print(index,row["Name"])
