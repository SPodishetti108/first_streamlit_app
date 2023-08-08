import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('My Parents New Healthy Diner')

st.header('Breakfast Menu')
st.subheader("South Indian : ")
st.text('idli \n Dosa \n Wada \n  :)')

st.subheader("North Indian : ")
st.text('Wada Paw \n Samosa \n Paw Baji \n  :)')

# Other Streamlist functions
st.write("Hello, Streamlit!")
st.write(12345)
st.write(["apple", "banana", "orange"])

st.text("This is some text.")

st.markdown("## This is a Markdown Heading")
st.markdown("This is **bold** and *italic* text.")


data = pd.DataFrame({"Name": ["Alice", "Bob", "Charlie"], "Age": [25, 30, 28]})

st.text("This is pandas dataframe display.")
st.dataframe(data)

st.text("This is pandas table display")
st.table(data)

plt.plot([1, 2, 3, 4])
st.pyplot(plt)

#button_clicked = st.button("Click Me")
#if button_clicked:
#    st.write("Button was clicked!")


#print("Gam Ganesha")
