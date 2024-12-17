# Data Science & Machine Learning

Welcome to the **Data Science & Machine Learning Repository**! This repository showcases a variety of projects that apply machine learning, data analysis, and artificial intelligence to solve real-world problems. Each project explores unique datasets, leveraging algorithms and techniques to uncover insights and create predictive models.

## Repository Contents

Explore the following projects:

- **[Franchise Cost Forecast](https://github.com/tmabgdata/Data-Science/tree/main/Franchise_Cost_Forecast)**  
  A linear regression-based tool to predict franchise investment costs.

- **[Cars Quality Forecast](https://github.com/tmabgdata/Data-Science/tree/main/Quality_of_Cars)**  
  Vehicle classification based on features using Naive Bayes.

- **[Milk Production Forecast](https://github.com/tmabgdata/Data-Science/tree/main/MilkProd)**  
  Time series analysis and forecasting system for monthly milk production using SARIMAX.

- **[Probability Equipment Failures](https://github.com/tmabgdata/Data-Science/tree/main/Equipment_Failure)**   
  Probability of equipment failures based on the Poisson distribution.

- **[Normality of Data](https://github.com/tmabgdata/Data-Science/tree/main/Normality_of_Data)**  
  Test the normality of data using the Shapiro-Wilk test.

- **[Recommendation Rules](https://github.com/tmabgdata/Data-Science/tree/main/Recommendation_Rules)**  
  Generate and visualize association rules from transactional data using the Apriori algorithm.

- **[Milk Benchmark](https://github.com/tmabgdata/Data-Science/tree/main/Milk_Benchmark)**
  Time series forecasting tool using multiple statistical methods.

- **[Churn Rate - (In Progress)](https://github.com/tmabgdata/Data-Science/tree/main/EAD_churn)**  
  An exploratory analysis and predictive modeling project for churn prediction.

- **[AI - EDA](https://github.com/tmabgdata/Data-Science/tree/main/AI_EDA)**
  Automated exploratory data analysis

- **[Cargo Optimization](https://github.com/tmabgdata/Data-Science/tree/main/Cargo_Transport_Optimization)**
  Optimizes cargo selection using a Genetic Algorithm

- **[Multilingual Language Detection Model](https://github.com/tmabgdata/Data-Science/tree/main/NLP_LM's_Regex)**  
  Language detection using regex and language models.

- **[Spell Checker Model](https://github.com/tmabgdata/Data-Science/tree/main/NLP_SpellChecker_Project)**  
  A custom-built spell-checker utilizing NLP techniques.

- **[Sentiment Analysis Project](https://github.com/tmabgdata/Data-Science/tree/main/NLP_Kindle_Review_Sentiment_Analysis)**  
  Sentiment analysis on Kindle reviews with visualization and insights.

## How to Run the Projects

Each project is self-contained with its own set of instructions in the respective folder. Follow these general steps:

### Python Projects with Streamlit

1. Clone the repository:

   ```bash
   git clone https://github.com/tmabgdata/Data-Science.git
   cd Data-Science

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Navigate to the project's folder, then run:

    ```bash
    streamlit run app.py
    ```

4. Open your browser at the provided URL (e.g., `http://localhost:8501)` to interact with the app.

### Jupyter Notebook Projects

1. Ensure you have Jupyter installed:

    ```bash
    pip install notebook
    ```

2. Navigate to the project's folder:

    ```bash
    cd path/to/project
    ```

3. Launch Jupyter Notebook:

    ```bash
    jupyter notebook
    ```

4. Open the notebook file (`.ipynb`) and execute the cells to reproduce the analysis.

### Dash Projects (Upcoming)

- Dash-based projects will include clear instructions for setup and usage upon their release.

## Folder Structure

```graphql
Data-Science/
├── NLP_LM's_Regex/                  # Multilingual Language Detection
├── NLP_SpellChecker_Project/        # Spell Checker Model
├── NLP_Kindle_Review_Sentiment_Analysis/ # Sentiment Analysis
├── Franchise_Cost_Forecast/         # Franchise Cost Prediction
├── Quality_of_Cars/                 # Cars Quality Classification
├── EAD_churn/                       # Churn Analysis
(In Progress) 
├── MilkProd/                        # Time Series Analysis Prediction
├── Equipment_Failure/               # Probability with Poisson
├── Normality_of_Data                # Shapiro-Wilk test
├── Recommendation_Rules             # Apriori algorithm 
├── requirements.txt                 # Project dependencies
├── python_environment.md            # Python setup guide
└── .gitignore                       # Ignored files (e.g., checkpoints, `ds` environment)

```

## Recommendations for Testing the Projects

- **Environment**: Use Python 3.12 for all projects to ensure compatibility.

- **Isolation**: Create a virtual environment for testing individual projects.

- **Dependencies**: Install all libraries via ``requirements.txt`` to avoid compatibility issues.

- **GitIgnore**: Keep large files, temporary data, and personal environment folders like ds/ excluded from version control.

## Contributions

Contributions are welcome! Whether it's fixing issues, improving existing projects, or adding new ones:

1. Fork the repository.

2. Create a feature branch.

3. Submit a pull request with detailed information about your changes.

---

### Kind regards,

Thiago Alves
