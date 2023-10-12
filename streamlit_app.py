import streamlit as st
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu

#menu
selected2 = option_menu(None, ["Home", "Upload", "Tasks", 'Settings'], 
    icons=['house', 'cloud-upload', "list-task", 'gear'], 
    menu_icon="cast", default_index=0, orientation="horizontal")
selected2



st.title("🏡 California House Price Prediction")
st.subheader("Check out the colab workbook 🔗.")
st.markdown("""
##### A web application for predicting California Housing Prices.
 
This app uses machine learning to predict the price of the house. 
It loads a pre-trained linear regression model, which takes as input various features of the house, 
such as the number of rooms, the number of bedrooms, the population of the house's neighborhood, and the distance to the nearest city. 
The app preprocesses the input data by combining some of the features and adding new features, such as the distance to the nearest city.
""")

# Lese den Datensatz aus einer CSV-Datei
data = pd.read_csv('housing_new.csv')

# Anzeige des Datensatzes als Tabelle
st.write("Hier ist der Datensatz als Tabelle:")
st.table(data.head(21))
