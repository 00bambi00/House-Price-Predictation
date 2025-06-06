import streamlit as st
import pickle
import pandas as pd
import matplotlib.pyplot as plt

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title('House Price Prediction with AI')

living_space = st.number_input('Living Space (square meters)', min_value=10, max_value=1000, value=100)
bedroom_number = st.slider('Number of Bedrooms', 0, 10, 3)
bathroom_number = st.slider('Number of Bathrooms', 0, 10, 2)
city = st.text_input('City / District', 'Bangkok')
property_type = st.selectbox('Property Type', ['Detached House / Single-family House', 'Townhouse', 'Condominium'])

input_df = pd.DataFrame({
    'living_space': [living_space],
    'bedroom_number': [bedroom_number],
    'bathroom_number': [bathroom_number],
    'city': [city],
    'property_type': [property_type]
})

input_df = pd.get_dummies(input_df)

model_cols = model.feature_names_in_ if hasattr(model, 'feature_names_in_') else input_df.columns
st.write("Model columns:", model_cols)

for col in model_cols:
    if col not in input_df.columns:
        input_df[col] = 0
input_df = input_df[model_cols]

st.write("Input DataFrame:", input_df)

if st.button('Predict House Price'):
    price_pred = model.predict(input_df)[0]
    st.success(f'Estimated House Price: {price_pred:,.2f} Baht')

    fig, ax = plt.subplots()
    ax.bar(['Estimated Price'], [price_pred], color='skyblue')
    ax.set_ylabel('Price (Baht)')
    st.pyplot(fig)

    result = f'House Price: {price_pred:,.2f} Baht\nProperty information: Size {living_space} sqm, Bedroom {bedroom_number}, Bathroom {bathroom_number}, City {city}, Property Type {property_type}'
    st.download_button('Download Result', result, file_name='prediction_result.txt')

