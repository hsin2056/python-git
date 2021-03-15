import pandas as pd
df=pd.read_csv(r"C:\Users\user\Desktop\Python\Py\Sample\nba.csv")
foss=df.groupby("Age")
print(foss.groups)
print(foss.get_group(40))
