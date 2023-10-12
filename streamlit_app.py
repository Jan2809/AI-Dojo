import streamlit as st
import pandas as pd
import numpy as np

st.title("🏡 California House Price Prediction")
st.subheader("Check out the colab workbook 🔗.")
st.markdown("""
##### A web application for predicting California Housing Prices.
 
This app uses machine learning to predict the price of the house. 
It loads a pre-trained linear regression model, which takes as input various features of the house, 
such as the number of rooms, the number of bedrooms, the population of the house's neighborhood, and the distance to the nearest city. 
The app preprocesses the input data by combining some of the features and adding new features, such as the distance to the nearest city.
""")

option = st.selectbox("Wähle eine Option", ["Option 1", "Option 2", "Option 3"])
st.write("Ausgewählte Option:", option)

df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))

st.dataframe(df)  # Same as st.write(df)
