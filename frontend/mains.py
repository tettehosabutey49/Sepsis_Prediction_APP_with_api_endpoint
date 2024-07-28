import streamlit as st
import requests
import joblib

## defining backend URL

backend = "http://127.0.0.1:8000/"

xgboost_end_point = "http://api:8080/predict_sepsis_XGBoost_prediction_post"
linear_regressor_end_point = "http://api:8080/predict_sepsis_Logistic_Regressor_post"

st.set_page_config(
    page_title="Prediction",
    layout="wide",
    page_icon="🔮"
)

def show_form():
    st.title("Sepsis Prediction App")

    with st.form("input-features"):
    
        st.header("Input Features")
                  
        col1, col2, col3 = st.columns(3)

        with col1: 
            prg = st.number_input("Plasma Glucose", min_value=0.0, step=1.0, key="Plasma Glucose")
            PL = st.number_input("Blood work results-1", min_value=0, step=1, key="Blood work results")
            PR = st.number_input("Blood Pressure", min_value=0, step=1, key="Blood Pressure")

        with col2:
            SK = st.number_input("Blood work result-2", min_value=0.0, step=1.0, key="Blood work result-2")
            TS = st.number_input("Blood work result-3", min_value=0.0, step=1.0, key="Blood work result-3")
            M11 = st.number_input("Body Mass Index", min_value=0.0, step=1.0, key="Body mass index")
        
        with col3:
            BD2 = st.number_input("Blood Work Result-4", min_value=0.0, step=1.0, key="Blood Work Result-4")
            Age = st.number_input("Patient Age", min_value=0.0, step=1.0, key="Patient Age")
            Insurance = st.selectbox("Does Patient have health insurance?", ["Yes", "No"])
        
        user_choice = st.selectbox("Select a model to use", options=["XGBoost🚀", "Logistic_Regressor"], key="selected_model")

        if st.form_submit_button("Predict Sepsis"):
            input_data = {
                "PRG": prg,
                "PL": PL,
                "PR": PR,
                "SK": SK,
                "TS": TS,
                "M11": M11,
                "BD2": BD2,
                "Age": Age,
                "Insurance": Insurance
            }

            if user_choice == "XGBoost🚀":
                response = requests.post(f"{backend}/XGBoost_prediction", json=input_data)
                #response = requests.post(f"{xgboost_end_point}", json=input_data)
            else: 
                response = requests.post(f"{backend}/Logistic_Regressor", json=input_data)
                #response = requests.post(f"{linear_regressor_end_point}", json=input_data)

            if response.status_code == 200:
                prediction = response.json()["Prediction"]
                probability = response.json()["Probability"]
                st.success(f'The Predicted Sepsis status is: {prediction}')
                st.success(f"The probability is {(round(float(probability.strip('%')) / 100, 2))*100}%")
            else: 
                st.error(f'Error: {response.json()["detail"]}')

show_form()


## streamlit run mains.py