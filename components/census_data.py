import streamlit as st
import pandas as pd
def app():
  st.markdown("""
    ## **Introduction**

    This Census data focuses on sales data of various business industries throughout the United States, from 1992 to 2021. We focused on the last year and five months of the data(January 2020 to May 2021) in order to examine how sales faired during the coronavirus pandemic.
  
    ## **Methods**

    All of the data had to be separated into two csvs' using google sheets. From there, both csvs were merged together. Results were then filtered by time period and the amount of sales that occurred within that time period.
  
  """)
  df = pd.read_csv('./datasets/MARTS-mf.csv')
  st.dataframe(df)