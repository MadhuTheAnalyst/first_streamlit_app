import streamlit
import pandas as pd
streamlit.title('My parents new healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('🥣 omega 3 and blueberry oatmeal')
streamlit.text('🥗 kale,spinach and rocket smoothie')
streamlit.text('🐔Hard Boiled free range egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlist.dataframe(my_fruit_list)
