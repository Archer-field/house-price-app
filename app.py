import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("house_price_model.pkl")

st.set_page_config(page_title="House Price Predictor")

st.title("🏠 House Price Prediction App")

st.write("Enter house details to predict price")

area = st.number_input("Area (sqft)", 100, 10000, 1000)
bedrooms = st.number_input("Bedrooms", 1, 10, 2)
bathrooms = st.number_input("Bathrooms", 1, 10, 2)
stories = st.number_input("Stories", 1, 5, 1)
parking = st.number_input("Parking Spaces", 0, 5, 1)

input_data = pd.DataFrame({
    "area": [area],
    "bedrooms": [bedrooms],
    "bathrooms": [bathrooms],
    "stories": [stories],
    "parking": [parking]
})

if st.button("Predict Price"):
    prediction = model.predict(input_data)
    st.success(f"💰 Estimated Price: ₹ {prediction[0]:,.2f}")
