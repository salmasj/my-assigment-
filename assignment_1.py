#!/usr/bin/env python
# coding: utf-8

# In[33]:


# Latihan 1 : Select Data

import matplotlib as plt
import pandas as pd
data_frame = pd.read_csv("C:/Programming Things/Data/medali.csv")

# Data 10 negara ranking pertama
print(data_frame[0:10])


# In[34]:


# Data nama negara rangking 11 s.d. 20
print(data_frame.loc[10:19, "country":"country"])


# In[35]:


# Data negara yang mendapatkan 1 medali emas
print(data_frame.loc[data_frame["gold"] == 1])


# In[36]:


# Data negara yang memperoleh medali keseluruhan > 20 dan perolehan medali emas < 5
print(data_frame.loc[(data_frame["total"] > 20) & (data_frame["gold"] < 5)])


# In[37]:


# Latihan 2 : Maximum and Minimum Value

# Data negara dengan perolehan perunggu terbanyak
max_bronze = data_frame["bronze"]. idxmax()
data_frame[max_bronze:max_bronze+1]


# In[38]:


# Data negara dengan perolehan perunggu paling sedikit namun total perolehan medali > 0

data_frame.loc[(data_frame["total"] > 0) & (data_frame["bronze"] == data_frame["bronze"].min())]


# In[39]:


# Latihan 3 : Sort

print(data_frame.sort_values(["gold", "silver"], ascending=[0, 1]))


# In[40]:


# Latihan 4 : Counting Frequency

data_frame["total"].value_counts()


# In[41]:


# Latihan 5 : Correlation

# Korelasi gold vs silver
data_frame["gold"].corr(data_frame["silver"])


# In[65]:


data_frame.plot(kind='scatter', x='gold', y='silver', color='blue')


# In[42]:


# Korelasi silver vs bronze
data_frame["silver"].corr(data_frame["bronze"])


# In[72]:


data_frame.plot(kind='scatter', x='silver', y='bronze', color='green')


# In[43]:


# Korelasi gold vs bronze
data_frame["gold"].corr(data_frame["bronze"])


# In[73]:


data_frame.plot(kind='scatter', x='gold', y='bronze', color='red')


# In[44]:


# Korelasi silver vs total
data_frame["silver"].corr(data_frame["total"])


# In[75]:


data_frame.plot(kind='scatter', x='silver', y='total', color='brown')


# In[45]:


# Korelasi bronze vs total
data_frame["bronze"].corr(data_frame["total"])


# In[77]:


data_frame.plot(kind='scatter', x='bronze', y='total', color='purple')


# In[25]:


# Korelasi Pearson
data = data_frame.corr()
data


# In[26]:


data_frame.corr().style.background_gradient(cmap='coolwarm')


# In[ ]:





# In[ ]:




