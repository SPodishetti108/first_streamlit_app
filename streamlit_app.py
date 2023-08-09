import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt
import requests


st.title('My Mom''s New Healthy Diner')
st.header('Breakfast Menu')
#import requests
fruityvice_response = requests.get('https://fruityvice.com/api/fruit/watermelon')
st.text(fruityvice_response)
