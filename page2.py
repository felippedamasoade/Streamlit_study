import pandas as pd
import streamlit as st
import numpy as np


st.markdown("#page two")
st.sidebar.markdown("#Page two")

x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)


