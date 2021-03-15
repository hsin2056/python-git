import pandas as pd
df=pd.read_csv(r"C:\Users\user\Desktop\Python\Py\Sample\csvsample.csv")
print(df.ndim)
print("--------")
print(df.shape)
print("--------")
print(df.dtypes)
print("--------")

print(df.info())
df=df.sort_values("sno")
print(df[["sno","sna","tot"]].head(6))
print(df.head(6))


