#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing required packages
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
pd.options.display.max_columns =None
pd.options.display.max_rows =None


# In[2]:


#loading the data
df  = pd.read_csv("E:\Work & Study\MBA\T3\MLP\My works\Datasets\loan_approval_pred.csv")

df.head()
df.tail()


# In[3]:


## DATA PRE-PROCESSING

#Finding out missing values in each column
print(df.isna().sum())
missing_status=df.isna().sum()
##print(df.isnull().sum())


# In[4]:


##Handling the missing data with mean value
df = df.fillna(0)
print(df.head())


# In[5]:


print(df.isna().sum())


# In[6]:


#FInding rows that have duplicate values
df[df.duplicated(keep = 'last')] 


# In[ ]:




