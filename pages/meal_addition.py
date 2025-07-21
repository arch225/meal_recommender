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

edited_df = st.data_editor(select_meal(meal_sel), num_rows="dynamic", use_container_width=True)
if meal_sel == "Breakfast":
     with pd.ExcelWriter('data/food_options.xlsx', mode='a', if_sheet_exists='replace') as writer:
        edited_df.to_excel(writer, sheet_name='breakfast', index=False)
elif meal_sel == "Lunch":
     with pd.ExcelWriter('data/food_options.xlsx', mode='a', if_sheet_exists='replace') as writer:
        edited_df.to_excel(writer, sheet_name='lunch', index=False)
elif meal_sel == "Dinner":
    with pd.ExcelWriter('data/food_options.xlsx', mode='a', if_sheet_exists='replace') as writer:
        edited_df.to_excel(writer, sheet_name='dinner', index=False)


# Show edited result
st.subheader("Updated DataFrame:")
