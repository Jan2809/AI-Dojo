import streamlit as st
from streamlit_extras.stoggle import stoggle

st.title("🏡 California House Price Prediction")
st.subheader("Check out the colab workbook 🔗.")
st.markdown("""
##### A web application for predicting California Housing Prices.
 
This app uses machine learning to predict the price of the house. 
It loads a pre-trained linear regression model, which takes as input various features of the house, 
such as the number of rooms, the number of bedrooms, the population of the house's neighborhood, and the distance to the nearest city. 
The app preprocesses the input data by combining some of the features and adding new features, such as the distance to the nearest city.
""")

stoggle(
    "Click me!",
    """🥷 Surprise! Here's some additional content""",
)
