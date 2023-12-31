import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt
import requests
import snowflake.connector
from urllib.error import URLError


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
############################################################################################
def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
  fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
  # write your own comment - what does this do?
  return fruityvice_normalized
############################################################################################
#New sectin to disply fruityvice api respomnce
#st.dataframe(fruityvice_normalized) 
#st.header('Fruityvice Fruit Advice!')

#import requests
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/Watermelon")
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
#st.text(fruityvice_response.json())
st.header('View Our Fruit List - Add your Fruit Favorites!')
try:
  fruit_choice = st.text_input('What fruit would you like information about?') # ,'Kiwi'
  if not fruit_choice:
      st.error("Please select a fruit to get information.")
  else: 
        #st.write('The user entered ', fruit_choice)
        back_from_function = get_fruityvice_data(fruit_choice)
        #fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
        # print user selection on streamlit, with pandas table format.
        #fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
        # write your own comment - what does this do?
        #st.text(fruityvice_normalized)
        #st.dataframe(fruityvice_normalized) 
        st.dataframe(back_from_function) 
except URLError as e:
    streamlit.error()

#Dont run anything past here while we troubleshoot.
#st.stop()

#import snowflake.connector

my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
#st.text("Hello from Snowflake:")
#st.text("The Fruit load list contains:")
my_cnx.close()
st.header("The Fruit load list contains:")
#Snowflake-related functions
################################################################
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("Select * from fruit_load_list")
    return my_cur.fetchall()
################################################################
# Add a button to load the fruit
if st.button('Get fruit load list'):
  my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  my_cnx.close()
  st.dataframe(my_data_rows)
################################################################  
#st.stop()
################################################################
# Allow the end user to add fruits to the list.
def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("insert into fruit_load_list values ('"+ new_fruit + "') ")
    return ( 'Thanks for adding ' + new_fruit )
################################################################    
add_my_fruit = st.text_input('What fruit would you like to add?')
if st.button('Add a fruit to the list'):
  my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
  back_from_button = insert_row_snowflake(add_my_fruit)
  my_cnx.close()
  st.text(back_from_button)
#st.write('Thanks for adding ', add_my_fruit)
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
################################################################ 

################################################################ 







