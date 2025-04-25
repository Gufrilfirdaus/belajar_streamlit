# prediksi_california_house.py

import streamlit as st
import pandas as pd
import shap
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import RandomForestRegressor

def prediksi_california_house():
    # Load California Housing dataset
    housing = fetch_california_housing(as_frame=True)
    X = housing.data
    Y = housing.target

    st.write("""
    # California House Price Prediction App 🏡
    
    This app predicts the **California House Price**!
    """)
    st.write('---')

    # Sidebar Input
    st.sidebar.header('Specify Input Parameters')

    def user_input_features():
        data = {}
        for col in X.columns:
            data[col] = st.sidebar.slider(col, float(X[col].min()), float(X[col].max()), float(X[col].mean()))
        features = pd.DataFrame(data, index=[0])
        return features

    df = user_input_features()

    # Show input
    st.header('Specified Input Parameters')
    st.write(df)
    st.write('---')

    # Train model
    model = RandomForestRegressor()
    model.fit(X, Y)

    # Prediction
    prediction = model.predict(df)

    st.header('Prediction of Median House Value')
    st.write(f"${prediction[0] * 100_000:,.2f}")
    st.write('---')

    # SHAP Explanation
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X)

    st.header('Feature Importance')

    st.set_option('deprecation.showPyplotGlobalUse', False)
    plt.title('Feature Importance based on SHAP Values')
    shap.summary_plot(shap_values, X)
    st.pyplot(bbox_inches='tight')
    st.write('---')

    plt.title('Feature Importance (Bar)')
    shap.summary_plot(shap_values, X, plot_type="bar")
    st.pyplot(bbox_inches='tight')
