import pandas as pd
data={"name":["Jack","Mary"],"year":[1986,1997],"moth":[8,1],"day":[20,31]}
df=pd.DataFrame(data)
print(df)
print("--------")
df1=pd.DataFrame(data,columns=["name","day","moth","year","ABC"],index=["a","b"])
print(df1)
