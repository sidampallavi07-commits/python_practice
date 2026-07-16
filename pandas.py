import pandas as pd

# pandas aggregate function and group by used


# aggregate function
df=pd.read_csv("data7.csv")

#whole dataframe

#print(df.mean(numeric_only=True))
#print(df.sum(numeric_only = True))
#print(df.min(numeric_only=True))
#print(df.max(numeric_only=True))
#print(df.count(numeric_only=True))


# single column

#print(df["year"].mean())
#print(df["year"].sum())
#print(df["year"].count())
#print(df["year"].max())
#print(df["year"].min())

# group by function used

group= df.groupby("variable")
#print(group["unit"].sum())
#print(group["unit"].max())
#print(group["unit"].count())
print(group["unit"].min())