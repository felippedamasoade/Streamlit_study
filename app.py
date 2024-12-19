import pandas as pd
import streamlit as st
import numpy as np

st.markdown("#First page")
st.sidebar.markdown("First Page")


#Gerando dados
dataframe = np.random.rand(10,20)
#Plotando DataFrame no Streamlit
dataframe1 = pd.DataFrame(
    np.random.rand(10,20),
    columns=('col %d' % i for i in range(20))
)



#Plotando DataFrame no Streamlit
dataframe2 = pd.DataFrame(
    np.random.rand(10,20),
    columns=('col %d' % i for i in range(20))
)






col1 , col2, col3 = st.columns(3)

with col1:
    st.header("First DataFrame")
    st.dataframe(dataframe)

with col2:
    st.header("Second DataFrame")
    ##O método .style.highlight_max(axis=0) aplica um estilo ao DataFrame para destacar (visualmente) os maiores valores em cada coluna (axis=0).
    st.dataframe(dataframe1.style.highlight_max(axis=0))
with col3:
    st.header("Third")
    st.table(dataframe2)

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)