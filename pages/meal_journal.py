import streamlit as st
import pandas as pd

df=pd.read_excel('data/food_options.xlsx',sheet_name='meal_plans')
st.dataframe(df)