import streamlit as st
import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt
from datetime import date
from io import StringIO

st.set_page_config(page_title="Time Series Analysis and Forecasting System",
                    layout = "wide")

st.title("Time Series Analysis and Forecasting System")

with st.sidebar:
    uploaded_file = st.file_uploader("upload file", type=['csv'])
    if uploaded_file is not None:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        data = pd.read_csv(stringio, header = None)
        start_date = date(2000,1,1)
        period = st.date_input("initial period of the series", start_date)
        forecast_period = st.number_input("months to forecast", min_value=1, max_value=48, value=12)
        process = st.button("process")

if uploaded_file is not None and process:
    try:
        ts_data = pd.Series(data.iloc[:,0].values, index=pd.date_range(
            start=period, periods=len(data), freq='M'
        ))

        decomposition = seasonal_decompose(ts_data, model='additive')
        fig_decomposition = decomposition.plot()
        fig_decomposition.set_size_inches(10,8)

        model = SARIMAX(ts_data, order=(2,0,0), seasonal_order=(0,1,1,12))
        fit_model = model.fit()
        forecast = fit_model.forecast(steps=forecast_period)

        forecast_fig, ax = plt.subplots(figsize=(10,5))
        ax = ts_data.plot(ax=ax)
        forecast.plot(ax=ax, style='r--')

        col1, col2, col3 = st.columns([3,3,2])
        with col1:
            st.write("Decomposition")
            st.pyplot(fig_decomposition)
        with col2:
            st.write("Forecast")
            st.pyplot(forecast_fig)
        with col3:
            st.write("Forecast Data")
            st.dataframe(forecast)

    except Exception as e:
        st.error(f"Error processing data: {e}")