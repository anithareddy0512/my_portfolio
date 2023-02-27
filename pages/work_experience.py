import streamlit as st
import pandas as pd
from PIL import Image
from pathlib import Path
#import plotly.express as px
import os

st.latex("Total Experience: 5.6    years")
st.write('\n')
st.write('\n')
x = st.button("Industrial Experience")
if x==True:
    st.write(
        ":point_right: 3 years Experience as Data Analyst at Sparkynode Analytics, Hyderabad."
    )
    st.balloons()
st.write('\n')
st.write('\n')
y = st.button("Teaching Experience")
if y==True:
    st.write(
        ":point_right: 2.6 years Experience as Assistant Professor at Vignan's University, Guntur."
    )
    st.balloons()
st.write('\n')
st.write('\n')
z = st.button("Internship")
if z==True:
    st.write("""
        :point_right: 1 years Internship in Emission Business Unit at Cummins India Limited, Pune
        """
    )
    st.write(
        ":point_right: Selected for three months Data Science Internship at Innomatics Research Labs, Hyderabad."
    )
    st.snow()

