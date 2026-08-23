import streamlit as st
import pandas as pd
import numpy as np
import joblib


# -----------------------------------
# Load Model and Preprocessor
# -----------------------------------

model = joblib.load(
    "../models/final_churn_model.pkl"
)

preprocessor = joblib.load(
    "../models/preprocessor.pkl"
)

# -----------------------------------
# Page Configuration
# -----------------------------------

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Customer Churn Prediction")
st.write("Enter customer details to predict whether the customer is likely to churn.")


# -----------------------------------
# Customer Information
# -----------------------------------

st.header("Customer Information")

col1, col2 = st.columns(2)

with col1:

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    senior_citizen = st.selectbox(
        "Senior Citizen",
        [0, 1]
    )

    partner = st.selectbox(
        "Partner",
        ["Yes", "No"]
    )

    dependents = st.selectbox(
        "Dependents",
        ["Yes", "No"]
    )

    tenure = st.number_input(
        "Tenure (Months)",
        min_value=0,
        max_value=100,
        value=12
    )

    phone_service = st.selectbox(
        "Phone Service",
        ["Yes", "No"]
    )

    multiple_lines = st.selectbox(
        "Multiple Lines",
        ["Yes", "No", "No phone service"]
    )

    internet_service = st.selectbox(
        "Internet Service",
        ["DSL", "Fiber optic", "No"]
    )


with col2:

    online_security = st.selectbox(
        "Online Security",
        ["Yes", "No", "No internet service"]
    )

    online_backup = st.selectbox(
        "Online Backup",
        ["Yes", "No", "No internet service"]
    )

    device_protection = st.selectbox(
        "Device Protection",
        ["Yes", "No", "No internet service"]
    )

    tech_support = st.selectbox(
        "Tech Support",
        ["Yes", "No", "No internet service"]
    )

    streaming_tv = st.selectbox(
        "Streaming TV",
        ["Yes", "No", "No internet service"]
    )

    streaming_movies = st.selectbox(
        "Streaming Movies",
        ["Yes", "No", "No internet service"]
    )

    contract = st.selectbox(
        "Contract",
        ["Month-to-month", "One year", "Two year"]
    )

    paperless_billing = st.selectbox(
        "Paperless Billing",
        ["Yes", "No"]
    )

    payment_method = st.selectbox(
        "Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ]
    )


monthly_charges = st.number_input(
    "Monthly Charges",
    min_value=0.0,
    value=70.0
)

total_charges = st.number_input(
    "Total Charges",
    min_value=0.0,
    value=840.0
)


# -----------------------------------
# Prediction
# -----------------------------------

if st.button("🔮 Predict Churn"):

    # ContractTenure
    contract_tenure = (
        contract + "_" + str(tenure)
    )

    # Feature Engineering
    tenure_years = tenure / 12

    is_new_customer = int(
        tenure <= 6
    )

    is_long_term_customer = int(
        tenure >= 24
    )

    service_values = [
        online_security,
        online_backup,
        device_protection,
        tech_support,
        streaming_tv,
        streaming_movies
    ]

    service_count = sum(
        value == "Yes"
        for value in service_values
    )

    expected_total_charges = (
        tenure * monthly_charges
    )

    charge_difference = (
        total_charges -
        expected_total_charges
    )

    if tenure > 0:
        average_monthly_charge = (
            total_charges / tenure
        )
    else:
        average_monthly_charge = 0


    # -----------------------------------
    # Create DataFrame
    # -----------------------------------

    customer = pd.DataFrame([{
        "gender": gender,
        "SeniorCitizen": senior_citizen,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "PhoneService": phone_service,
        "MultipleLines": multiple_lines,
        "InternetService": internet_service,
        "OnlineSecurity": online_security,
        "OnlineBackup": online_backup,
        "DeviceProtection": device_protection,
        "TechSupport": tech_support,
        "StreamingTV": streaming_tv,
        "StreamingMovies": streaming_movies,
        "Contract": contract,
        "PaperlessBilling": paperless_billing,
        "PaymentMethod": payment_method,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges,
        "TenureYears": tenure_years,
        "IsNewCustomer": is_new_customer,
        "IsLongTermCustomer": is_long_term_customer,
        "ServiceCount": service_count,
        "ExpectedTotalCharges": expected_total_charges,
        "ChargeDifference": charge_difference,
        "AverageMonthlyCharge": average_monthly_charge,
        "ContractTenure": contract_tenure
    }])


    # -----------------------------------
    # Preprocessing
    # -----------------------------------

    customer_processed = preprocessor.transform(
        customer
    )


    # -----------------------------------
    # Prediction
    # -----------------------------------

    prediction = model.predict(
        customer_processed
    )[0]

    probability = model.predict_proba(
        customer_processed
    )[0, 1]


    # -----------------------------------
    # Result
    # -----------------------------------

    st.header("Prediction Result")

    if prediction == 1:

        st.error("⚠️ Customer is likely to CHURN")

    else:

        st.success("✅ Customer is likely to NOT CHURN")

    st.metric(
        "Churn Probability",
        f"{probability:.2%}"
    )