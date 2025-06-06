# 🏠 House Price Prediction with AI

This is a machine learning project that predicts the estimated market price of a house based on basic property features such as size, number of bedrooms/bathrooms, location, and property type.

The web interface is built using [Streamlit](https://streamlit.io), allowing users to interact with the model in real time.

---

## 🔍 Features

- Predict house price based on:
  - Living space (sqm)
  - Number of bedrooms
  - Number of bathrooms
  - City/District
  - Property type (Detached, Townhouse, Condo)
- Real-time prediction and bar chart visualization
- Downloadable result summary

---

## 📂 Project Structure

thai_housing_prediction_project/
├── app.py # Streamlit app
├── model.pkl # Trained machine learning model (pickle)
├── data/
│ └── ddproperty_2022.csv # Raw data used for model training (not included in repo)
├── house_price_prediction.ipynb # Training and evaluation notebook
├── requirements.txt # Python dependencies
└── README.md # This file


---

## 🧠 Model Info

- Algorithm: Gradient Boosting Regressor (can be replaced/updated)
- Evaluation:
  - RMSE ≈ 27,999,707 THB
  - R² Score ≈ 0.93
- Preprocessing: Basic one-hot encoding on categorical features

---

here is a link to https://house-price-predictation-a5wbb2cwtwb9m67atjhrt4.streamlit.app 
