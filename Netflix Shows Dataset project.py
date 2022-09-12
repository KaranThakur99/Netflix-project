#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
data = pd.read_csv(r"C:\Users\KARAN-PC\Downloads\8. Netflix Dataset.csv")


# In[2]:


data


# In[4]:


data.head()


# In[5]:


data.tail()


# In[6]:


data.shape


# In[8]:


data.size


# In[9]:


data.columns


# In[10]:


data.dtypes


# In[12]:


data.info()


# # Task.1. Is there any duplicate record in this dataset ? If yes, then remove the duplicate records.

# In[13]:


data.head(1)


# In[16]:


data.duplicated()


# In[15]:


data[data.duplicated()]


# In[18]:


data.drop_duplicates()       #to drop the duplicates but it will not change it permanently


# In[19]:


data.drop_duplicates(inplace = True)


# In[20]:


data


# In[22]:


data[data.duplicated()] # no dublicate any more


# # Task.2. Is there any null value present in any column ? Show with heat-map    

# In[23]:


# isnull()
data.head(2)


# In[25]:


data.isnull()


# In[26]:


data.isnull().sum()                     #to show the count of null value in each column


# # seaborn library(heat map)

# In[27]:


import seaborn as sns


# In[29]:


sns.heatmap(data.isnull())


# # Q1) For 'House of card', what is the show id and the director of the show?

# In[30]:


data.head()


# In[33]:


data[data['Title'].isin(['House of Cards'])]             # to show all records of a particular item in any column


# # str.contains()

# In[36]:


data[data['Title'].str.contains('House of Cards')]  #to show all record of particular string in any column, same as above can use any


# # Q2) In which year highest number of tv shows & movies were released? show with the bar graph.

# In[37]:


data.head(2)


# In[38]:


data.dtypes


# # to_datetime

# In[40]:


data['Data_N'] = pd.to_datetime(data['Release_Date'])     #adding new column by the name of Data_N in which we will add dates of release


# In[41]:


data.head()


# In[42]:


data.dtypes


# # dt.year.value_counts()

# In[43]:


data['Data_N'].dt.year.value_counts()      # it counts the occurence of all individual years in date column, dt.year means we are cosidering only year fpr date, month and year


# # Bar graph

# In[47]:


data['Data_N'].dt.year.value_counts().plot(kind='bar')


# # Q3) How many movies & tv shows are in a dataset? Show with bar graph.

# # groupby

# In[48]:


data.head(2)


# In[51]:


data.groupby('Category').Category.count()     # to group all unique items of a column and show their count    


# # countplot

# In[52]:


sns.countplot(data['Category'])                                  # to show the count of all unique values in form of bar graph


# # Q4) Show all the movies that were released in year 2000.

# In[53]:


data.head(1)


# In[38]:


data['Year'] = data['Data_N'].dt.year      # created a new column by the name of year 


# In[55]:


data.head(1)


# In[60]:


data[(data['Category'] == 'Movie') & (data['Year'] == 2000)]   # putting two condtions with and operator


# In[61]:


data[(data['Category'] == 'Movie') & (data['Year'] == 2020)]


# # Q5) Show only the titles of all TV shows that were released in india only?

# In[63]:


data.head(2)


# In[64]:


data[(data['Category']== 'TV Show') & (data['Country']=='India')]


# In[65]:


data[(data['Category']== 'TV Show') & (data['Country']=='India')]['Title'] # to show the titles only


# # Q6) Show top 10 directors, who gave the highest number of movies and tv shows?

# In[69]:


data['Director'].value_counts().head(10)


# # Q7) Show all the records, where "category is movie and type is comedies" or "country is united kingdom".

# In[7]:


data.head(20)


# In[5]:


data[ (data['Category']== 'Movie') & (data['Type']== 'Comedies') ]


# In[11]:


data[(data['Category']== 'Movie') & (data['Type']== "Comedies") | (data["Country"]== "United Kingdom")] #


# # Q3) In how many movies/shows, Tom Cruise was cast?

# In[16]:


data.head(2)


# In[19]:


data[data["Cast"]== "Tom Cruise"]   # no movies by tom cruise only, other peeps are also with him so need to serach by str.contains() within a string. this filtering doesn't apply where there are multiple values


# # str.contains()

# In[20]:


data[data["Cast"].str.contains("Tom Cruise")]


# # create a data frame with no null value

# In[21]:


data_new = data.dropna()     # it drops the row that contains all or any missing values.


# In[23]:


data_new.head(2)


# In[25]:


data_new[data_new["Cast"].str.contains("Tom Cruise")]  # here we go we got 2 values where tom cruise is cast.


# # Q9) What are the differnt ratings defined by netflix.

# In[26]:


data.head(2)


# In[27]:


data["Rating"].nunique()


# In[29]:


#unique
data["Rating"].unique()


# # Q.9.1. How many movies got the "TV-14" rating, in canada?

# In[30]:


data.head(2)


# In[32]:


data[(data["Category"]== "Movie") & (data["Rating"]== "TV-14")]


# In[34]:


data[(data["Category"]== "Movie") & (data["Rating"]== "TV-14")].shape


# In[35]:


data[(data["Category"]== "Movie") & (data["Rating"]== "TV-14") & (data["Country"]== "Canada")]


# In[36]:


data[(data["Category"]== "Movie") & (data["Rating"]== "TV-14") & (data["Country"]== "Canada")].shape


# # Q.9.2 How many tv shows got the 'R' rating after year 2018?

# In[37]:


data.head(2)


# In[39]:


data(data["Category"]== "TV Show") & (data["Rating"]== "R") & (data["year"] > 2018)]


# # Q10) What is the maximum duration of a movie/show on netflix?

# In[40]:


data.head(2)


# In[41]:


data.Duration.unique()         # it will also the same data.["Duration"].unique()


# In[42]:


data.Duration.dtypes


# # str.split()

# In[43]:


data.head(2)


# In[46]:


data[["Minutes", "Unit"]] = data['Duration'].str.split(' ', expand = True)


# In[47]:


data.head(2)


# In[48]:


#max()
data['Minutes'].max()


# In[49]:


data['Minutes'].min()


# In[50]:


data['Minutes'].mean()


# In[51]:


data.dtypes


# # Q.11) Which individual country has the highest no. of tv shows?

# In[52]:


data.head(2)


# In[54]:


data_tvshow = data[data['Category']== 'TV Show']           # created a table of Tvshows only


# In[56]:


data_tvshow.head()


# In[57]:


data_tvshow.Country.value_counts()


# In[58]:


data_tvshow.Country.value_counts().head(1)


# # Q12) how can we sort the dataset by year?

# In[59]:


data.sort_values(by= 'Year').head()


# In[ ]:


data.sort_values(by= 'Year', ascending=False)


# # Q14) Find all the instances where:

# #    Category is 'Movie' and type is 'Dramas'

# #                         or

# # Category is 'TV Show' & Type is "kids'TV'

# In[60]:


data.head(2)


# In[64]:


data[(data['Category']== 'Movie') &(data['Type']== 'Dramas') | (data['Category']== 'TV Show') &(data['Type']== "Kids' TV")]


# In[ ]:




