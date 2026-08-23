# Telco Customer Churn Prediction

## 📌 Project Overview

This project focuses on predicting customer churn in the telecom industry using Machine Learning.

Customer churn refers to customers leaving or discontinuing a company's services. Predicting churn can help businesses identify customers who are more likely to leave and support better customer retention.

This project includes data preprocessing, feature engineering, model training, model evaluation, customer churn prediction, and a Streamlit web application for making predictions on new customers.

---

## 🎯 Project Objective

The main objectives of this project are:

- Predict whether a customer is likely to churn.
- Identify customers who are at risk of leaving.
- Perform data preprocessing and feature engineering.
- Train and evaluate a Machine Learning model.
- Handle class imbalance during model development.
- Provide churn probability for a new customer.
- Build an interactive Streamlit application for prediction.

---

## 📂 Project Structure

```text
Telco Customer Churn/
│
├── app/
│   ├── app.py
│   └── templates/
│
├── data/
│
├── models/
│   ├── final_churn_model.pkl
│   └── preprocessor.pkl
│
├── notebooks/
│   ├── 05_preprocessing.ipynb
│   ├── 06_model_training.ipynb
│   ├── 07_model_evaluation.ipynb
│   └── 08_prediction.ipynb
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Joblib
- Streamlit

---

## ⚙️ Machine Learning Workflow

The project follows these steps:

1. Data understanding
2. Exploratory Data Analysis (EDA)
3. Data cleaning
4. Feature engineering
5. Train-test split
6. Feature preprocessing
7. Model training
8. Model evaluation
9. Customer churn prediction
10. Streamlit application

---

## 🔧 Feature Engineering

Additional features were created to help the model better understand customer behaviour, tenure, service usage, and billing information.

The engineered features include:

- `TenureYears`
- `IsNewCustomer`
- `IsLongTermCustomer`
- `ServiceCount`
- `ExpectedTotalCharges`
- `ChargeDifference`
- `AverageMonthlyCharge`
- `ContractTenure`

---

## 🤖 Machine Learning Model

The project uses **Logistic Regression** for customer churn prediction.

The target variable is:

- `0` → No Churn
- `1` → Churn

The dataset contains more No Churn customers than Churn customers, so class imbalance was considered during model development.

A balanced Logistic Regression model was also used by applying class weights to give more importance to the minority Churn class.

---

## 📊 Model Performance

The Logistic Regression model achieved the following results on the test dataset:

| Metric | Score |
|---|---:|
| Accuracy | 80.27% |
| Precision | 66.33% |
| Recall | 52.14% |
| F1 Score | 58.38% |
| ROC-AUC | 84.41% |

### Classification Report

| Class | Precision | Recall | F1-Score |
|---|---:|---:|---:|
| No Churn | 0.84 | 0.90 | 0.87 |
| Churn | 0.66 | 0.52 | 0.58 |

### Confusion Matrix

```text
[[936   99]
 [179  195]]
```

The ROC-AUC score of **84.41%** indicates that the model has good ability to distinguish between Churn and No Churn customers.

---

## 🌐 Streamlit Application

The project includes a Streamlit web application for making predictions on new customers.

The application allows users to enter customer information such as:

- Gender
- Senior Citizen
- Partner
- Dependents
- Tenure
- Phone Service
- Multiple Lines
- Internet Service
- Online Security
- Online Backup
- Device Protection
- Tech Support
- Streaming TV
- Streaming Movies
- Contract
- Paperless Billing
- Payment Method
- Monthly Charges
- Total Charges

The application provides:

- Churn / No Churn prediction
- Churn probability

---

## 📌 Example Prediction

Example output from the application:

```text
Prediction: No Churn
Churn Probability: 1.88%
```

A churn probability of **1.88%** indicates a relatively low probability of churn for the given customer based on the model prediction.

---

## ▶️ How to Run the Project

### 1. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 2. Run the Streamlit Application

From the project root directory, run:

```bash
streamlit run app/app.py
```

The application will open in the browser.

---

## 📁 Important Files

### `app/app.py`

Contains the Streamlit application used for customer churn prediction.

### `models/final_churn_model.pkl`

Contains the trained Machine Learning model.

### `models/preprocessor.pkl`

Contains the preprocessing pipeline used to transform customer data before prediction.

### `notebooks/`

Contains the notebooks used for data preprocessing, model training, model evaluation, and prediction.

---

## 🚀 Future Improvements

Possible future improvements include:

- Testing additional Machine Learning algorithms.
- Performing hyperparameter tuning.
- Improving recall for Churn customers.
- Adding more visualizations.
- Deploying the Streamlit application online.
- Adding customer risk categories such as Low, Medium, and High Risk.

---

## 👨‍💻 Project

**Telco Customer Churn Prediction**

A Machine Learning project for predicting customer churn using telecom customer data.