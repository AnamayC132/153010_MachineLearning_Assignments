#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing required packages
import numpy as np
import pandas as pd

pd.options.display.max_columns =None
pd.options.display.max_rows =None


# In[2]:


#loading the data
df  = pd.read_csv("E:\Work & Study\MBA\T3\MLP\My works\Datasets\loan_approval_pred.csv")

train  = df
test = df
train.head()
test.head()


# In[3]:


#Checking the proportion of Loan_Status variable values. 
train.Loan_Status.value_counts()/train.shape[0]


# In[4]:


#Rough guess of finding out if education has an influnce on Loan_Status variable
(pd.crosstab(train.Education, train.Loan_Status,margins=True)/train.shape[0]*100).round(2)


# In[ ]:




