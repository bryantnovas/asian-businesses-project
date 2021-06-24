#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set()


# # Table of Contents:
# 
# [1.Introduction & Hypothesis](#1)<br>
# [2.Analysis on our Data](#2)<br>
# [3.Conclusions](#3)<br>

# ## Introduction & Hypothesis <a id='1'></a>:
# 
# ### Introduction:
#     What is the SBA Loan? 
#     an SBA loan is a small business loan that is partially guaranteed by the government (the Small Business Administration), which eliminates some of the risk for the financial institution who is issuing the loan.
#     SBA loans can range in size anywhere from $500 to $5.5 million and can offer APR’s as low as 6.5%. Additionally, repayment terms for SBA loans can range from 5 to 25 years, but 10 years is a standard SBA loan repayment term length.
#     This notebook will be analyzing the data from the website below regarding SBA loans in New York.
#   <a href=" https://web.sba.gov/dsbs/search/dsp_dsbs.cfm"> click here</a>
# 
# ### Hypothesis:
#      My hypotheis is that financial resources such as the SBA loan are not being distributed to the small businesses in the communities that need the assistance the most.
# 
#      The data in this notebook will show the how many businesses recieve financial assistance through SBA loans by borough.
# 

# In[2]:


pd.set_option('display.max_columns', None)


# In[3]:


df = pd.read_csv('SBA_dataset.csv')


# In[4]:


df.head(3)


# ## Analysis on our data <a id='2'></a> :

# In[5]:


df['City'] = df['City'].str.lower()


# In[6]:


# The average year established for these businesses is 2011
df['Year Established'].mean()


# In[7]:


Queens = ['arverne', 'astoria', 'bayside', 'bellerose', 'breezy point', 'cambria heights',
          'college point', 'corona east', 'elmhurst', 'elmhurst', 'far rockaway', 'floral park', 'flushing',
          'forest hills', 'fresh meadows', 'glen oaks', 'hollis', 'howard beach', 'jackson heights', 'jamaica', 'kew gardens',
          'little neck', 'long island city', 'maspeth', 'middle village', 'oakland gardens', 'ozone park', 'queens village', 'rego park',
          'richmond hill', 'ridgewood', 'rockaway park', 'rosedale', 'saint albans', 'south ozone park', 'south richmond hill', 'springfield gardens', 'sunnyside', 'whitestone', 'woodhaven', 'woodside']
print(Queens)
df.loc[(df.City.isin(Queens)),'City']='queens'


# In[8]:


Bronx = ['allerton', 'baychester', 'bedford park', 'belmont', 'castle hill', 'city island', 
 'clason point', 'co-op city', 'eastchester', 'edenwald', 'fordham', 'highbridge', 'hunts point', 'kingsbridge', 'longwood', 'marble hill',
 'melrose', 'morris heights', 'morris park', 'morrisania', 'mott haven', 'mount hope', 'norwood', 'parkchester', 'pelham bay', 'riverdale', 'soundview', 'the hub', 'throgs neck', 'tremont', 'university heights', 'wakefield', 'west farms', 'westchester', 'williamsbridge', 'woodlawn']
print(Bronx)
df.loc[(df.City.isin(Bronx)),'City']='bronx'


# In[9]:


Staten_Island = ['annadale', 'arden heights', 'arlington', 'arrochar', 'bay terrace', 
 'bloomfield', 'brighton heights', 'bulls head', 'castleton', 'castleton corners', 'charleston', 'chelsea', 'clifton', 'concord', 
 'dongan hills', 'egbertville', 'elm park', 'eltingville', 'emerson hill', 'fort wadsworth', 'graniteville', 'grant city', 'grasmere', 'great kills', 'greenridge', 'grymes hill', 'hamilton park', 'heartland village', 'huguenot', 'lighthouse hill', 'livingston', 'manor heights', 'mariners harbor', 'meiers corners', 'midland beach', 'new brighton', 'new dorp', 'new springville', 'oakwood', 'ocean breeze', 'old place', 'old town', 'pleasant plains', 'port richmond', 'prince’s bay', 'randall manor', 'richmond valley', 'richmondtown', 'rosebank', 'rossville', 'sandy ground', 'shore acres', 'silver lake', 'south beach', 'st.george', 'stapleton', 'stapleton heights', 'sunnyside', 'todt hill', 'tompkinsville']
print(Staten_Island)
df.loc[(df.City.isin(Staten_Island)),'City']='staten island'


# In[10]:


Manhattan = '''
Alphabet City
Astor Row
Battery Park City
Bowery
Carnegie Hill
Chelsea
Chinatown
Civic Center
Columbus Circle
Cooperative Village
Diamond District
Downtown Manhattan
East Harlem
East Village
Financial District
Five Points
Flatiron District
Fort George
Garment District
Gramercy Park
Greenwich Village
Hamilton Heights
Hell’s Kitchen
Herald Square
Hudson Yards
Inwood
Kips Bay
Koreatown
Lenox Hill
Lincoln Square
Little Germany
Little Italy
Lower East Side
Madison Square
Manhattan Valley
Marble Hill
Marcus Garvey Park
Meatpacking District
Midtown
Morningside Heights
Murray Hill
NoHo
Nolita
NoMad
Battery Park City
Radio Row
Rockefeller Center
Rose Hilll
SoHo
South Street Seaport
Strivers’ Row
Stuyvesant Square
Stuyvesant Town
Sugar Hill
Sutton Place
Tenderloin
Theater District
Times Square
Tribeca
Tudor City
Turtle Bay
Two Bridges
Union Square
Upper East Side
Upper West Side
Washington Heights
Waterside Plaza
West Village
Yorkville
'''
Manhattan_list = Manhattan.lower().split()
print(Manhattan_list)
df.loc[(df.City.isin(Manhattan_list)),'City']='manhattan'


# In[11]:


Brooklyn = ['admirals row', 'atura', 'barren island', 'bath beach', 'bay ridge', 'bedford', 'bedford-stuyvesant', 'bensonhurst',
 'bergen beach', 'bococa', 'boerum hill', 'borough park', 'brighton beach', 'brooklyn heights', 'brownsville', 'bushwick', 'cadman plaza',
 'canarsie', 'carroll gardens', 'city line', 'clinton hill', 'cobble hill', 'coney island', 'crown heights', 'cypress hills', 'ditmas park', 
 'downtown dumbo', 'dyker heights', 'east flatbush', 'east new york', 'east williamsburg', 'farragut', 'fiske terrace', 'flatbush', 'flatlands', 'fort greene', 'fort hamilton', 'fulton ferry', 'georgetown', 'gerritsen beach', 'gowanus', 'gravesend', 'greenpoint', 'greenwood heights', 'highland park', 'homecrest', 'kensington', 'little poland', 'madison,', 'manhattan beach', 'marine park', 'midwood', 'mill basin', 'navy yard', 'new lots', 'new utrecht', 'ocean hill', 'ocean parkway', 'park slope', 'pigtown', 'plum beach', 'prospect heights', 'prospect park', 'south prospect', 'lefferts gardens', 'rambo', 'red hook', 'sea gate', 'sheepshead bay', 'south brooklyn', 'south park slope', 'starrett city', 'stuyvesant heights', 'sunset park', 'vinegar hill', 'weeksville', 'white sands', 'williamsburg', 'windsor terrace', 'wingate']
print(Brooklyn)
df.loc[(df.City.isin(Brooklyn)),'City']='brooklyn'


# In[12]:


# setting any city in the dataframe that is not apart of the 5 boroughs to "other"
df.loc[(~df.City.isin(['brooklyn','bronx','queens','staten island',"manhattan"])),'City']='other'


# In[13]:


df


# In[14]:


newdf = df[df.City.isin(["bronx", "brooklyn","queens","manhattan","staten island", "other"])]


# In[16]:


len(newdf)


# In[17]:


data = newdf.groupby("City")['City'].count()


# In[18]:


# data.plot.pie(autopct="%.1f%%")


# In[19]:


pie, ax = plt.subplots(figsize=[10,6])
labels = data.keys()
plt.pie(x=data, autopct="%.1f%%", labels=labels, pctdistance=0.5)
plt.title(" Percentage of Businesses W/ SBA loans by City", fontsize=14);
# pie.savefig("SBAPieChart.png")
plt.show()


# # Conclusion <a id='3'></a>:
#     from this pie chart you can see a majority of the SBA loans went to cities in New York that are outside of the 5 boroughs. Therefore from this data I would say more resources should be allocated to small businesses within boroughs such as The Bronx which has only 5 percent 

# In[ ]:




