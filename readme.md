
# Data Source

# Kaggle - Churn Modelling Calssification Data Set

This data set contains details of a bank's customers and the target variable is a binary variable reflecting the fact whether the customer left the bank (closed his account) or he continues to be a customer.

It consists of 10,000 records with demographic and bank history information from customers from three countries, France, Germany and Spain,
Exploratory Analysis
# Bank Customer Churn Prediction

## Problem Statement
In the highly competitive banking industry, retaining customers is critical for the success and growth of any financial institution. Customer churn, which refers to customers leaving the bank for competitors, can significantly impact profitability. The aim of this project is to develop a machine learning model that accurately predicts whether a bank customer will churn or not based on their profile and transaction history.

## Importance of the Project
Predicting customer churn is vital for banks to:
1. **Increase Retention Rates:** Identifying customers likely to leave allows banks to take proactive measures to retain them, thereby reducing churn rates.
2. **Enhance Customer Satisfaction:** By understanding the reasons behind churn, banks can improve their services and customer experience.
3. **Optimize Marketing Strategies:** Targeted marketing campaigns can be designed to address the specific needs of customers who are at risk of churning.
4. **Maximize Revenue:** Retaining existing customers is often more cost-effective than acquiring new ones, thus protecting and enhancing the bank's revenue.

## Features
- **Customer Information:** Age, Gender, Tenure, Account Balance, Number of Products, Has Credit Card, Is Active Member, Estimated Salary.
- **Behavioral Data:** Transaction history, average transaction amount, transaction frequency.
- **Geographical Data:** Customer’s region or country.

## Model and Methodology
1. **Data Collection:** Gathering historical data of bank customers including both churned and retained customers.
2. **Data Preprocessing:** Cleaning the data, handling missing values, encoding categorical variables, and normalizing the data.
3. **Exploratory Data Analysis (EDA):** Analyzing data to find patterns and correlations between features and churn.
4. **Model Selection:** Trying various machine learning algorithms like Logistic Regression, Decision Trees, Random Forest, and Gradient Boosting.
5. **Model Evaluation:** Evaluating models using metrics like Accuracy, Precision, Recall, F1-Score, and ROC-AUC.
6. **Hyperparameter Tuning:** Optimizing model parameters to improve performance.
7. **Deployment:** Deploying the best model using a web application framework (e.g., Flask or Django).

## Installation
To set up the project on your local machine, follow these steps:
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/bank-customer-churn-prediction.git
