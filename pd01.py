import pandas as pd
ss= pd.Series([1,4,6,8,10])
print(ss)
print("--------")
print(8 in ss)
print("--------")
print(ss.index)
print("--------")
print(ss.values)
print("--------")
ss1= pd.Series([1,4,6,8,10],index=["a","b","c","d","e"])
print(ss1)
print("--------")
print(4 in ss1)
print("--------")
print("a" in ss1)
print("--------")
print(4 in ss1.values)





