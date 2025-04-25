import streamlit as st 
import pandas as pd
from prediksi import predict_churn

st.set_page_config(layout="centered")
st.sidebar.title("My Portfolio \n👨🏻‍💻 Muhammad Gufril Firdaus")

page = st.sidebar.selectbox(
    "Main Menu",
    ["Tentang Saya", "Data Science Project", "Prediksi Churn", "Kontak"], 
    index=0,
)

if page == "Tentang Saya":
    import tentang_saya
    tentang_saya.tampilkan_tentang_saya()

elif page == "Data Science Project":
    import project
    project.tampilkan_data_science_project()

elif page == "Kontak":
    import kontak
    kontak.tampilkan_kontak()

elif page == "Prediksi Churn":
    st.title("Prediksi Churn Pelanggan")
    st.write("Masukkan informasi pelanggan untuk memprediksi apakah pelanggan tersebut akan churn atau tidak.")

    # Input pengguna, harus sesuai urutan dan nama kolom saat training
    user_input = {
        'CreditScore': st.number_input('Credit Score', min_value=300, max_value=850, value=600),
        'Age': st.number_input('Age', min_value=18, max_value=100, value=30),
        'Tenure': st.number_input('Tenure (Years)', min_value=0, max_value=10, value=3),
        'Balance': st.number_input('Balance', min_value=0, max_value=500000, value=50000),
        'NumOfProducts': st.selectbox('Number of Products', options=[1, 2, 3, 4], index=1),
        'HasCrCard': st.selectbox('Has Credit Card', options=[0, 1], index=0),
        'IsActiveMember': st.selectbox('Is Active Member', options=[0, 1], index=1),
        'EstimatedSalary': st.number_input('Estimated Salary', min_value=1000, max_value=200000, value=50000)
    }

    # Menjalankan prediksi
    if st.button('Prediksi'):
        result = predict_churn(user_input)

        # Menampilkan hasil prediksi
        if result == 1:
            st.success("✅ Pelanggan diprediksi akan *churn*.")
        else:
            st.success("✅ Pelanggan diprediksi **tidak** akan *churn*.")
