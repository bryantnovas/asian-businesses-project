<div align="center"><img src="4-Months Ago.png"></div>

## Contents

- [Acknowledgement](#acknowledgement)
- [Introduction](#introduction)
- [Installation](#installation)
- [Technology Stack](#technology-stack)
- [Data Cleaning](#data-cleaning)
- [Hypothesis](#hypothesis)
- [Conclusion](#conclusion)
- [About us](#about-us)

# SBS Recovery 

# Acknowledgement
Our team would like to acknowledge alll the Asian communities that have been impacted by the massive Asian hate that occured due to this pandemic. We hope to find more solutions that enforce the #StopAsianHate movement. Our team would also like to thank all instructors at The Knowledge House for their guidance, help, encouragement and inspiration to complete this Capstone Project. This wouldn't have been possible without you. Lastly we would like to thank the SBS, Census, and the NYPD for providing public information on hate crime complaint statics. 

# Introduction
**We were taked with finding ways to allocate resources for Small Buisness that were impacted by COVID-19.By analyzing hate crime data,news articles, and buisness traffic we were able to determine that Asian Buisness were the ones that the minority group that was impacted the most ever since COVID-19 were Asian business. By analyzing these trends, we were able to reach a conclusion and prove/disprove our hypothesis.**

Our data sources are:
https://www1.nyc.gov/site/nypd/stats/reports-analysis/hate-crimes.page
This is the source for hate crime annual reports. For this analysis we used 2020 and 2019 annual reports. 
https://web.sba.gov/pro-net/search/dsp_dsbs.cfm
This is the data source for small business that are registered, we filtered our searches for minority oowned business.
https://www.census.gov/econ/currentdata/datasets/index
This is the source for analyzing all the business traffic we analyzed several annual reports of the the different kinds of industries.
<br>

# Installation

In order to run this application locally on you machine you would need to follow these instructions:
1. In your terminal type:  "pip install pipenv" - this will create the enviroment
2. In order to activate the enviroment type: "pipenv shell"
3. In order to install all packages needed type: "pipenv install"
4. And finally you can run the app by typing this command: "streamlit run app.py"

<br>

<div align="center"><img src="./img/app.gif"></div>

<br>

<div align="center"><img src="./img/home_screenshot.png"></div>

<br>

<div align="center"><img src="./img/totals_screenshot.png"></div>

<br>

<div align="center"><img src="./img/boro_screenshot.png"></div>

# Technology Stack
In this analysis, we used python as the primary programming language because of its rich palette of tools that make data analysis a cinch. Some of the packages we used are
| Library | Description |
| --- | --- |
| [Matplotlib](https://matplotlib.org/) | Matplotlib is a library utilized to make custom visualizations that are interactive or static and easy to interpert. |
| [NumPy](https://github.com/numpy/numpy) | NumPy is a popular library used for array manipulation. In comparison to other libraries, NumPy makes it efficient to work with to adjust our data. |
| [Pandas](https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html) | Pamdas is another library for data science that is used for open source data and manipulating dataframes. We used this library for our data cleaning to iterate through rows and columns, and work with missing data. |
| [Bokeh](https://docs.bokeh.org/en/latest/index.html) | Bokeh is another library utilized for intereactive visualizations.Bokeh reenders its graphics using HTML and Javascript. This is also another great for making web dashboards and applications. |
| [Streamlit](https://streamlit.io) | Streamlit is an open source library to make a. custom web application. It is used for Machine Learning engineering and makes it easy to make a dashboard. |
| [Folium](https://python-visualization.github.io/folium/) | Folium makes it easy to create GeoMaps in Python.It allows us to make an excellent plotting on the geo maps. |
| [PyGoogleNews](https://github.com/kotartemiy/pygooglenews) | This library acts as a python wrapper of the Google News feed and allows us to parse through aricles, and make an extensive search for specific articles. |

To understand further how we have utilzed these libraries, you can take a look at the links of the documentation that have been provided above.
# Data Cleaning

Before we start analyzing our data, we must first start data cleaning our data sources and make sure we can manipulate our data to draw our conclusions. When cleaning our data, we had to keep in mind that our News Articles were specified in New York City. Alot of our data had to be specified to boroughs or zip code in NYC, as we must graph based on the geographic area's in New York. Another modification we made was analyzing our data by Anti-Asian hate crimes. In some cases, precints were not recorded so we filled our value's to not impact our datasets.

### What should we look into / errors?


# Hypothesis
#### What are our proposed Hypothesis? 

## Hypothesis 1

####  Our hypothesis is that throughout the pandemic there has been an increase in Hate Crime in the Asian community, due to the origin being reported in China.Therefore impacting the view of the Asian community,publicly and many feeling discouraged by the viewpoint of the Asian community. We hypothesize that due to the pandemic, there is a difference in trend with the hate crime data, and there is a higher amount of hate crime for the Asian community.

## Hypothesis 2
####  By looking for common words that were negatively associated within articles that were identified as Anti-Asian, we can determine the relationship between the Anti-Asian crimes that exist. We can also analyze how Anti-Asian crimes have shifted throughout the pandemic and currently are potrayed in the news to identify how badly impacted the Asian communities were harmed. My hypothesis is that the words that are negatively associated within the newspaper articles surrounding the news around Anti-Asian crimes has increased. Overall impacting the business traffic of Asian business and increasing hate crime surrounding Asian communities. 

## Hypothesis 3
### Hypothesis: We hypothesize that the amount of overall sales will decrease when the pandemic became widespread in 2020, and many businesses were forced to close and/or shift their business model.¶

## Hypothesis 4
### Financial resources such as the SBA loan are not being distributed to the small businesses in the communities that need the assistance the most.The data in this notebook will show the how many businesses recieve financial assistance through SBA loans by borough.


# Conclusion¶
Overall we were able to form several conclusions from our data analysis, and comprehend that the Asian community was impacted heavily throughout the pandemic. As well, as we were able to draw conclusions of what areas of business were impacted the most, and how buisness traffic shifted. 

Hate Crime for the Asian Community did increase from 2019 to 2020, therefore showing that the Asian community was impacted the most in 2020 affecting their buisness.One way we can contunie to do a further analysis is by analyzing the boroughs and common zipcodes that were identified in customers survey and compare that to COVID-19 data. By analyzing the behavior we can see the common trends and patterns of where area's got hit the most.Overall within the last couple months, the negative connatation of words within the newspapers.Allowing us to observe that many of those who are in the Asian community were attacked and harmed and hated on.We encourage the asian community, to feel comfortable reporting crimes and incidents that occur to them, to show that there is a greater need for bringing their buisness back.

From our SBA loan data, we are able to see that majority of finacial asssistance went to cities in New York that are outside of the 5 boroughs. Therefore proving that business in New York City did not get the finacial need, where it has the largest percentage of minorities, including the Asian community.As expected, the outbreak of the coronavirus pandemic and the subsequent lockdown had a major impact on sales, especially in the months of March and April of 2020. The industries that faired the best was Retail, Retail Trade and Food Services while Health and Personal Care stores faired the least. There was a significant difference between the Retail, Retail Trade and Food Services and the other business industries covered in this study. Perhaps more investigation can be done on why there was such a significant gap between those industries. 

Our overall solution is to bring recognition,by implementing the survey that we created and sending it out to each business  that is registered under our Small Buisness Data. Using the survey results, we will display the results in the similar format of our dashboard to stakeholders, government officials, that can bring awarness and funds to the conversation.
# About us

| Preview                                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [<img src="./img/Bryant Novas.jpg" width="1000" />]                                                                                                                                              |Bryant is an aspiring data scientist with a passion for IT & Data with over 8 yrs of experience in help desk support and repairs. It is important for me as an individual to work for a company in which I admire the mission and the people I am surrounded by. I enjoy learning new things, both related and unrelated to tech and value being in an environment in which I can continue to grow and provide value                                                                                 |
| [<img src="./img/Amy Rosa.jpg" width="1000" />]                                                                                                                                               | Amy served as an educator, mentor, and reliable colleague. Part of being an educator is to have a love of learning, a deep intellectual curiosity that drives you toward continual growth and wisdom. That love of learning and intellectual curiosity is what led me to The Knowledge House, where she has gained technical skills that were non-existent before, skills which she work diligently everyday to perfect. In the near future, she hopes to obtain a data analyst position or an internship within the data science field that will enable her to further develop my technical skills.|

| [<img src="./img/Jessica De Mota Munoz .jpg" width="1000" />]                                                                                                                                               |Jessica De Mota Munoz is currently an Undergraduate Junior at Hunter College majoring in Computer Science and minoring in Psychology. Throughout the years, she has interned at different companies such as IBM,Pfizer,and Mount Sinai that have given her knowledge of the technical field. As well as worked on open source projects with Netflix and done research with Google. Jessica hopes to obtain her degree in the near future, and contunie expanding herself in the tech field, as a Data Analyst and Product Manager that encourage projects in Public Advocacy.Her goal is to help find solutions in communities that are often not represented through Data. |

| [<img src="./img/Gyasi Sturgis.jpg" width="1000" />]                                                                                                                                               | Gyasi Sturgis is currently a  a senior at Lehman College in The Bronx. he is a computer science major with a particular interest in data science. Some of his hobbies include bike riding, gaming and chess.|