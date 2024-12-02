# NLP Spell Checker Project

This project involves building a Natural Language Processing (NLP) system for text preprocessing, language detection, and spell checking using a dataset in Brazilian Portuguese. The system uses machine learning models like Logistic Regression and Random Forest, with various text preprocessing techniques applied for optimal performance.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Data](#data)
- [Preprocessing Steps](#preprocessing-steps)
- [Modeling](#modeling)
- [Results](#results)
- [How to Use](#how-to-use)
- [Future Work](#future-work)
- [Contributing](#contributing)
- [License](#license)

---

## Introduction

Spell checking is a critical task in NLP, especially for applications in text editors and search engines. This project explores creating a spell checker for Portuguese text using advanced preprocessing techniques and machine learning models.

---

## Features

- Tokenization and text normalization.
- Stopword removal tailored to Brazilian Portuguese.
- Vectorization using TF-IDF.
- Support for hyperparameter optimization.
- Evaluation of multiple machine learning models.

---

## Data

The dataset (`artigos.txt`) consists of textual data in Brazilian Portuguese. It is located at:
`Data-Science\NLP_SpellChecker_Project\data\raw\artigos.txt`.

---

## Preprocessing Steps

1. **Tokenization**: Splitting text into individual words.
2. **Stopword Removal**: Removing common words that do not contribute to meaning.
3. **Stemming and Lemmatization**: Reducing words to their base forms.
4. **Vectorization**: Converting text to numerical features using TF-IDF and n-grams.

---

## Modeling

- Models evaluated:
  - Logistic Regression
  - Random Forest
- Hyperparameter tuning was performed using GridSearchCV.
- Implemented lemmatization and n-grams for better context understanding.

---

## Results

### Logistic Regression
- Baseline Accuracy: 50.6%
- After tuning: 50.7%

### Random Forest
- Baseline Accuracy: 51.3%
- After preprocessing: 51.6%

---

## How to Use

### Requirements

Install the necessary Python packages:
```bash
pip install -r requirements.txt
```

## Run the Project

1. Clone this repository.

2. Ensure the dataset is placed at the specified path.

3. Run the Jupyter Notebook to train and evaluate models:

```bash
jupyter notebook notebooks/main_notebook.ipynb
```

## Future Work

. Add more complex language models (e.g., transformers).

. Implement a comprehensive evaluation metric like F1-score.

. Expand to support other languages.

## Contributing

Contributions are welcome! Feel free to fork this repository and submit a pull request.

## License

This project is licensed under the MIT License.

