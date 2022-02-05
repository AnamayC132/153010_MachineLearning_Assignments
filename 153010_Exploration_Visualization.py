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

df.head()
df.tail()


# In[3]:


# Size of the dataset
df.shape


# In[4]:


#Examining the column names and the datatypes
df.dtypes


# In[5]:


#Finding number of unique values in each column
df.nunique()


# In[6]:


# List all columns
df.columns


# In[7]:


#Statistical understanding about the numerical data
df.describe()


# In[8]:


#Find out how many individuals are graduate and non graduate
df.groupby(['Education']).size()


# In[9]:


#Randomly sampling 10 rows
df.sample(n=10)


# In[10]:


#Making a new column based on calcualtion of other columns in the df
df['Total Income'] = (df['ApplicantIncome'] + df['CoapplicantIncome'])
df.head()


# In[11]:


df[(df.Gender=='Male') & (df.Loan_Status=='Y')]


# In[ ]:




