#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[24]:


df = pd.read_csv("C:/Users/prash/Downloads/abc/youtubers_df.csv")


# # Data Exploration

# In[164]:


df.shape        


# In[167]:


df_as_string = df.to_string(index=False)

print(df_as_string)


# In[166]:


df.head()


# In[29]:


df.info()


# In[33]:


df.columns


# In[40]:


df.describe()


# #  Data Cleaning

# In[41]:


df.isnull().sum()          # calculate null values


# In[46]:


df.dropna(inplace = True)          # drop null values from original data set using inplace=true


# In[47]:


df.shape                # again check dataset


# # Data Analysis

# In[56]:


#  1. most popular category among you tube streamer

popular_category = df["Categories"].value_counts()
print(popular_category)


# In[60]:


top_5_category= popular_category.head(5)
print (top_5_category)


# In[93]:


plt.figure(figsize=(5,3))
top_5_category.plot(kind='bar')
plt.title('top_category')
plt.xlabel('category')
plt.ylabel('youtube streamers')
plt.show()


# # Top 5 category with youtube streamer.

# In[63]:


# 1a. Is there a correlation between the number of subscribers and the number of likes or comments?

correlation_likes = df['Suscribers'].corr(df['Likes'])
correlation_comments = df['Suscribers'].corr(df['Comments'])


print(correlation_likes)
print(correlation_comments)


# In[77]:


plt.figure(figsize=(8,5))
sns.scatterplot(x = 'Suscribers', y = 'Likes', data = df )
sns.scatterplot(x = 'Suscribers',y = 'Comments',data= df)
plt.title('suscribers vs likes and comments')
plt.xlabel('suscribers')
plt.ylabel('likes vs comments' )
plt.show()


# # Above scatter plot shows that there is weak positive correlation between suscribers ,likes and comments .

# In[79]:


# 2. top countries 
top_countries = df['Country'].value_counts().head(5)
print(top_countries)


# In[86]:


plt.figure(figsize=(6,4))
top_countries.plot(kind= 'bar')
plt.title('top_countries')
plt.xlabel('country')
plt.ylabel('youtube streamers')
plt.show()


# In[99]:


# 3a  distribution of streamers audiences by country. Are there regional preferences for specific content categories?

region_category_counts = df.pivot_table(index='Country', columns='Categories', aggfunc='size', fill_value=0)


plt.figure(figsize=(12, 8))
sns.heatmap(region_category_counts, cmap="YlGnBu")
plt.title('Regional Preferences for Content Categories')
plt.xlabel('Category')
plt.ylabel('Region')
plt.show()



# # Above bar graph show top 5 country with highest streamers.

# In[90]:


# 4a. average number of subscribers, visits, likes, and comments.


df.describe()


# In[104]:


# 4a. averge numbers of likes , suscribers ,comments and visits.
averge_suscriber = df['Suscribers'].mean()
averge_likes = df['Likes'].mean()
averge_Comments = df['Comments'].mean()
averge_visits = df['Visits'].mean()
print(averge_suscriber)
print(averge_likes)
print(averge_Comments)
print(averge_visits)


# In[112]:


# plot barplot for visualisation of averge values.

labels = ['suscribers','likes','comments','visits']
values = [averge_suscriber,averge_likes,averge_Comments,averge_visits]

plt.figure(figsize=(10,6))
plt.bar( labels , values , color=['skyblue', 'red', 'blue', 'lightsalmon'])
plt.title('Averge matrix for youtube streamers')
plt.ylabel('averge count')
plt.show()


# In[103]:


df.columns


# In[127]:


# 5 Which categories have the highest number of streamers?

category_streamer_count = df['Categories'].value_counts()
most_popular_category = category_streamer_count.idxmax()
number_of_streamers = category_streamer_count.max() 

plt.figure(figsize=(7,4))
plt.bar(most_popular_category,number_of_streamers, color= 'skyblue') 
plt.title('category with number of streamers')
plt.xlabel('categories')           
plt.ylabel('number of streamer')
plt.show()


# In[129]:


df['Username']


# In[130]:


# 6 Top 10 youtuber with heighest number of suscribers

Top_10_username= df.nlargest(10 , 'Suscribers')
print(Top_10_username)


# In[138]:


top_10_suscribers = df.nlargest(10, 'Suscribers')
top_10_df = pd.DataFrame(top_10_suscribers[['Username', 'Suscribers']])
print(top_10_df)


# In[143]:


plt.figure(figsize=(10,4))

plt.bar(top_10_df['Username'],top_10_df['Suscribers'])
plt.title('Top 10 Youtuber with number of suscribers') 
plt.xlabel('Youtuber')
plt.ylabel('suscribers') 
plt.xticks(rotation=45)
plt.show()


# In[148]:


# 6 b Top 10 youtuber with maximum numbers of likes

top_10_likes = df.nlargest(10,'Likes')
top_10_likes = pd.DataFrame(top_10_likes[['Username','Likes']])
print(top_10_likes)


# In[152]:


df['Likes']


# In[157]:


df['Likes'] = df['Likes'].astype(int)


# In[154]:


df['Likes']


# In[159]:


df.info()


# In[163]:


plt.figure(figsize=(10,6))
plt.bar(top_10_likes ['Username'],top_10_likes ['Likes'])
plt.title('Top_10_Youtubers with likes')
plt.xlabel('Youtubers')
plt.ylabel('Likes')
plt.xticks(rotation=45)
plt.show()


# #  From the above two graphs we can conclude that T-series and Mrbeast are top youtubers with highest number of suscribers and likes . 

# In[ ]:




