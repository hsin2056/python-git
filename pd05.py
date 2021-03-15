import pandas as pd
df=pd.read_csv(r"C:\Users\user\Desktop\Python\Py\Sample\nba.csv")
print(df)
print(df.sort_values("Age").head(6))
print("---------------------")
print(df.sort_values("Age",ascending=False).head(6))
print("---------------------")
#print(df[df["Age"] >= 20].head(6)) 
#mask=df["Age"] >= 20
#print(df[mask].head(6))    
#print(df[df["Age"].between(20,28)].head(6))     
mask1=df["Age"].between(20,28)
print(df[mask1].head(8))
mask2=df["Age"].isin([20,25,28])
print(df[mask2].head(8))



