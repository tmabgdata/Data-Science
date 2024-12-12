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

## Formulas Used in the Time Series Forecasting Project

### 1. **Naive Method**

Forecasts are based on the last observed value:

$\hat{y}_{t+h} = y_t$

---

### 2. **Mean Method**

Forecasts are the average of all historical values:

$\hat{y}_{t+h} = \frac{1}{n} \sum_{i=1}^{n} y_i$

---

## 3. **Drift Method**

Forecasts include a constant rate of change:

$\hat{y}_{t+h} = y_t + h \cdot \frac{y_t - y_1}{T - 1}$

---

## 4. **Holt’s Linear Trend Method**

This method uses exponential smoothing to capture linear trends.

1. **Level Update:**

$l_t = \alpha y_t + (1 - \alpha)(l_{t-1} + b_{t-1})$

2. **Trend Update:**

$b_t = \beta (l_t - l_{t-1}) + (1 - \beta)b_{t-1}$


3. **Forecast:**

$\hat{y}_{t+h} = l_t + h \cdot b_t$

---

## 5. **Holt-Winters Additive Method**

This method captures trends and seasonality with additive components.

1. **Level Update:**

$l_t = \alpha \left( y_t - s_{t-p} \right) + (1 - \alpha)(l_{t-1} + b_{t-1})$

2. **Trend Update:**

$b_t = \beta (l_t - l_{t-1}) + (1 - \beta)b_{t-1}$

3. **Seasonal Component Update:**

$s_t = \gamma (y_t - l_t) + (1 - \gamma)s_{t-p}$

4. **Forecast:**

$\hat{y}_{t+h} = l_t + h \cdot b_t + s_{t+h-p}$

---

## 6. **ARIMA (Auto Regressive Integrated Moving Average)**

A combination of autoregressive (AR), integration (I), and moving average (MA) components.

1. **AR Component (Autoregression):**

$y_t = \phi_1 y_{t-1} + \phi_2 y_{t-2} + \cdots + \phi_p y_{t-p} + \epsilon_t$

2. **I Component (Differencing for Stationarity):**

$y'_t = y_t - y_{t-1}$

3. **MA Component (Moving Average):**

$y_t = \epsilon_t + \theta_1 \epsilon_{t-1} + \theta_2 \epsilon_{t-2} + \cdots + \theta_q \epsilon_{t-q}$
