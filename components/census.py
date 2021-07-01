import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns


def app():
    st.write(
        ''' 
          ## **Introduction**

          This Census data focuses on sales data of various business industries throughout the United States, from 1992 to 2021. We focused on the last year and five months of the data(January 2020 to May 2021) in order to examine how sales faired during the coronavirus pandemic.

          Hypothesis: We hypothesize that the amount of overall sales will decrease when the pandemic became widespread in 2020, and many businesses were forced to close and/or shift their business model.

          ### **Methods**

          All of the data had to be separated into two csvs' using google sheets. From there, both csvs were merged together. Results were then filtered by time period and the amount of sales that occurred within that time period.
     ''')

    df = pd.read_csv('./datasets/MARTS-mf.csv')
    st.dataframe(df)

    time_periods = pd.read_csv('./datasets/TIME PERIODS.CSV')
    st.dataframe(time_periods)

    categories = pd.read_csv('./datasets/Categories.csv')
    st.dataframe(categories)

    result = pd.merge(df, time_periods, on='per_idx')
    st.dataframe(result)

    result = pd.merge(
        result, categories[['cat_idx', 'cat_desc']], on='cat_idx')
    st.dataframe(result)

    result.drop(columns=['geo_idx', 'et_idx'])

    st.write('Time period (2020-2021) values were isolated here by per_idx.')

    result = result[result["per_idx"] > 336]
    st.dataframe(result)

    st.write('Business type was isolated here by the category index(cat_idx).')

    result = result[(result["cat_idx"] == 1) | (result["cat_idx"] == 5) | (result["cat_idx"] == 11) | (result["cat_idx"] == 12)
                    | (result["cat_idx"] == 13) | (result["cat_idx"] == 15) | (result["cat_idx"] == 17) | (result["cat_idx"] == 20) | (result["cat_idx"] == 21)]
    st.dataframe(result)

    st.write(
        'The sum of values was taken for each type of business from January 2020 until May 2021.')

    grouped_df = result.groupby(
        ['per_name', 'cat_desc'], as_index=False, sort=False)['val'].sum()
    st.dataframe(grouped_df)

    st.write('Each group was set to a variable in order to create the graphs.')

    time = grouped_df["per_name"].unique()
    st.dataframe(time)

    cat = grouped_df["cat_desc"].unique()
    st.dataframe(cat)

    st.write(
        '''
          ## **Analysis Section** 

          Retail Trade, and Retail Trade and Food Services entities had the highest amount of sales overall, as evidenced in the following line graph. The remainder of the businesses, achieved an amount of sales that were below a .2 value. There appears to be a .6 gap in sales values between Retail Trade, Retail Trade and Food Services, and the rest of the business types.
       ''')

    with sns.axes_style("white"):
        plt.figure(figsize=(30, 25))
        color_list = ['#291F1E', '#031A6B', '#EF709D', '#E2EF70',
                      '#70E4EF', '#75F4F4', '#90E0F3', '#B8B3E9', '#D999B9', '#D17B88']
        for idx, category in enumerate(cat):
            x = grouped_df["per_name"].unique()
            y = grouped_df[grouped_df["cat_desc"] == category]["val"]
            plt.xlabel("Time Period", fontsize=30)
            plt.ylabel("Sales", fontsize=30)
            plt.title("Small Business Sales", fontsize=30)
            plt.plot(x, y, label=category, color=color_list[idx])
        plt.xticks(fontsize=25)
        plt.xticks(rotation=45)
        plt.yticks(fontsize=25)
        plt.legend(prop={'size': 20})
    st.pyplot()

    with sns.axes_style("white"):
        plt.figure(figsize=(30, 25))
        color_list = ["#EAC435", "#345995", "#03CEA4", "#FB4D3D",
                      "#CA1551", "#7F95D1", "#FF82A9", "#FFC0BE", "#FFEBE7", "#33032F"]
        for idx, category in enumerate(cat):
            x = grouped_df["per_name"].unique()
            y = grouped_df[grouped_df["cat_desc"] == category]["val"]
            plt.xlabel("Time Period", fontsize=30)
            plt.ylabel("Sales", fontsize=30)
            plt.title("Small Business Sales", fontsize=30)
            plt.bar(x, y, label=category, color=color_list[idx])
        plt.xticks(fontsize=25)
        plt.xticks(rotation=45)
        plt.yticks(fontsize=25)
        plt.legend(prop={'size': 20})
    st.pyplot()

    st.write('It appears that Retail Trade and Food Services industry had the highest amount of sales throughout the pandemic, but saw a steep decline in the months of March and April in 2020.')

    st.dataframe(grouped_df[grouped_df['cat_desc'] ==
                 '44X72: Retail Trade and Food Services'])

    st.write('Sales for Food Services and Drinking Places took a dramatic nosedive in March and April of 2020, but began increasing in May of 2020, then fluctuating in the proceeding months.')

    st.dataframe(grouped_df[grouped_df['cat_desc'] ==
                 '722: Food Services and Drinking Places'])

    st.write('In Food and Beverage Stores, sale values appeared to hover around similiar values. March and April 2020 values seemed to increase from January and February of that year then fluctuate around the 140,000.0 mark, finishing at an increased value of 150,486.2 in May of 2021.')

    st.dataframe(grouped_df[grouped_df['cat_desc']
                 == '445: Food and Beverage Stores'])

    st.write('Sales beginning in January 2020 in Health and Personal Stores, started off small to begin with, and hovered around the same values throughout the year into May 2021.')

    st.dataframe(grouped_df[grouped_df['cat_desc'] ==
                 '446: Health and Personal Care Stores'])

    st.write('Sales within Clothing and Clothing Accessory Stores  went into a steep decline of 16,930.2 to 5447.5 in April of 2020, then increased by almost half in the upcoming months(June to August 2020), steadily increasing until January of 2021, where it fell by 15,340.2 . From January of 2021 to May of 2021, clothing store sales increased by a total of approximately 14,000.0.')

    st.dataframe(grouped_df[grouped_df['cat_desc'] ==
                 '448: Clothing and Clothing Access. Stores'])

    st.write('General Merchandise Stores sales remained steady overall, but showed a decrease between the months of March 2020 and April 2020 of 17,720.9. Sales fluctuated in the proceeding months, decreasing again in the months between December 2020 and February 2020.')

    st.dataframe(grouped_df[grouped_df['cat_desc'] ==
                 '452: General Merchandise Stores'])

    st.write('Nonstore Retailers appears to have increased sales overall from January 2020, its highest point of sales being December of 2020, with a value of 179640.4. ')

    st.dataframe(grouped_df[grouped_df['cat_desc']
                 == '454: Nonstore Retailers'])

    st.write(
        '''
          ## **Results**

          My findings indicate that overall Retail Trade, Retail Trade and Food Services had the highest amount of sales in the past year(January 2020 to May 2021). One commonality among many of the different business types is that in the months between March 2020 and April 2020, sales saw a decline. Another commonality is that some of the business types also saw a decline in sales between the months of December 2020 and January 2021.

          ## **Conclusion**

          As expected, the outbreak of the coronavirus pandemic and the subsequent lockdown had a major impact on sales, especially in the months of March and April of 2020. The industries that faired the best was Retail, Retail Trade and Food Services while Health and Personal Care stores faired the least. There was a significant difference between the Retail, Retail Trade and Food Services and the other business industries covered in this study. Perhaps more investigation can be done on why there was such a significant gap between those industries.

          ## **Appendix**

          Data collected from the United States Census Bureau: https://www.census.gov/econ/currentdata/datasets/index 
     ''')
