#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


dataset = pd.read_csv("covid19_Confirmed_dataset.csv")
dataset.head()


# In[3]:


dataset.shape


# In[4]:


df = dataset.drop(["Lat","Long"], axis = 1, inplace = True)


# In[5]:


dataset.head()


# In[24]:


corona_dataset_aggregated = dataset.groupby("Country/Region").sum(numeric_only=True)


# In[25]:


corona_dataset_aggregated.head()


# In[26]:


corona_dataset_aggregated.shape


# In[27]:


corona_dataset_aggregated.loc["China"]


# In[28]:


corona_dataset_aggregated.loc["India"].plot()
corona_dataset_aggregated.loc["Japan"].plot()
corona_dataset_aggregated.loc["Spain"].plot()
plt.legend()


# In[29]:


corona_dataset_aggregated.loc["Japan"][:3].plot()


# In[30]:


corona_dataset_aggregated.loc["Japan"].diff().plot()


# In[31]:


corona_dataset_aggregated.loc["India"].diff().max()


# In[32]:


corona_dataset_aggregated.loc["Japan"].diff().max()


# In[33]:


corona_dataset_aggregated.loc["Spain"].diff().max()


# In[34]:


countries = list(corona_dataset_aggregated.index)
max_infection_rates = []

for c in countries:
    max_infection_rates.append(corona_dataset_aggregated.loc[c].diff().max())
corona_dataset_aggregated["Max_infection_rates"] = max_infection_rates


# In[35]:


corona_dataset_aggregated


# In[36]:


corona_data = pd.DataFrame(corona_dataset_aggregated["Max_infection_rates"])


# In[37]:


corona_data


# In[39]:


happiness_report = pd.read_csv("worldwide_happiness_report.csv")
happiness_report


# In[45]:


useless_cols =["Overall rank", "Score", "Generosity", "Perceptions of corruption"]


# In[46]:


happiness_report.drop(useless_cols, axis= 1, inplace= True)
happiness_report.head()


# In[47]:


happiness_report.set_index("Country or region", inplace= True)
happiness_report.head()


# In[48]:


corona_data.shape


# In[49]:


happiness_report.shape


# In[50]:


data = corona_data.join(happiness_report, how= "inner")
data


# In[51]:


data.corr()


# In[52]:


data


# In[55]:


x=data["GDP per capita"]
y=data["Max_infection_rates"]
sns.scatterplot(x,np.log(y))


# In[56]:


sns.regplot(x,np.log(y))


# In[58]:


x=data["Social support"]
y=data["Max_infection_rates"]
sns.scatterplot(x,np.log(y))


# In[59]:


sns.regplot(x,np.log(y))


# In[61]:


x=data["Healthy life expectancy"]
y=data["Max_infection_rates"]
sns.scatterplot(x,np.log(y))


# In[62]:


sns.regplot(x,np.log(y))


# In[64]:


x=data["Freedom to make life choices"]
y=data["Max_infection_rates"]
sns.scatterplot(x,np.log(y))


# In[65]:


sns.regplot(x,np.log(y))


# In[ ]:




