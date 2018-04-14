import pandas as pd
import numpy as np

s = pd.Series([1,3,5,np.nan, 6,8])
print(s[0:3])

s = pd.Series([1,3,5,np.nan,6,8] , index=['a','b','c','h','g','f'])
print(s['c'])
