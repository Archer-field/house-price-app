import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("house_price_model.pkl")

st.set_page_config(page_title="House Price Predictor")

st.title("🏠 House Price Prediction App")

st.write("Enter house details to predict price")

# USER INPUTS
carpet = st.number_input("Carpet Area", 100, 10000, 1000)
bathroom = st.number_input("Bathrooms", 1, 10, 2)
balcony = st.number_input("Balconies", 0, 5, 1)
parking = st.number_input("Car Parking", 0, 5, 1)

# DataFrame
input_data = pd.DataFrame({
    "Carpet Area": [carpet],
    "Bathroom": [bathroom],
    "Balcony": [balcony],
    "Car Parking": [parking]
})

# Prediction
if st.button("Predict Price"):
    prediction = model.predict(input_data)

    price_lakh = prediction[0] / 100000

    st.success(f"💰 Estimated Price: ₹ {price_lakh:.2f} Lakhs")
