import streamlit as st
import pandas as pd


# データ分析関連
st.subheader('データ分析関連')
df = pd.read_csv('.\data\平均気温.csv', index_col='月')
#st.dataframe(df)
#st.table(df)
st.line_chart(df)
st.bar_chart(df['2021年'])
