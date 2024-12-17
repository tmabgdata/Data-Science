# Cargo Transport Optimization

This Streamlit application optimizes cargo selection using a Genetic Algorithm. It helps users maximize the value of selected items while ensuring weight and volume constraints are respected.

<p align="center">
  <img src="https://res.cloudinary.com/dof97idbn/image/upload/v1734461250/Cargo_Op.gif" alt="Forecasting GIF" width="600">
</p>

## Requirements

Install the necessary libraries using pip:

pip install streamlit pandas geneticalgorithm

## How to Run the Application

1. Save the script as app.py.  
2. Run the application using Streamlit:

streamlit run app.py

3. Follow the instructions in your browser.

## Input Data Format

The application requires a CSV file with the following columns:  

- PESO: Weight of the item.  
- VOLUME: Volume of the item.  
- VALOR: Value of the item.  

The file must use a semicolon ";" as a delimiter.

### Example Input File

PESO;VOLUME;VALOR  
100;10;500  
200;20;800  
300;30;1000  
400;40;1500  

## Application Workflow  

1. Upload Data:  
- Upload a CSV file containing the cargo data.  
- The application will display the total number of items, total weight, total volume, and total value.  

2. Set Constraints:  
- Sobra de Peso: Enter the maximum allowable weight.  
- Sobra de Volume: Enter the maximum allowable volume.  
- Iterações: Set the number of iterations for the Genetic Algorithm.  

3. Run Optimization:  
- The Genetic Algorithm will process the data and return the optimal cargo selection.

4. Results:  
- View the optimized cargo list.  
- Final totals for weight, volume, and value will be displayed.

## Genetic Algorithm Configuration  

The following parameters are configured for the Genetic Algorithm:  

- Population Size: 10  
- Mutation Probability: 0.1  
- Elitism Ratio: 0.01  
- Crossover Probability: 0.5  
- Parents Portion: 0.3  
- Crossover Type: Uniform  
- Iterations Without Improvement: None  

## Output  

After running the optimization, the application displays:  

1. Optimized List: A table of selected items.  
2. Summary Metrics:  
   - Quantity of selected items.  
   - Total weight.  
   - Total volume.  
   - Total value.  

### Example Output

Quantidade Final: 5  
Peso Final: 2900  
Volume Final: 200  
Valor Total: 15000  

## Notes  

- Ensure the uploaded CSV file adheres to the specified format.  
- Solutions exceeding the weight or volume constraints are penalized in the optimization process.  