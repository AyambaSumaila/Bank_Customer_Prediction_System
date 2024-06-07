import  streamlit as st
import  numpy as np
import pandas as pd
from sklearn.preprocessing import  StandardScaler
import pickle

stanC=StandardScaler()

df=pickle.load(open("df.pkl", 'rb'))
rand=pickle.load(open("rand.pkl", 'rb'))

def prediction(CreditScore,	Geography, Gender, Age, Tenure, Balance, NumberOfProducts, HasCrCard, IsActiveMember, EstimatedSalary):

    if CreditScore == '':
        st.error("Please enter a valid score.")
        return None
    if Geography == '':
        st.error("Please enter a valid Geography.")
        return None
    if Gender == '':
        st.error("Please enter a valid Gender.")
        return None
    if Age == '':
        st.error("Please enter a valid Age!.")
        return None

    if Tenure == '':
        st.error("Please enter a valid Tenure.")
        return None

    if Balance == '':
        st.error("Please enter a valid Balance.")
        return None

    if NumberOfProducts == '':
        st.error("Please enter a valid Number of Products.")
        return None


    if HasCrCard == '':
        st.error("Please enter a valid NUmber of HasCard")
        return None

    if IsActiveMember == '':
        st.error("Please enter a valid number of Isactive")
        return None

    if EstimatedSalary == '':
        st.error("PLease enter a valid number of Estimated Salary")
        return None



    features=np.array([[float(CreditScore),	Geography, Gender, float(Age), float(Tenure), float(Balance), float(NumberOfProducts), HasCrCard, IsActiveMember, float(EstimatedSalary)]])
    features=stanC.fit_transform(features)
    prediction=rand.predict(features).reshape(1, -1)

    return prediction[0]
st.title("Bank Churn Prediction System ")

CreditScore=st.number_input("Credit Score")
Geography=st.text_input("Geography")
Gender=st.text_input("Gender")
Age=st.number_input("Age")
Tenure=st.number_input("Tenure")
Balance=st.number_input("Balance")
numberOfProducts=st.number_input("Products Number")
credits_card=st.number_input("Credit Card")
active_member=st.number_input("Active Member")
estimated_salary=st.number_input("Estimated Salary ")




if st.button("Predict"):
    pred=prediction(CreditScore, Geography, Gender, Age, Tenure, Balance, numberOfProducts, credits_card, active_member, estimated_salary )

    if pred is not None:
        if pred == 1:
            st.write("This customer has left")
        else:
            print("The customer is still active")
