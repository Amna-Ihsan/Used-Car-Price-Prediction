import streamlit as st
import pandas as pd
import joblib

# load saved files
model = joblib.load("lasso_model.pkl")
scaler = joblib.load("scaler.pkl")
fuel_encoder = joblib.load("fuel_encoder.pkl")
seller_encoder = joblib.load("seller_encoder.pkl")
transmission_encoder = joblib.load("transmission_encoder.pkl")

# title
st.title("Used Car Price Prediction App")
st.write("Enter car details to predict the selling price")

# user input
year = st.number_input("Year",min_value=2000, max_value=2026,value=2014)
present_price = st.number_input("Present Price",min_value=0.0,value=5.59)
kms_driven = st.number_input("Km Driven",min_value=0,value=27000)

fuel_type = st.selectbox("Fuel Type", list(fuel_encoder.classes_))
seller_type  = st.selectbox("Seller Type", list(seller_encoder .classes_))
transmission  = st.selectbox("Transmission ", list(transmission_encoder.classes_))

owner = st.number_input("Owner", min_value=0, max_value=5, value=0)

# Predict button
if st.button("Predict Selling Price"):


    input_data = pd.DataFrame({
        "Year": [year],
        "Present_Price": [present_price],
        "Kms_Driven" : [kms_driven],
        "Fuel_Type":[fuel_type],
        "Seller_Type":[seller_type],
        "Transmission":[transmission],
        "Owner": [owner]
                })

    # Encode Categorical values
    input_data["Fuel_Type"] = fuel_encoder.transform(input_data["Fuel_Type"])
    input_data["Seller_Type"] = seller_encoder.transform(input_data["Seller_Type"])
    input_data["Transmission"] = transmission_encoder.transform(input_data["Transmission"])

    # scale input
    input_data_scaled = scaler.transform(input_data)

    # Predict
    prediction = model.predict(input_data_scaled)
    st.success(f"Predicted Selling Price: {prediction[0]:.2f} lakhs")