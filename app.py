import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the saved model and scaler
model = joblib.load('crop_yield_model.pkl')
scaler = joblib.load('scaler.pkl')

# Page Config
st.set_page_config(page_title="Agri-Yield Predictor", layout="centered")

# Custom CSS for a Green "Sustainable" Look
st.markdown("""
    <style>
    .main { background-color: #f0f5f0; }
    h1 { color: #2e7d32; }
    .stButton>button { background-color: #2e7d32; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("🌱 Sustainable Crop Yield Predictor")
st.write("Optimize agricultural output using Machine Learning for a greener future.")

# UI Sections
st.sidebar.header("Input Environmental Factors")

def user_input_features():
    rainfall = st.sidebar.slider('Rainfall (mm)', 50.0, 300.0, 150.0)
    temp = st.sidebar.slider('Temperature (°C)', 15.0, 45.0, 25.0)
    fertilizer = st.sidebar.slider('Fertilizer (kg)', 50.0, 250.0, 120.0)
    area = st.sidebar.number_input('Area (Hectare)', 1.0, 20.0, 5.0)
    
    data = {'Rainfall_mm': rainfall,
            'Temperature_C': temp,
            'Fertilizer_kg': fertilizer,
            'Area_hectare': area}
    features = pd.DataFrame(data, index=[0])
    return features

input_df = user_input_features()

st.subheader('Selected Input Parameters')
st.write(input_df)

if st.button('Predict Yield'):
    # Scale inputs
    scaled_input = scaler.transform(input_df)
    
    # Prediction
    prediction = model.predict(scaled_input)
    
    # Result Display
    st.success(f"### Predicted Yield: {prediction[0]:.2f} Ton/Hectare")
    
    # Sustainability Tip
    st.info("**Sustainability Insight:** Based on your inputs, ensure localized irrigation to reduce water waste if rainfall is below 100mm.")

st.markdown("---")
st.caption("Developed for Sustainability & Green Skilling Competition 2024")