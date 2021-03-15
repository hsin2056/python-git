import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.rand(5,3),\
        index=list("ABCDE"),columns=list("XYZ"))
print(df)
print("---------------------")
print(df.loc["A":"C","X":"Y"])
print("---------------------")
print(df.iloc[0,0])
print("---------------------")
print(df.iloc[:,0:1])
