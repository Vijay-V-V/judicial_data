#!/usr/bin/env python
# coding: utf-8

# In[10]:


# chunking
# due to the large size of the dataset, we split it into pieces to make it easier to analyze.
# here chunksize is given as 50000, meaning we create new datasets, each containing max of 50000 rows, split from the original dataset
import pandas as pd
for i,chunk in enumerate(pd.read_csv(r"C:\Users\Vijay\Downloads\Precog task\csv\cases\cases\cases_2010.csv", chunksize=50000)):
    chunk.to_csv('chunk{}.csv'.format(i), index=False)

