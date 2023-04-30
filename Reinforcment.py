#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as nm
import pandas as pd

df = pd.read_csv('trading.csv')
df.head()


# In[5]:


rebalance_window = 63
validation_window = 63


# In[6]:


unique_trade_date = df[(df.datadate > 20151001)&(df.datadate <= 20200707)].datadate.unique()
print(unique_trade_date)

