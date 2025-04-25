import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Fungsi untuk memuat model dan scaler
def load_model_and_scaler():
    # Load model churn
    with open("model_churn_log.pkl", "rb") as model_file:
        model = pickle.load(model_file)

    # Load scaler
    with open("scaler.pkl", "rb") as scaler_file:
        scaler = pickle.load(scaler_file)

    # Kolom fitur yang digunakan dalam model
    feature_columns = [
        'CreditScore', 'Age', 'Tenure', 'Balance',
        'NumOfProducts', 'HasCrCard', 'IsActiveMember', 'EstimatedSalary'
    ]

    return model, scaler, feature_columns

# Fungsi prediksi churn
def predict_churn(user_input):
    model, scaler, feature_columns = load_model_and_scaler()

    # Buat DataFrame dari input user
    data = pd.DataFrame([user_input], columns=feature_columns)

    # Validasi bahwa scaler adalah objek StandardScaler dan cocok fiturnya
    if not isinstance(scaler, StandardScaler):
        raise ValueError("Scaler bukan objek StandardScaler yang valid.")
    
    if hasattr(scaler, 'feature_names_in_'):
        if list(scaler.feature_names_in_) != feature_columns:
            raise ValueError(f"Fitur tidak cocok dengan training: {scaler.feature_names_in_} != {feature_columns}")

    # Transformasi data
    data_scaled = scaler.transform(data)

    # Prediksi
    prediction = model.predict(data_scaled)

    return prediction[0]  # ambil hasil sebagai integer
