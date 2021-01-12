#!/usr/bin/env python
# coding: utf-8

# In[7]:


import urllib
import ssl

context = ssl._create_unverified_context()

url = 'https://api.hkma.gov.hk/public/market-data-and-statistics/daily-monetary-statistics/daily-figures-monetary-base?offset=0'

with urllib.request.urlopen(url, context=context) as req:
    print (req.read())


# In[10]:


with urllib.request.urlopen(url, context=context) as f:
    print(f.read())


# In[12]:


datasets = json.loads(f)

# but isn't it as json file?


# In[15]:


import urllib, json

url = "https://api.hkma.gov.hk/public/market-data-and-statistics/daily-monetary-statistics/daily-figures-monetary-base?offset=0"

response = urllib.request.urlopen(url, context=context)

data = json.loads(response.read())

print(data)


# In[16]:


dataset = json.dumps(data, indent=2)
print(dataset)


# In[21]:


#json dumps creates a string; the json data is still in the data variable
for item in data['result']['records']:
    print(item)


# In[34]:


for item in data['result']['records']:
    Date = item['end_of_date']
    cert_of_indebt = item['cert_of_indebt']
    gov_notes_coins = item['gov_notes_coins_circulation'] 
    aggr_balance_bf_disc_win = item['aggr_balance_bf_disc_win']
    aggr_balance_af_disc_win = item['aggr_balance_af_disc_win']
    outstanding_efbn = item['outstanding_efbn']
    ow_lb_bf_disc_win = item['ow_lb_bf_disc_win']
    mb_bf_disc_win_total = item['mb_bf_disc_win_total']
    print(Date, cert_of_indebt, gov_notes_coins, aggr_balance_bf_disc_win)    


# In[66]:


import pandas as pd

pd_response = urllib.request.urlopen(url, context=context)


# In[67]:


df = pd.read_json(pd_response)

df

#doesn't work for multiple level json:


# In[65]:


#so how to use muliple level json

from pandas.io.json import json_normalize

import urllib, json

url = "https://api.hkma.gov.hk/public/market-data-and-statistics/daily-monetary-statistics/daily-figures-monetary-base?offset=0"

response = urllib.request.urlopen(url, context=context)

nycphil = json_normalize(response['end_of_date'])


# In[71]:


file = "/Users/paul/Documents/DATA/daily-figures-monetary-base.json"


# In[74]:


pd.read_json(file)


# In[78]:





multiple_level_data = pd.json_normalize(dataset, record_path =['results'])




# In[ ]:




