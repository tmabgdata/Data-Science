# Sentiment Analysis Project

This project focuses on performing sentiment analysis on product reviews using various machine learning techniques, including Support Vector Machine (SVM), Naive Bayes, and LSTM (Long Short-Term Memory) models. The goal of the project is to classify reviews as either positive or negative based on the text.

[kindle review sentiment analysis](https://github.com/tmabgdata/Data-Science/blob/main/NLP_Kindle_Review_Sentiment_Analysis/kindle_review_sentiment_analysis.ipynb)

## Project Overview

The sentiment analysis is performed on a dataset of product reviews. The reviews are preprocessed using techniques like tokenization, stopword removal, lemmatization, and vectorization with TF-IDF and Bag of Words (BoW) methods. The models are then trained on the processed text data to predict whether a review is positive or negative.

### Key Components:

- **Data Preprocessing:** Removal of HTML tags, URLs, special characters, stopwords, and lemmatization of words.
- **Feature Engineering:** TF-IDF and BoW vectorization methods.
- **Models Used:** SVM, Naive Bayes, and LSTM.
- **Performance Metrics:** Accuracy, precision, recall, F1-score, confusion matrix.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/tmabgdata/Data-Science/tree/main/NLP_Kindle_Review_Sentiment_Analysis
cd NLP_Kindle_Review_Sentiment_Analysis
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Results

- SVM Model:
    - Accuracy: 84.5%
    - Precision: 0.87 (positive class)
    - Recall: 0.91 (positive class)
    - F1-score: 0.89 (positive class)

- LSTM Model:
    - Accuracy: 82%
    - Precision: 0.89 (positive class)
    - Recall: 0.84 (positive class)
    - F1-score: 0.86 (positive class)

## Contributing

Feel free to fork this repository and submit pull requests. If you find any bugs or improvements, please create an issue or contribute to the project!
