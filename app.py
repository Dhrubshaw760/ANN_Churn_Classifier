import streamlit as st
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder
import pandas as pd
import pickle

# Load the trained model
model = tf.keras.models.load_model('model.h5')

with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)
with open('onehot_encoder_geo.pkl', 'rb') as f:
    onehot_encoder_geo = pickle.load(f)
with open('label_encoder_gender.pkl', 'rb') as f:
    label_encoder_gender = pickle.load(f)

## Streamlit app 
st.title('Customer Churn Prediction')

# User Input
credit_score = st.number_input('Credit Score')
geo = st.selectbox('Geography', onehot_encoder_geo.categories_[0])
gender = st.selectbox('Gender', label_encoder_gender.classes_)
age = st.slider('Age', 18, 92)
balance = st.number_input('Balance')
estimated_salary = st.number_input('Estimated Salary')
tenure = st.slider('Tenure', 0, 10)
num_of_prod = st.slider('No of prods', 1, 4)
has_cr_card = st.selectbox('Has Credit Card', [0, 1])
is_active_member = st.selectbox('Is Active Member ', [0, 1])

# Input Data
# Example input data
input_data = pd.DataFrame({
    'CreditScore': [credit_score],
    'Gender': [label_encoder_gender.transform([gender])[0]],
    'Age': [age],
    'Tenure': [tenure],
    'Balance': [balance],
    'NumOfProducts': [num_of_prod],
    'HasCrCard': [has_cr_card],
    'IsActiveMember': [is_active_member],
    'EstimatedSalary': [estimated_salary],
})

# Encode Geography
ohe = onehot_encoder_geo.transform([[geo]]).toarray()
ohdf = pd.DataFrame(ohe, columns=onehot_encoder_geo.get_feature_names_out(['Geography']))

# Combine one-hot encoded
input_data = pd.concat([input_data.reset_index(drop=True), ohdf], axis=1)  

# Scale the input data
scaler = scaler.transform(input_data)

# Predict churn 
pred = model.predict(scaler)
pred_proba = pred[0][0]
st.write('Churn Probability: ', pred_proba)

if pred_proba > 0.5:
    st.write('The customer is likely to churn.')
else:
    st.write('The customer is not likely to churn.')
