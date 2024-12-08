# Franchise Cost Forecast

This project is an interactive application developed with Python and Streamlit to predict the **initial cost of a franchise** based on annual investment. The application uses a Linear Regression model for the predictions.

## Features

- Visualization of historical data on annual investments and initial franchise costs.
- Scatter plot displaying actual data and the regression line.
- Prediction of a franchise's initial cost based on user-provided annual investment values.

## Technologies Used

- **Python 3.12**
- **Streamlit**: Interactive interface for the application.
- **Pandas**: Data manipulation and analysis.
- **Matplotlib**: Data visualization.
- **Scikit-learn**: Linear Regression model implementation.

## Project Structure

```python
Franchise Cost Forecast/ 
├── data/ 
│ └── slr12.csv  
├── app.py  
└── README.md
```

## Prerequisites

Before running the project, ensure you have installed:

- [Python 3.12](https://www.python.org/)

- [Streamlit](https://streamlit.io/): Install via pip: `pip install streamlit`

- Additional libraries:
  - Pandas: `pip install pandas`
  - Matplotlib: `pip install matplotlib`
  - Scikit-learn: `pip install scikit-learn`

## Running the Project

1. Clone this repository:

   ```bash
   git clone https://github.com/YOUR_USERNAME/Franchise_Cost_Forecast.git
    ```

2. Navigate to the project directory:

    ```bash
    cd LinearRegression
    ````

3. Run the Streamlit application:

    ```bash
    streamlit run app.py
    ```

4. Access the application in your browser at:

    ```bash
    http://localhost:8501
    ```

## How to Use the Application

1. In the left column, view the historical data of investment and initial costs.

2. In the right column, see the scatter plot and the fitted regression line.

3. Input an annual investment value in the designated field.

4. Click the Process button to calculate and display the predicted initial cost.

## Dataset

The dataset `slr12.csv` contains:

- FrqAnual: Annual franchise investment.

- CusInic: Initial franchise cost.

The data should be located in the `data/` folder of the project.

## Contribution

Contributions are welcome! Feel free to open an issue or submit a pull request.

## Contact

Created by Thiago Alves. For questions or suggestions, feel free to contact me on GitHub.

### Adjustments

- Replace `YOUR_USERNAME` with your GitHub username.
- Optionally, include screenshots of the application or an example prediction to enhance the documentation.
