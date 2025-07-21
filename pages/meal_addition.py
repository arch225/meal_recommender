import streamlit as st
import pandas as pd

def select_meal(meal):
    if meal == "Breakfast":
        df=pd.read_excel("data/food_options.xlsx", sheet_name="breakfast")
        return df
    elif meal == "Lunch":
        df=pd.read_excel("data/food_options.xlsx", sheet_name="lunch")
        return df
    elif meal == "Dinner":
        df=pd.read_excel("data/food_options.xlsx", sheet_name="lunch")
        return df

meal_sel=st.selectbox("Select a meal", ["Breakfast", "Lunch", "Dinner"])

st.dataframe(select_meal(meal_sel))