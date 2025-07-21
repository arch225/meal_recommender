
import streamlit as st
import pandas as pd
from datetime import datetime,timedelta

# Set page title
st.title("Meal Planner")

# Date input
selected_date = st.date_input("Select a date", datetime.now()+timedelta(days=1))

# Calculate day of week
day_of_week = selected_date.strftime("%A")
st.write(f"Selected day: {day_of_week}")
df_breakfast=pd.read_excel('data/food_options.xlsx',sheet_name='breakfast')
df_lunch=pd.read_excel('data/food_options.xlsx',sheet_name='lunch')
df_dinner=pd.read_excel('data/food_options.xlsx',sheet_name='dinner')

st.divider()
st.write("### Breakfast Options")
brf=df_breakfast[df_breakfast['day']==day_of_week]['breakfast_option'].iloc[0]
b_select=st.selectbox("Select Breakfast Option", options=df_breakfast['breakfast_option'].tolist(),index=df_breakfast['breakfast_option'].tolist().index(brf))
brf_desc=df_breakfast[df_breakfast['breakfast_option']==b_select]['breakfast_description'].iloc[0]
st.write(brf_desc)

st.divider()

st.write("### Lunch Options")
lnch=df_lunch[df_lunch['day']==day_of_week]['lunch'].iloc[0]
l_select=st.selectbox("Select Lunch Option", options=df_lunch['lunch'].tolist(),index=df_lunch['lunch'].tolist().index(lnch))
lnch_desc=df_lunch[df_lunch['lunch']==l_select]['lunch_description'].iloc[0]
st.write(lnch_desc)
st.divider()

st.write("### Dinner Options")
dnnr=df_dinner[df_dinner['day']==day_of_week]['dinner'].iloc[0]
d_select=st.selectbox("Select Dinner Option", options=df_dinner['dinner'].tolist(),index=df_dinner['dinner'].tolist().index(dnnr))
dnnr_desc=df_dinner[df_dinner['dinner']==d_select]['dinner_description'].iloc[0]
st.write(dnnr_desc)
st.divider()

if st.button("Submit Meal Plan"):

    # Create DataFrame with meal selections
    meal_data = pd.DataFrame({
        'Date': [selected_date],
        'Day': [day_of_week],
        'Breakfast': [b_select],
        'Lunch': [l_select], 
        'Dinner': [d_select]
    })
    
    try:
        # Try to read existing data
        existing_data = pd.read_excel('data/food_options.xlsx', sheet_name='meal_plans')
        # Append new data
        updated_data = pd.concat([existing_data, meal_data], ignore_index=True)
    except:
        # If sheet doesn't exist, use new data
        updated_data = meal_data
        
    # Write to Excel
    with pd.ExcelWriter('data/food_options.xlsx', mode='a', if_sheet_exists='replace') as writer:
        updated_data.to_excel(writer, sheet_name='meal_plans', index=False)
    
    st.success("Meal plan saved successfully!")

