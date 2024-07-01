#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import Libraries 
import pandas as pd
import numpy as num
import matplotlib as plot
import seaborn as sea


# In[18]:


#download csv on notebook
df_big_tech_companies = pd.read_csv(r"big_tech_companies.csv")


# In[21]:


df_big_tech_companies.shape


# In[22]:


df_big_tech_stock_prices = pd.read_csv(r"big_tech_stock_prices.csv")


# In[23]:


df_big_tech_stock_prices.shape


# In[24]:


df_big_tech_stock_prices.info


# In[28]:


#top 5 rows displayed 
df_big_tech_stock_prices.head


# In[29]:


df_big_tech_stock_prices.columns.tolist()


# In[34]:


#checking date range for the data by using min and max functions 
min_date = df_big_tech_stock_prices['date'].min()
max_date = df_big_tech_stock_prices['date'].max()

print("Minimum date:", min_date)
print("Maximum date:", max_date)


# In[ ]:




