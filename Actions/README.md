# Actions Viewer

This project is a Streamlit application that allows users to visualize stock data for selected companies. The application fetches data from Yahoo Finance and displays various charts, including price history, trading volume, and candlestick charts.

## Features

- **Company Selection**: Choose from a list of companies (AAPL, GOOGL, MSFT, AMZN, TSLA).
- **Date Range Selection**: Specify the start and end dates for the data.
- **Price History Chart**: View the adjusted close price over time.
- **Trading Volume Chart**: Visualize the trading volume over time.
- **Candlestick Chart**: Analyze the stock's open, high, low, and close prices.

## Technologies Used

- **Python 3.12**
- **Streamlit**: Interactive web application framework.
- **yfinance**: Library to fetch stock data from Yahoo Finance.
- **Plotly**: Library for creating interactive charts.

## Project Structure

Actions/ ├── app.py


## How to Run the Application

1. Clone this repository:

    ```bash
    git clone https://github.com/YOUR_USERNAME/Actions.git
    cd Actions
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the Streamlit application:

    ```bash
    streamlit run app.py
    ```

4. Open your browser at the provided URL (e.g., `http://localhost:8501`) to interact with the app.

## Usage

1. Select the company from the dropdown menu in the sidebar.
2. Choose the start and end dates for the data.
3. Click the "Generate Charts" button to display the charts.
4. View the price history, trading volume, and candlestick charts in the main area.

## Contribution

Contributions are welcome! Feel free to open an issue or submit a pull request.

## Contact

Created by Thiago Alves. For any questions or suggestions, please contact me via GitHub.

### Customization

- Replace `YOUR_USERNAME` with your GitHub username.
- Optionally include example inputs, outputs, or screenshots of the application to make the documentation more engaging.

Make sure to replace YOUR_USERNAME with your actual GitHub username before using the documentation. Make sure to replace YOUR_USERNAME with your actual GitHub username before using the documentation.