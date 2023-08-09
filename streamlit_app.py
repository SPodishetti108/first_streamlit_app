import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt
import requests as req


st.title('My Mom''s New Healthy Diner')
st.header('Breakfast Menu')
fruityvice_responce = req.get("https://fruityvice.com/api/fruit/watermelon") 
st.text(fruityvice_responce)
