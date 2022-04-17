import pandas as pd
import numpy as np
import altair as alt
import streamlit as st

#printing the title of the webapp
st.title('World Bank Data - India')

#importing the csv file
India=pd.read_csv("World_Bank_india2.csv")
India.set_index('years',inplace=True)
India.T
st.table(India)
