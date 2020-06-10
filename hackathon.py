#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os


# In[7]:


df = pd.read_csv(r"C:\Users\Admin\Downloads\Hackathon_Data_May6.csv")
df


# In[8]:


df.replace(np.nan,0)


# In[9]:



df['MRP'] = df['MRP'].round(0).astype(int)
df.head(29)


# In[10]:


df.dtypes


# In[11]:


df.describe()


# # Warehouse Planning
# 

# In[12]:


df['Site Id'].describe()
#DELMDK Has the most no of site.


# In[13]:


df.groupby('Pack Size')['ParentSKU'].count()

#pack size in per unit parent sku where size of 190,192 requires 1 parentsku and size of 1,50,30,700 requires large no of parentsku.


# In[14]:


df.groupby('Site Id')['ParentSKU'].count()
#city like ahmedabad, banglore ,mumbai has highest no of Parentsku while 
#kolkata,,hrdfactory,gurgaon requires more no of parentsku


# In[46]:


import numpy as np
import matplotlib.pyplot as plt

Parentsku=[63,1561,1595,1425,1576,1363,1607,1587,541,1492,615,1529,1482,1519,1557,1577,1592,1600,1490,1589,1485,1485,1562,1539]
Site_Id=('AHMEDABAD','BANGALORE','BHUBANESWR','CHENNAI','DEHRADUN','DELMDK' ,'GHAZIABAD','GURGAON','GUWAHATI','HRDFACTORY','INDORE' ,'JAIPUR','JAMMU','KOCHI','KOLKATA2','KOLKATA','MUMBAI'  )
y_pos = np.arange(len(Parentsku))
plt.bar(y_pos, Parentsku)
plt.xticks(y_pos, Site_Id,rotation=90)
plt.xlabel('Site_Id')
plt.ylabel('Parentsku')
plt.title('parentsku city wise')
plt.ylim(0,2000)
plt.xlim(15,0)
plt.subplots_adjust(bottom=0.4, top=0.99)

plt.show()


# # Demand Planning.

# In[101]:


#yearwise net profit.
df.groupby('Year')['Net Sales calculated'].sum()


# In[105]:


#monthly profit
df.groupby(['Net Sales calculated','Year'])['Month'].sum()


# In[114]:


# How many Quantity of per product that has been bought every year in each site?
a=df.groupby(['Year', 'Site Id'])['Pack Size'].sum()


# In[100]:


#zone wise net sales
df.groupby(['Year', 'Net Sales calculated'])['Zone'].sum()


# In[112]:


#yearwise demand of product size and quanitity.
df.groupby(['Size', 'Year'])['Qty'].count()


# In[ ]:


names='100g', '100gm', 'groupC', 'groupD',
size=[12,11,3,30]


# # Pricing of Product

# In[149]:


#no of cash discount offered yearwise.
df.groupby(['Year'])['Cash Discount'].sum()


# In[139]:


#cash discount given in product and quanity wise yearly
df.groupby(['Pack Size','Pack Unit Id','Year'])['Cash Discount'].sum()


# In[171]:


#rate of change of price per quanitity
df.groupby('Qty')['Price'].sum().pct_change()


# In[168]:


#rate od chnage of MRP year wise
df.groupby(['Price','Year'])['MRP'].sum().pct_change()


# In[176]:


df.groupby(['Year'])['MRP'].sum().pct_change()


# In[178]:


Year = [2017,2018,2019,2020]
bars = (a)
y_pos = np.arange(len(bars))
plt.bar(y_pos, Year,)
plt.xticks(y_pos, bars)
plt.show()


# # conclusion.
# 

# # if we increase the number of warehouse in cities like Gurgaon and also increase the discount where demand is less then the sales will get increase.

# In[ ]:




