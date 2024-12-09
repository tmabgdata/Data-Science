# Generate Recommendation Rules

This project is a **Streamlit** application designed to generate and visualize **association rules** from transactional data using the Apriori algorithm. It allows users to define parameters such as **minimum support**, **confidence**, and **lift** to filter and customize the generated rules. The app also provides an interactive scatter plot for rule visualization.

<div align="center">
  <img src="https://res.cloudinary.com/dof97idbn/image/upload/v1733774971/found_rules.gif" alt="Project GIF" width="600">
</div>

## 🔧 **Features**

- **File Upload**: Accepts `.csv` files containing transactional data.
- **Parameter Settings**: Allows users to customize:
  - Minimum support.
  - Minimum confidence threshold.
  - Minimum lift value.
  - Minimum size of itemsets.
- **Association Rules Generation**: Generates rules using the Apriori algorithm.
- **Interactive Visualization**: Scatter plot to visualize the relationships between support, confidence, and lift of rules.
- **Results Export**: Download the filtered rules as a `.csv` file.

## 🚀 **How to Use**

### 1. Installation

Ensure Python is installed (version 3.9 or higher is recommended). Install the required libraries:

```bash
pip install streamlit pandas mlxtend matplotlib
```

## 2. Run the Application

Run the app locally:

```bash
streamlit run app.py
```

## 3. Usage

#### 1. Upload a Transactional File:
    
- The file should contain transactions in a comma-separated format, with each line representing one transaction.

#### 2. Set Parameters:

- Adjust minimum support, confidence, lift, and range of itemsets using the sidebar inputs.

#### 3. Generate Rules:

- Click the Run button to process the file and generate rules.

#### 4. Analyze Results:

- Explore the transaction data, filtered rules, and visualization in separate sections.

- Review a summary of the generated rules, including total count, mean support, confidence, and lift.

#### 5. Export Rules:

- Download the rules as a `.csv` file for further analysis or reporting.

## 📊 Example Visualizations

- Scatter Plot: Displays the relationship between:
        
    - Support (x-axis)
    - Confidence (y-axis)
    - Lift (color gradient)

## 🛠 Technologies Used

- **Python**: Core programming language.
- **Streamlit**: For creating the interactive web application.
- **Pandas**: For data handling and manipulation.
- **mlxtend**: For generating association rules using the Apriori algorithm.
- **Matplotlib**: For visualizing rule relationships.

## 📈 Use Case

This tool is ideal for retail, e-commerce, and other domains where understanding associations between items is crucial. Examples include:

- Recommending products based on frequently purchased itemsets.
- Identifying patterns in customer purchase behavior.

## 🤝 Contributions

Contributions are welcome! Feel free to fork the repository, submit issues, or create pull requests.