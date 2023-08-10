import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt
import requests
import snowflake.connector
#st.title('My Parents New Healthy Diner')
st.title('My Mom\'s New Healthy Diner')
st.header('Breakfast Favorites')
st.text('🍞Omega 3 & Blueberry Oatmeal')
st.text('🥗Kale, Spinach & Rocket Smoothie')
st.text('🐔 Hard-Boiled Free-Range Egg')
st.text('🥑🍞Avocado Toast')

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')


# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = st.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show  = my_fruit_list.loc[fruits_selected]
# Display the table on the page.
#st.dataframe(my_fruit_list)
st.dataframe(fruits_to_show)
#st.title('My Mom\'s New Healthy Diner')
st.header('Fruityvice Fruit Advice!')
#import requests
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/Watermelon")
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
#st.text(fruityvice_response.json())

fruit_choice = st.text_input('What fruit would you like information about?','Kiwi')
st.write('The user entered ', fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)


# print user selection on streamlit, with pandas table format.
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
#st.text(fruityvice_normalized)
st.dataframe(fruityvice_normalized) 

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)




