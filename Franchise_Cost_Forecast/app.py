import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

st.title("Franchise Cost Forecast")

data = pd.read_csv(r"D:\Repositories\Data-Science\Franchise_Cost_Forecast\data\slr12.csv", sep = ";")

X = data[['FrqAnual']]
y = data['CusInic']

model = LinearRegression().fit(X,y)

col1, col2 = st.columns(2)

with col1:
    st.header("Data")
    st.table(data.head(6))

with col2:
    st.header("Dispersion Graph")
    fig, ax = plt.subplots()  # Substituir subplot por subplots
    ax.scatter(X, y, color='blue')
    ax.plot(X, model.predict(X), color='red')
    st.pyplot(fig)

st.header("Anual Franchise Value")

new_value = st.number_input("input value", min_value=1.0, max_value=999999.0, value=1500.0, step=0.01)

process = st.button("process")

if process:
    new_value_data = pd.DataFrame([[new_value]], columns=['FrqAnual'])
    pred = model.predict(new_value_data)
    st.header(f"Initial Cost Forecast $: {pred[0]:.2f}")