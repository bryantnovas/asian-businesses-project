from components import census as cs
from components import sba as sd
from components import google_news as gn
from components import hate_crime as hc
import streamlit as st

page_componets = {
    "Census Data Analisys": cs,
    "SBA Data Analisys": sd,
    "Google News Analisys": gn,
    "Hate Crime Analisys": hc
}

st.set_page_config(layout="wide")
st.set_option('deprecation.showPyplotGlobalUse', False)

st.sidebar.title('Navigation')
selection = st.sidebar.selectbox("Go to", list(page_componets.keys()))
page = page_componets[selection]
page.app()
