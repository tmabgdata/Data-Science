# Time Series Benchmark Forecasting

This project provides a comprehensive time series forecasting tool using multiple statistical methods, implemented with Streamlit. The application enables users to upload datasets, choose forecast methods, and visualize predictions, making it ideal for exploring trends and benchmarking.

## 🌟 Features

- **Data Upload**: Upload your time series dataset in CSV format.

- **Forecast Methods**: Choose from various forecasting methods, including:

    - **Naive**

    - **Mean**

    - **Drift**

    - **Holt's Linear Method**

    - **Holt-Winters Additive Seasonal Method**

    - **ARIMA (Auto Regressive Integrated Moving Average)**

- **Interactive Inputs**: Configure forecast periods, data range, and methods via the sidebar.

- **Visualization**: Compare actual and predicted values with dynamically generated plots.

- **Warnings & Validation**: Input validation to guide users in defining proper ranges.

## 🎥 Demo

<img src="https://res.cloudinary.com/dof97idbn/image/upload/v1734021849/benchmark_milk.gif" alt="Demo GIF" style="max-width:100%; height:auto;">

## 📊 Methods

### 1. Naive

Predicts future values as the last observed value in the series.

### 2. Mean

Forecasts using the average of observed values.

### 3. Drift

Projects values based on the trend of the first and last data points.

### 4. Holt's Linear

A linear exponential smoothing method for trend-based forecasting.

### 5. Holt-Winters Additive

Handles seasonality with additive decomposition.

### 6. ARIMA

Automatically determines the best-fit model parameters and provides seasonal adjustment.
