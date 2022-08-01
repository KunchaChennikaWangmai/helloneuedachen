#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

df_SPX = pd.read_csv('https://s3.eu-west-1.amazonaws.com/neueda.conygre.com/pydata/SPX.csv',
                     index_col='Date', parse_dates=True)


# In[2]:


df_SPX.info()


# In[4]:


df_SPX.head()
df_SPX['Price'] = pd.to_numeric(df_SPX['Price'].str.replace(',',''))
df_SPX['Open'] = pd.to_numeric(df_SPX['Open'].str.replace(',',''))
df_SPX['High'] = pd.to_numeric(df_SPX['High'].str.replace(',',''))
df_SPX['Low'] = pd.to_numeric(df_SPX['Low'].str.replace(',',''))
df_SPX['Change %'] = pd.to_numeric(df_SPX['Change %'].str.replace('%',''))


# In[7]:


df_SPX.sort_values(by=['Date'])


# In[15]:


cols = ['High','Low']
rows = "'2015-06-01'<=Date and Date<='2016-06-30'"
df1 = df_SPX[cols].sort_index().query("Date >= 2015 and Date < 2017")[['High','Low']]
df1.plot(figsize=(18,9))
#df_SPX(rows)[cols]


# In[17]:


byMonth = pd.Grouper(freq='BM')
funcs = ['max','min', 'mean']
df2 = df_SPX.agg(funcs)
df2


# In[20]:


import matplotlib.pyplot as plt
x = df_SPX.index
plt.scatter(x, df_SPX['Open'])
plt.scatter(x, df_SPX['Change %'])
plt.show()


# In[ ]:




