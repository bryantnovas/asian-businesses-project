import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st


def app():
    st.write(
        '''
        ## **Background & Introduction:**


        ### **Objective :**
        The objective is to analyze the Hate Crime Data in NYC. Specifically, we want to analyze Anti-Asian Hate Crime. With COVID-19,many Anti-Asians faced a huge shift in their buisness traffic. By analyzing, the hate crime data, we want to see the relationship this has within NYC and the Asian business that exist. 

        ### **What Is A Hate Crime?**
        A hate crime is defined as the highest priority of the FBI's civil rights program. A hate crime as a whole is defined as a crime involving violence. that is motivated by prejudice on the basis of   race,religion, sexual orientation, or other groups. 

        ### **How Many Hate Crimes Occur Per Year?**
        There are 7,314 hate crime incidents involving 8,559 offenses. The predicate offenses of a hate crime consist of murder, non negligent manslaughter,forcible rape,agg assault, arson, intimidation, and vandalism. 

        ### **Hypthesis:**
        Our hypothesis is that throughout the pandemic there has been an increase in Hate Crime in the Asian community, due to the origin being reported as China.Therefore impacting the view of the Asian community,publicly and many feeling discouraged by the viewpoint of the Asian community. Overall the 500% of Hate Crimes impact the buisness traffic of the Asian buisness that exist. We also hypothesize that due to the pandemic, there is a difference in trend with the hate crime data.

        ## **Analysis on Our Data**

        ### **Our Data:**

        The data is organized by the report sightings that are found per each precicnt. Each is selected by bias category, and bias type with the offense description of what they face. Ranging from the first date to most recent date, and analyzed from quarterly reports that are passed to the NYPD. All with a specific offense description and the number of arrests that occured within that day. 


        ### **Libraries We Will Be Using:**
        - Numpy -> We are using the numpy to create array's that we can chart. 
        - Pandas -> The pandas library is being used to read and analyze our dataframe 
        - MatPlotLib -> We are using matplotlib for data visualization.

        We are reading in the dataframe of the Hate Crimes that occured in 2020.
        ''')

    df = pd.read_csv(
        "./datasets/hate-crime-arrests-by-motivation-annual-2020.csv")
    st.write(df)

    st.write('Analyzing our dataframe we can see that there are many null values that appear in our dataframe.')

    st.write('All the null values are represented in the first columns in which we are not using therefore we can eliminate these values.')

    df = df.drop([0, 1, 2, 3, 4, 5])

    st.write('Now we have dropped the null values so we can re-arrange our dataframe in a manner that is convivemy for our report')

    st.write(df)

    st.write('We are renaming our columns so we can work with them more appropiately to identify the bias-motivations.')
    df = df.rename(columns={"Unnamed: 0": "Index", "Unnamed: 1": "Precinct", "Unnamed: 2": "Gender",
                            "Unnamed: 3": "Race", "Unnamed: 4": "Age", "Unnamed: 5": "Bias-Motivation"})

    st.write(df['Bias-Motivation'].values)

    st.write('We are going to store these values in a dictionary with the appropiate group that is associated with the Bias-Motivation')

    Group = {'ANTI-ASIAN': 'Anti-Ethnicity',
             'ANTI-WHITE': 'Anti-Ethnicity',
             'ANTI-BLACK': 'Anti-Ethnicity',
             '60 YEARS OLD OR MORE': 'Anti-Age',
             'ANTI-JEWISH': 'Anti-Religion',
             'ANTI-ISLAMIC(MUSLIM)': 'Anti-Religion',
             'ANTI-MALE HOMOSEXUAL(GAY)': 'Anti-LGBTQ',
             'ANTI-LGBT(MIXED GROUP)': 'Anti-LGBTQ',
             'ANTI-TRANSGENDER': 'Anti-LGBTQ',
             'ANTI-FEMALE': 'Anti-LGBTQ',
             'OTHER': 'Other',
             'NON CONFORMING': 'Other'
             }
    st.write(Group)

    st.write(
        'Now we are copying our original dataframe to make new edits to our new dataframe')

    twentytwenty_hate = df.copy()

    st.write(
        'Using our dictionary we are placing these values into a new column which we use later on.')

    twentytwenty_hate['Categories'] = twentytwenty_hate['Bias-Motivation'].map(
        Group)

    st.write(twentytwenty_hate)

    st.write('Now we are going to analyze the same with precinct as all precinct are identified with a Borough and can be grouped by a Borough.')

    precinct_dictionary = {'120': 'Staten Island',
                           '005': 'Manhattan',
                           '006': 'Manhattan',
                           '007': 'Manhattan',
                           '009': 'Manhattan',
                           '010': 'Manhattan',
                           '013': 'Manhattan',
                           '023': 'Manhattan',
                           '028': 'Manhattan',
                           '040': 'Bronx',
                           '044': 'Bronx',
                           '046': 'Bronx',
                           '048': 'Bronx',
                           '049': 'Bronx',
                           '060': 'Brooklyn',
                           '061': 'Brooklyn',
                           '066': 'Brooklyn',
                           '067': 'Brooklyn',
                           '100': 'Queens',
                           '101': 'Queens',
                           '102': 'Queens',
                           '107': 'Queens',
                           '110': 'Queens',
                           '111': 'Queens',
                           '112': 'Queens',
                           '114': 'Queens',
                           '115': 'Queens',
                           '078': 'Brooklyn',
                           '084': 'Brooklyn',
                           'nan': 'hello'}
    st.write(precinct_dictionary)

    st.write('Similar to earlier, we are going to make a new column in our dataframe that will create a Borough column.This makes it easier, rather than graphing by Precinct that contain multiple values we are only limiting it to 5 different boroughs.')
    twentytwenty_hate['Borough'] = twentytwenty_hate['Precinct'].map(
        precinct_dictionary)

    st.write(twentytwenty_hate)

    st.write('Now we are plotting our information to view the different kinds of groups per borough and a specific Bias-Motivation.')

    st.write('This is our analysis of Anti-Asian Count Per Borough, we are able to analyze that the Boroughs in which the most Anti-Asian Crimes were in Manhattan and Bronx')

    with sns.axes_style("white"):
        twentytwenty_hate[twentytwenty_hate["Bias-Motivation"] == "ANTI-ASIAN"].groupby("Borough").size().sort_values(
            ascending=False).plot(kind='pie',  xlabel='Borough', title='Anti-Asian Count Per Borough', autopct='%.2f')
    st.pyplot()

    st.write('This is our analysis of Anti-Religion Count Per Borough, we are able to analyze that the Boroughs in which the most Anti-Religion were located in Brooklyn.')

    with sns.axes_style("white"):
        twentytwenty_hate[twentytwenty_hate["Categories"] == "Anti-Religion"].groupby("Borough").size().sort_values(
            ascending=False).plot(kind='pie', xlabel='Borough', title='Anti-Religion Count Per Borough', autopct='%.2f')
    st.pyplot()

    st.write('This is our analysis of Anti-Ethncity Count Per Borough, we are able to analyze that the Boroughs in which the most Anti-Ethnicity was located the most in Manhattan.')

    with sns.axes_style("white"):
        twentytwenty_hate[twentytwenty_hate["Categories"] == "Anti-Ethnicity"].groupby("Borough").size().sort_values(
            ascending=False).plot(kind='pie', xlabel='Borough', title='Anti-Ethnicity Count Per Borough', autopct='%.2f')
    st.pyplot()

    st.write('This is our analysis of Anti-LGBTQ Count Per Borough, we are able to analyze that the Boroughs in which the most Anti-LGBTQ  Hate Crimes occured was in Queens.')

    with sns.axes_style("white"):
        twentytwenty_hate[twentytwenty_hate["Categories"] == "Anti-LGBTQ"].groupby("Borough").size().sort_values(
            ascending=False).plot(kind='pie', xlabel='Borough', title='Anti-LGBTQ Count Per Borough', autopct='%.2f')

    st.write('This is our analysis of Anti-Age  Count Per Borough, we are able to analyze that the Boroughs in which the most Anti-Age  Hate Crimes were  located in Queens.')

    with sns.axes_style("white"):
        twentytwenty_hate[twentytwenty_hate["Categories"] == "Anti-Age"].groupby("Borough").size().sort_values(
            ascending=False).plot(kind='pie', xlabel='Borough', title='Anti-Age Count Per Borough', autopct='%.2f')
    st.pyplot()

    st.write('This is our analysis of Unidentifiable Hate Crimes Per Borough, we are able to analyze that the Boroughs in which the most Unidentifiable  Hate Crimes were located in Manhattan.')

    with sns.axes_style("white"):
        twentytwenty_hate[twentytwenty_hate["Categories"] == "Other"].groupby("Borough").size().sort_values(
            ascending=False).plot(kind='pie', xlabel='Borough', title='Other Count Per Borough', autopct='%.2f,')
    st.pyplot()

    st.write('### **Analyzing our 2nd Dataset:**')

    st.write('This dataset is from our 2019 Hate Crime')

    nineteen_hate_crime = pd.read_csv("./datasets/2019 Hate Crime.csv")

    st.write('We are using loc to visualize the dataset without the null values, and comprehend how we want the dataframe needs to look like.')

    st.write(nineteen_hate_crime.loc[4:])

    st.write(
        'Knowing how this information looks like, we can drop the rows that are not needed.')

    nineteen_hate_crime = nineteen_hate_crime.drop([0, 1, 2, 3])

    st.write('There are still rows that are empty,therefore we can just drop them.')

    st.write('We can also drop the columns after Unnamed5 because they all represent null values that are unecessary for us.')

    nineteen_hate_crime = nineteen_hate_crime.drop(
        columns=['Unnamed: 6', 'Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9', 'Unnamed: 10'])

    st.write(
        'Now let\'s rename our columns to be appropoate and fill values that are empty with 0')

    nineteen_hate_crime = nineteen_hate_crime.rename(columns={"NYC Hate Crime Report": "Index", "Unnamed: 1": "Precinct", "Unnamed: 2": "Gender",
                                                              "Unnamed: 3": "Race", "Unnamed: 4": "Age", "Unnamed: 5": "Bias-Motivation"})

    st.write('Fill the nan values with 0')

    nineteen_hate_crime['Precinct'] = nineteen_hate_crime['Precinct'].fillna(0)

    st.write('In 2019 there was only 3 Asians who were targeted for a hate crime.')

    st.write('Get all precicnt values and group them by borough or add a borough column in so it\'s associated with all the datasets keep in mind precints with value 0 are with no borough')

    st.write('These precinct values can be stored with their borough in a dictionary and we can map this in a proper way to create a new column.')

    cop_dictionary = {'1': 'Manhattan',
                      '5': 'Manhattan',
                      '6': 'Manhattan',
                      '9': 'Manhattan',
                      '10': 'Manhattan',
                      '13': 'Manhattan',
                      '14': 'Manhattan',
                      '17': 'Manhattan',
                      '18': 'Manhattan',
                      '25': 'Manhattan',
                      '28': 'Manhattan',
                      '30': 'Manhattan',
                      '32': 'Manhattan',
                      '33': 'Manhattan',
                      '34': 'Manhattan',
                      '40': 'Bronx',
                      '42': 'Bronx',
                      '43': 'Bronx',
                      '47': 'Bronx',
                      '48': 'Bronx',
                      '49': 'Bronx',
                      '60': 'Brooklyn',
                      '61': 'Brooklyn',
                      '62': 'Brooklyn',
                      '63': 'Brooklyn',
                      '66': 'Brooklyn',
                      '66': 'Brooklyn',
                      '67': 'Brooklyn',
                      '68': 'Brooklyn',
                      '70': 'Broooklyn',
                      '71': 'Brooklyn',
                      '75': 'Brooklyn',
                      '76': 'Brooklyn',
                      '77': 'Brooklyn',
                      '79': 'Brooklyn',
                      '81': 'Brooklyn',
                      '84': 'Brooklyn',
                      '88': 'Brooklyn',
                      '90': 'Brooklyn',
                      '94': 'Brooklyn',
                      '101': 'Queens',
                      '102': 'Queens',
                      '103': 'Queens',
                      '106': 'Queens',
                      '107': 'Queens',
                      '110': 'Queens',
                      '112': 'Queens',
                      '113': 'Queens',
                      '114': 'Queens',
                      '115': 'Queens',
                      0: 'Un-Identified'}

    nineteen_hate_crime['Borough'] = nineteen_hate_crime['Precinct'].map(
        cop_dictionary)

    nineteen_hate = nineteen_hate_crime.copy()

    st.write('We can place these values to create categories, just analyzing the values in this column they differ from 2020.')

    category_dictionary = {'Anti-Islamic (Muslim)': 'Anti_Religion',
                           'Anti-Jewish': 'Anti_Religion',
                           'Anti-transgender': 'Anti_LGBTQ',
                           'Anti-male homosexual (Gay)': 'Anti_LGBTQ',
                           'Anti-female homosexual (Lesbian)': 'Anti_LGBTQ',
                           'Anti-Hispanic': 'Anti_Ethnicity',
                           'Anti-White': 'Anti_Ethnicity',
                           'Anti-Black': 'Anti-Ethnicity',
                           'Anti-multi racial groups': 'Anti_Ethnicity',
                           'Anti-Hispanic': 'Anti_Ethnicity',
                           'Anti-Asian': 'Anti_Ethnicity'
                           }

    nineteen_hate['Categories'] = nineteen_hate['Bias-Motivation'].map(
        category_dictionary)

    st.write(
        'This is a visualization of the different kinds of Categories Per Borough')

    st.write('Anti_Religion was identified the most in Manhattan, however the Borough is Un-Identified for those who are Anti-Religion')

    with sns.axes_style("white"):
        nineteen_hate[nineteen_hate["Categories"] == "Anti_Religion"].groupby("Borough").size().sort_values(
            ascending=False).plot(kind='bar', xlabel='Borough', ylabel='Anti-Religion Count Per Borough')
    st.pyplot()

    with sns.axes_style("white"):
        nineteen_hate[nineteen_hate["Categories"] == "Anti_Religion"].groupby("Borough").size().sort_values(
            ascending=False).plot(kind='pie', xlabel='Borough', ylabel='Anti-Religion Count Per Borough', autopct='%.2f')
    st.pyplot()

    st.write(
        'Hate Crime Against Anti_Ethinicity is identifed the most at an Unidentified Precinct.')

    with sns.axes_style("white"):
        nineteen_hate[nineteen_hate["Categories"] == "Anti_Ethnicity"].groupby("Borough").size().sort_values(
            ascending=False).plot(kind='pie', xlabel='Borough', ylabel='Anti-Ethncity Count Per Borough', autopct='%.2f')
    st.pyplot()

    st.write(
        'Hate Crime Against Anti-LGBTQ is identifed the most at an Unidentified Precinct.')

    with sns.axes_style("white"):
        nineteen_hate[nineteen_hate["Categories"] == "Anti_LGBTQ"].groupby("Borough").size().sort_values(
            ascending=False).plot(kind='pie', xlabel='Borough', ylabel='Anti-LGBTQ Count Per Borough', autopct='%.2f')
    st.pyplot()

    st.write(
        'Hate Crime Against Asian Community is identifed the most at an Unidentified Precinct.')

    with sns.axes_style("white"):
        nineteen_hate[nineteen_hate["Bias-Motivation"] == "Anti-Asian"].groupby("Borough").size().sort_values(
            ascending=False).plot(kind='pie', xlabel='Borough', ylabel='Anti-Asian Count Per Borough', autopct='%.2f')
    st.pyplot()

    st.write('From this we are able to identify that alot of the Boroughs aren\'t identified whether it was that the Precicnt wasn\'t identifed or someone didn\'t feel comfortable to do so, showing inaccuracies in data.')

    st.write('## **Exploratory Data Analysis:**')

    st.write('Save all values into variables to plot  of all the different categories')

    nineteen_lgbtq = nineteen_hate[nineteen_hate["Categories"]
                                   == "Anti_LGBTQ"].groupby("Borough").size()

    nineteen_ethnicity = nineteen_hate[nineteen_hate["Categories"]
                                       == "Anti_Ethnicity"].groupby("Borough").size()

    nineteen_religion = nineteen_hate[nineteen_hate["Categories"]
                                      == "Anti_Religion"].groupby("Borough").size()

    twentytwenty_religion = twentytwenty_hate[twentytwenty_hate["Categories"]
                                              == "Anti-Religion"].groupby("Borough").size()

    twentytwenty_ethnicity = twentytwenty_hate[twentytwenty_hate["Categories"]
                                               == "Anti-Ethnicity"].groupby("Borough").size()

    twentytwenty_lgbtq = twentytwenty_hate[twentytwenty_hate["Categories"]
                                           == "Anti-LGBTQ"].groupby("Borough").size()
    with sns.axes_style("white"):
        plt.plot(nineteen_religion, label='Religion')
        plt.plot(nineteen_ethnicity, label='Ethnicity')
        plt.plot(nineteen_lgbtq, label='LGBTQ')
        plt.plot(twentytwenty_religion, label='Religion')
        plt.plot(twentytwenty_ethnicity, label='Ethnicity')
        plt.plot(twentytwenty_lgbtq, label='LGBTQ')
        plt.grid(True, color='k', linestyle=':')
        plt.title('Different Categories Per Borough')
        plt.xlabel('Boroughs')
        plt.ylabel('Count')
        plt.style.use('fivethirtyeight')
        plt.legend()
        st.pyplot()

    st.write('Overall in 2019, the trend that was the common was Religion and in 2020 Ethnicity peaked the most as well as the LGBTQ hate.')

    st.write(
        'Now analyzing the data from 2019 and 2020 Asian Crimes, we merge it into a new dataframe')

    bar1 = nineteen_hate[nineteen_hate["Bias-Motivation"] ==
                         "Anti-Asian"].groupby("Borough", as_index=False).size()

    bar2 = twentytwenty_hate[twentytwenty_hate["Bias-Motivation"]
                             == "ANTI-ASIAN"].groupby("Borough", as_index=False).size()

    bar1 = bar1.rename(columns={'size': '2019'})

    bar2 = bar2.rename(columns={'size': '2020'})

    new_df = pd.merge(bar1, bar2, on='Borough', how='outer')

    st.write('To graph this we must fill the null values with 0 and graph the plot')

    new_df.fillna(0)
    new_df.plot.bar(x='Borough')

    st.write(
        '''
                Overall we are able to view that the hate crime associated with the Asian community is higher.

                ## **Further Analysis & Conclusions:**

                ### **Conclusions:**
                Hate Crime for the Asian Community did increase from 2019 to 2020, therefore showing that the Asian community was impacted the most in 2020 and therefore impacting their buisness.

                ### **Further Analysis:**

                One way we can contunie to do a further analysis is by analyzing the boroughs and common zipcodes that were identified in customers survey and compare that to COVID-19 data. By analyzing the behavior we can see the common trends and patterns of where area's got hit the most.

                https://www1.nyc.gov/site/doh/covid/covid-19-data-neighborhoods.page

                Another further analysis that can be done is going back to 2018  and 2017 data to compare larger trends and see where these areas have gotten worse for the Asian community.

                Lastly the further analysis can be done by comparing business traffic in the retail sector around these boroughs that were largely impacted by the Asian community, in the case of 2020 it would be identifying business in Manhattan that are Asian primarly and 2019 analyzing business that are in Brooklyn.
        ''')
