import streamlit as st
import pandas as pd
from PIL import Image
from pathlib import Path
#import plotly.express as px
import os

# path of the picture
base_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
image_ = base_dir / "resources" / "anitha.jpg"
img = Image.open(image_)
col1,col2 = st.columns(2,gap="small")
with col1:
    st.image(img, width=300)
with col2: 
    st.subheader("B. Anitha Reddy :woman: ")
    st.write("""
        To be associated with a progressive organization that 
        gives me scope to apply my knowledge and skils to work
        towards the growth of the organization and me.
    """)
    st.write("""
             :pushpin: Data science Intern | Data Science Enthusiast | Assistant Professor 
             """)
    st.write(":email: anithareddy.bogasamudram@gmail.com")
st.write("Follow me on:")
st.write(":link: https://www.linkedin.com/in/anitha-reddy-bogasamudram-9b8b16266/")
st.write(":link: https://github.com/anithareddy0512")
