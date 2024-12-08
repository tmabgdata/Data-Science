# Cars Quality Forecast

This project is an interactive tool developed with Python and Streamlit to classify the **quality of vehicles** based on various features. It uses a **Naive Bayes model** trained on categorical data to predict the vehicle's quality.

## Features

- Load and preprocess data for categorical classification.
- Train and evaluate a **Categorical Naive Bayes** model with accuracy feedback.
- Interactive interface for users to input vehicle features and receive quality predictions.

## Technologies Used

- **Python 3.12**
- **Streamlit**: Interactive web application.
- **Pandas**: Data manipulation.
- **Scikit-learn**: Machine Learning model implementation and preprocessing.

## Project Structure

```
Quality_of_Cars/
├── .streamlit/
│ └── config.toml
├── data/
│ └── car.csv
├── app.py
└── README.md
```

# Project documentation


## Dataset
The dataset `car.csv` contains the following features:
- **buying**: Price of the car.
- **maint**: Maintenance cost.
- **doors**: Number of doors.
- **persons**: Capacity for passengers.
- **lug_boot**: Trunk size.
- **safety**: Safety rating.
- **class**: Target variable representing car quality (e.g., acceptable, unacceptable, good, very good).

The dataset must be located in the `data/` folder.

## Prerequisites
Before running the project, ensure you have the following installed:
- [Python 3.12](https://www.python.org/)
- Libraries:
  - Streamlit: `pip install streamlit`
  - Pandas: `pip install pandas`
  - Scikit-learn: `pip install scikit-learn`

## How to Run the Project

1. Clone this repository:

```bash
git clone https://github.com/YOUR_USERNAME/Quality_of_Cars.git
```

2. Navigate to the project directory:

```bash
cd Quality_of_Cars
```

3. Run the Streamlit application:

```bash
http://localhost:8501
```

4. Open your browser at:

```bash
http://localhost:8501
```

## Usage

1. Review the model's accuracy displayed on the main page.

2. Use the dropdown menus to select the car's features:
Price

- Maintenance cost
- Number of doors
- Passenger capacity
- Trunk size
- Safety rating

3. Click Process to classify the car's quality.

4. The predicted quality will be displayed at the top of the page.

## Configuration

The Streamlit interface configuration is defined in .`streamlit/config.toml`. You can customize page settings, such as layout and title.

## Contribution

Contributions are welcome! Feel free to open an issue or submit a pull request.

## Contact

Created by Thiago Alves. For any questions or suggestions, please contact me via GitHub.


### Customization

- Replace `YOUR_USERNAME` with your GitHub username.

- Optionally include example inputs, outputs, or screenshots of the application to make the documentation more engaging.

- Add a note about the dataset source if it's public or mention its license. 
