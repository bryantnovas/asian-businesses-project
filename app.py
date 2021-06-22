import components.census_data as cs
import components.sba_data as sd
import streamlit as st

page_componets = {
  "Census Data": cs,
  "SBA Data": sd
    
}

st.set_page_config(layout="wide")

st.sidebar.title('Navigation')
selection = st.sidebar.selectbox("Go to", list(page_componets.keys()))
page = page_componets[selection]
page.app()