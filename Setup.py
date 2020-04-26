#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
agents = pd.read_csv('agents_test.csv')
from ast import literal_eval
from sklearn import preprocessing
import numpy as np
from sklearn import tree,ensemble
from sklearn.tree import DecisionTreeClassifier
import pickle
from sklearn.externals import joblib
ogdf = agents
ogdf


# In[107]:


df = agents
agents.columns


# In[114]:


#def prediction(x1,x2,df = agents):
encoder = preprocessing.LabelEncoder()
for i in df.columns:
    if isinstance(df[i][0], str):
        df[i] = encoder.fit_transform(df[i])
conditions = df.drop(['Name','Agent Number','S.No','Phone No.','Ratings','Companies'], axis = 1)
details = df.drop(['Name','Service Provided','S.No','Phone No.','Ratings','Companies','Area'], axis = 1)
model = DecisionTreeClassifier()
X = conditions
y = details
model.fit(X, y)
model.score(X, y)
#Predict Output
# predicted= model.predict([])
# predicted = int(predicted)
value = df[df['Agent Number']==predicted]


# def original(predicted,df = pd.read_csv('agents_test.csv')):
#     value = df[df['Agent Number']==predicted]
#     value = value.to_dict('list')
#     return value


# In[115]:


# Save the model
model_filename = 'finad.pkl'
print("Saving model to {}...".format(model_filename))
joblib.dump(model, model_filename)


# In[116]:


#for the first parameter
# 3  is for south Delhi , 4 is for west delhi , 0 for central delhi,1 is for east delhi, 2 for north delhi
#for the second parameter 
# 1 and 4 for Insurance and Investment and 0 for insurance and 3 for investment 
#This will be the input fromthe appwhere the user will enter is area from('Parts of Delhi': South, North, East, West and central)
# pred = prediction(0,0)
# original(pred)
# og


# 

# In[117]:


# def main():
#     print('0 for Central Delhi,1 is for East Delhi, 2 for North Delhi,3  is for South Delhi , 4 is for West Delhi ')
#     area = int(input('Enter the area : '))
#     print('1 and 4 for Insurance or Investment and 0 for Insurance and 3 for Investment')
#     need = int(input('Enter the need : '))
#     pred = prediction(area,need)
#     og = original(pred)
#     return og
    


# In[118]:


main()


# In[119]:


#url = ""


# In[ ]:




