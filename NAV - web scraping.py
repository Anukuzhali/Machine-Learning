#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import pandas as pd


# In[2]:


base_url='https://api.mfapi.in/mf'


# In[3]:


r=requests.get(base_url)


# In[4]:


x=r.json()


# In[5]:


len(x)


# In[9]:


extension=[]
for i in range(0,10000):
    extension.append(str(r.json()[i]['schemeCode']))


# In[7]:


note_urls=[]
for i in extension:
    note_urls.append('https://api.mfapi.in/mf/'+i)


# In[8]:


import json


# In[10]:


par_text=[]
for url in note_urls:
    note_resp = requests.get(url)
    par_text.append(note_resp.json())


# In[11]:


sample_list = pd.json_normalize(
    par_text, 
    record_path =['data'], 
    meta=[['meta','fund_house'],['meta','scheme_type'],['meta','scheme_code'],['meta','scheme_name'],['meta','scheme_category']],errors='ignore')


# In[14]:


extension1=[]
for i in range(10000,20001):
    extension1.append(str(r.json()[i]['schemeCode']))


# In[15]:


note_urls1=[]
for i in extension1:
    note_urls1.append('https://api.mfapi.in/mf/'+i)


# In[16]:


par_text1=[]
for url in note_urls1:
    note_resp1 = requests.get(url)
    par_text1.append(note_resp1.json())


# In[17]:


sample_list1 = pd.json_normalize(
    par_text1, 
    record_path =['data'], 
    meta=[['meta','fund_house'],['meta','scheme_type'],['meta','scheme_code'],['meta','scheme_name'],['meta','scheme_category']],errors='ignore')


# In[21]:


sample_list.tail()


# In[23]:


nav_list1=sample_list[:1000001]


# In[25]:


nav_list2=sample_list[1000001:2000001]


# In[27]:


nav_list3=sample_list[2000001:3000001]


# In[28]:


nav_list4=sample_list[3000001:]


# In[30]:


sample_list1.tail()


# In[31]:


nav_list1.to_csv('samp_nav1.csv')


# In[32]:


nav_list2.to_csv('samp_nav2.csv')


# In[33]:


nav_list3.to_csv('samp_nav3.csv')


# In[34]:


nav_list4.to_csv('samp_nav4.csv')


# In[35]:


nav_list5=sample_list1[:1000001]


# In[36]:


nav_list6=sample_list1[1000001:2000001]


# In[37]:


nav_list7=sample_list1[2000001:3000001]


# In[38]:


nav_list8=sample_list1[3000001:4000001]


# In[39]:


nav_list9=sample_list1[4000001:5000001]


# In[40]:


nav_list10=sample_list1[5000001:6000001]


# In[41]:


nav_list11=sample_list1[6000001:7000001]


# In[42]:


nav_list12=sample_list1[7000001:8000001]


# In[43]:


nav_list13=sample_list1[8000001:9000001]


# In[44]:


nav_list14=sample_list1[9000001:10000001]


# In[45]:


nav_list15=sample_list1[10000001:]


# In[46]:


nav_list5.to_csv('samp_nav5.csv')


# In[47]:


nav_list6.to_csv('samp_nav6.csv')


# In[48]:


nav_list7.to_csv('samp_nav7.csv')


# In[49]:


nav_list8.to_csv('samp_nav8.csv')


# In[50]:


nav_list9.to_csv('samp_nav9.csv')


# In[51]:


nav_list10.to_csv('samp_nav10.csv')


# In[52]:


nav_list11.to_csv('samp_nav11.csv')


# In[53]:


nav_list12.to_csv('samp_nav12.csv')


# In[54]:


nav_list13.to_csv('samp_nav13.csv')


# In[55]:


nav_list14.to_csv('samp_nav14.csv')


# In[56]:


nav_list15.to_csv('samp_nav15.csv')


# In[ ]:




