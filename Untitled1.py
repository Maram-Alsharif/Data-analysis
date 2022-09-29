#!/usr/bin/env python
# coding: utf-8

# In[711]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[790]:


df_MaccaRegion=pd.read_excel('C:\\Users\\maram\\OneDrive\\Desktop\\Macca - Riyadh regions.xlsx',sheet_name = 'Sheet2')
df_RiyadhRegion=pd.read_excel('C:\\Users\\maram\\OneDrive\\Desktop\\Macca - Riyadh regions.xlsx',sheet_name = 'Sheet3')
df_Gender=pd.read_excel('C:\\Users\\maram\\OneDrive\\Desktop\\Macca - Riyadh regions.xlsx',sheet_name = 'Sheet1')


# In[713]:


df_RiyadhRegion


# In[714]:


df_MaccaRegion['Sport']


# In[715]:


import matplotlib as mpl
mpl.get_backend()


# In[716]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('pinfo', 'plt.plot')


# In[801]:


import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure()
fig.set_size_inches(9, 4)
plt.bar(df_MaccaRegion['Sport'], df_MaccaRegion['Favorite sport'], 0.4, label = 'Macca')
plt.xlabel("People's Favorite Sport")
plt.ylabel("Rate")
plt.title("Relative distribution of individuals who engage in sports activity at the level of Macca Region")
plt.legend()
  
plt.show()


# In[799]:


fig = plt.figure()
fig.set_size_inches(9, 5)
plt.bar(df_RiyadhRegion['Sport'], df_RiyadhRegion['Favorite sport'], 0.4, label = 'Riyadh')
plt.xlabel("People's Favorite Sport")
plt.ylabel("Rate")
plt.title("Relative distribution of individuals who engage in sports activity at the level of Riyadh Region")
plt.legend()
plt.show()


# In[791]:


df_Gender


# In[778]:





# In[795]:


fig = plt.figure()
fig.set_size_inches(8.4, 2.5)
plt.bar(df_Gender['Region '], df_Gender['Women '], 0.4, label = 'Women')
plt.xlabel("Region ")
plt.ylabel("Rate")
plt.title("The number of women practicing sports in the Makkah - Riyadh region")
plt.legend()
plt.show()


# In[796]:


fig = plt.figure()
fig.set_size_inches(8.4, 2.5)
plt.bar(df_Gender['Region '], df_Gender['Men'], 0.4, label = 'Men')
plt.xlabel("Region ")
plt.ylabel("Rate")
plt.title("The number of women practicing sports in the Makkah - Riyadh region")
plt.legend()
plt.show()


# In[ ]:




