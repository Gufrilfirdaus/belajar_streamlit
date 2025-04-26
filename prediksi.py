import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler
import streamlit as st

# Fungsi untuk memuat model dan scaler
def load_model_and_scaler():
    with open("model_churn_log.pkl", "rb") as model_file:
        model = pickle.load(model_file)

    with open("scaler.pkl", "rb") as scaler_file:
        scaler = pickle.load(scaler_file)

    feature_columns = [
        'CreditScore', 'Age', 'Tenure', 'Balance',
        'NumOfProducts', 'HasCrCard', 'IsActiveMember', 'EstimatedSalary'
    ]

    return model, scaler, feature_columns

# Fungsi prediksi churn
def predict_churn(user_input):
    model, scaler, feature_columns = load_model_and_scaler()

    data = pd.DataFrame([user_input], columns=feature_columns)

    if not isinstance(scaler, StandardScaler):
        raise ValueError("Scaler bukan objek StandardScaler yang valid.")

    if hasattr(scaler, 'feature_names_in_'):
        if list(scaler.feature_names_in_) != feature_columns:
            raise ValueError(f"Fitur tidak cocok dengan training: {scaler.feature_names_in_} != {feature_columns}")

    data_scaled = scaler.transform(data)
    prediction = model.predict(data_scaled)
    return prediction[0]

# Fungsi input user yang lebih bervariasi
def user_input_features():
    st.header('📝 Input Customer Information')
    CreditScore = st.slider('Credit Score (range 300-900)', 300, 900, 600)
    Age = st.number_input('Age (years)', min_value=18, max_value=100, value=30)
    Tenure = st.selectbox('Tenure (years)', options=list(range(0, 11)), index=5)
    Balance = st.text_input('Balance (account balance)', value="50000")
    try:
        Balance = float(Balance)
    except ValueError:
        st.warning("⚠️ Balance must be a number. Set automatically to 0.")
        Balance = 0.0
    NumOfProducts = st.radio('Number of Products', options=[1, 2, 3, 4])
    HasCrCard = st.selectbox('Has Credit Card?', options=[('Yes', 1), ('No', 0)], format_func=lambda x: x[0])[1]
    IsActiveMember = st.selectbox('Is Active Member?', options=[('Yes', 1), ('No', 0)], format_func=lambda x: x[0])[1]
    EstimatedSalary = st.slider('Estimated Salary', 0, 200000, 70000)

    user_data = {
        'CreditScore': CreditScore,
        'Age': Age,
        'Tenure': Tenure,
        'Balance': Balance,
        'NumOfProducts': NumOfProducts,
        'HasCrCard': HasCrCard,
        'IsActiveMember': IsActiveMember,
        'EstimatedSalary': EstimatedSalary
    }

    return user_data

# Main Program
def main():
    st.title('🏦 Customer Churn Prediction App')

    user_input = user_input_features()

    # Tombol Reset untuk form
    if st.button('🔄 Reset Form'):
        st.experimental_rerun()

    if st.button('🔮 Predict Now'):
        prediction = predict_churn(user_input)
        if prediction == 1:
            st.error('⚡ Customer is likely to CHURN! Take action!')
        else:
            st.success('🎯 Customer is likely to STAY loyal!')

if __name__ == '__main__':
    main()
