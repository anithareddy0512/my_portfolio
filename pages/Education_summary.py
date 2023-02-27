import streamlit as st
import pandas as pd
from PIL import Image
from pathlib import Path
#import plotly.express as px
import os

st.subheader(":blue Education Details :open_book:")
st.write('\n')
study = {
    "Master's": "NITW Warangal, Automobile Engineering, (2014-16)",
    "Bachelor's": "RVR&JC College of Engineering, Mechanical Engineering, (2009-2013)",
    "HSC": "Guntur Vikas Junior college, (2007-2009)",
    "SSC": "SSSM, Podili       (2006-2007)"  
}
cols = st.columns(len(study),gap="large")
for index, (name, details) in enumerate(study.items()):
    cols[index].success(f"{name}")
    cols[index].info(f"{details}")

 
