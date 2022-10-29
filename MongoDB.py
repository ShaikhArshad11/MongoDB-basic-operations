#!/usr/bin/env python
# coding: utf-8

# In[34]:


import pymongo
client = pymongo.MongoClient("mongodb+srv://shaikh121arshad:@cluster0.ybrpao3.mongodb.net/?retryWrites=true&w=majority")
db = client.test


# In[35]:


print(db)


# In[7]:


db2 = client['hello']


# In[8]:


client.list_database_names()


# In[9]:


coll1 = db2['ineuron_collection']


# In[8]:


dict1 = {
    "name" : "arshad",
    "email" : "shaikg121@gmail.com",
    "product" : ["pencil", "pen", "oil"],
    "company" : "Ineuron"
}


# In[9]:


coll1.insert_one(dict1)


# In[15]:


dict3 = {
    "_id" : "hello_world",
    "name" : "arshad",
    "email" : "shaikg121@gmail.com",
    "product" : ["pencil", "pen", "oil"],
    "company" : "Ineuron",
    "mob_no" : 45698712
}


# In[16]:


coll1.insert_one(dict3)


# In[36]:


list2 = [
    {"name" : "dfgeg",
     "email" : "shaikg121@gmail.com",
     "product" : ["pencil", "pen", "oil"],
     "company" : "Ineuron"},
    
    {"name" : "shaikh",
     "email" : "shaikg121@gmail.com",
     "product" : ["pencil", "pen", "oil"],
     "company" : "Ineuron",
     "mob_no" : 45698712}
]


# In[38]:


coll1.insert_many(list2)


# In[41]:


coll1.find()


# In[45]:


for i in coll1.find():
    print(i)


# In[48]:


for i in coll1.find({"name":"arshad"}) :
    print(i)


# In[51]:


for i in coll1.find({"name":{"$in":["arshad","shaikh"]}}): # $in command to help me out
    print(i)


# In[56]:


coll1.find_one()


# In[10]:


for i in coll1.find({"qty":{"$gt":25}}): # $gt means grater than 
    print(i)


# In[61]:


for i in coll1.find({"qty":{"$lt":25}}): # $lt means lesser than 
    print(i)

$gt is grater than
$gte is greater than equal to
$lt is lesser than
$lte is lesser than equal to
# In[13]:


for i in coll1.find():
    print(i)


# In[16]:


coll1.update_many({"name": "arshad"},{"$set":{"name": "arsh"}})


# In[19]:


for i in coll1.find().limit(2): # limit function will limit number of records to be shown
    print(i)


# In[22]:


for i in coll1.find({'qty': {"$not":{"$gte": 30}}}):
    print(i)


# In[28]:


coll1.find_one_and_update({"product" : "pen"}, {"$set" : {"name" : "Hello"}})


# In[29]:


for i in coll1.find():
    print(i)


# In[31]:


coll1.find_one_and_update({"qty" : {"$gte" : 30}}, {"$set" : {"qty" : 100}})


# In[32]:


coll1.delete_many({"name":"dfgeg"})


# In[33]:


for i in coll1.find():
    print(i)


# In[ ]:





# In[ ]:





# In[ ]:




