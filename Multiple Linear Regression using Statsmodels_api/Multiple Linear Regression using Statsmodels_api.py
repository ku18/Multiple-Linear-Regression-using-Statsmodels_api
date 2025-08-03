#!/usr/bin/env python
# coding: utf-8

# In[8]:


# Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn
seaborn.set()

# Load Data
data = pd.read_csv('1.02. Multiple linear regression.csv')
data.describe
y = data ['GPA']
x1 = data [['SAT','Rand 1,2,3']]

#Create Multiple linear regression model using statsmodel
x = sm.add_constant(x1)
results = sm.OLS(y,x).fit()

#find summary
results.summary()


# In[ ]:




