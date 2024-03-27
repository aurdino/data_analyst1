# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 18:23:22 2024

@author: VishalRajak
"""

import pandas as pd

data = {
     "Name" : ['Vishal', 'Chandan', 'Ravi','Darsh','Ravi'],
     "Age" : [26,30,28,6,30]
    }
df = pd.DataFrame(data) #data frame used for table
print(df,'\n')
filter = df['Age'] > 25
print(df[filter])

g = df.groupby('Name').agg(
        {
            "Age" : "mean"   
        }
    )

print('g', g)

print(g.index,'\n', df.index)
print(g.reset_index)
#remove duplicates 

print('uniq:', df.drop_duplicates().reset_index(drop=True))