# Normality Test

This project is a simple **Streamlit** application to test the normality of data using the Shapiro-Wilk test. It provides a visual representation of the data with a histogram and QQ plot, and displays the p-value of the test to determine if the data follows a normal distribution.

<p align="center">
  <img src="https://res.cloudinary.com/dof97idbn/image/upload/v1733767356/Normality_Test.gif" alt="Normality GIF" width="600">
</p>


## 🔧 **Features**

- **File Upload**: Accepts `.csv` files for analysis.
- **Histogram**: Displays the frequency distribution of the data.
- **QQ Plot**: Shows the quantile-quantile plot for the data.
- **Normality Test**: Uses the Shapiro-Wilk test to evaluate normality and provides a clear interpretation of the result.

## 🚀 **How to Use**

### 1. Installation

Ensure you have Python installed (version 3.9 or higher is recommended). Install the required libraries using the following command:

```bash
pip install streamlit pandas numpy matplotlib scipy
```

### 2. Run the Application

Run the app from your terminal:

```bash
streamlit run app.py
```

### 3. Usage

1. **Upload a File**:

    - Click **Browse files** in the sidebar to upload a `.csv` file containing a single column of numerical data.

2. **Run the Test**:

    - Click the Run button to process the data.

3. **Interpret the Results**:

    - View the histogram and QQ plot for a visual analysis of the data distribution.

    - Check the p-value of the Shapiro-Wilk test to determine if the data is normally distributed:
        
        - **p-value > 0.05**: Insufficient evidence to reject normality.
        - **p-value ≤ 0.05**: Sufficient evidence to reject normality.

## 📊 Example Visualizations

The app generates:

- **Histogram**: Displays the distribution of the data.

- **QQ Plot**: Compares the quantiles of the data to a normal distribution.

## 🛠 Technologies Used

- **Python**: Core programming language.

- **Streamlit**: For creating the interactive web application.

- **Pandas**: For data handling and manipulation.

- **Matplotlib**: For plotting the histogram and QQ plot.

- **SciPy**: For statistical analysis, including the Shapiro-Wilk test.

## 📈 Use Case

This tool is useful for data scientists and analysts who need to test the normality of their data before applying statistical methods that assume normality, such as t-tests or ANOVA.

## 🤝 Contributions

Contributions, issues, and feature requests are welcome! Feel free to fork the repository and submit a pull request.