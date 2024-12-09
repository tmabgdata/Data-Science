import streamlit as st
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules
import matplotlib.pyplot as plt

st.set_page_config(page_title="Generate Recommendation Rules",
                    layout="wide")
st.title("Generate Recommendation Rules")

with st.sidebar:
    uploaded_file = st.file_uploader("Upload file", type=['csv'])
    mini_support = st.number_input("Minimum Support", 0.0001,1.0,0.01,0.01)
    mini_threshold = st.number_input("Minimum Threshold", 0.0001,1.0,0.2,0.01)
    mini_lift = st.number_input("Minimum Lift", 0.0001,10.0,1.0,0.1)
    mini_range = st.number_input("Minimum Range", 1,10,2,1)
    process = st.button("Run")

if process and uploaded_file is not None:
    try:
        transactions = []
        for line in uploaded_file:
            transaction = line.decode("utf-8").strip().split(',')
            transactions.append(transaction)
        
        te = TransactionEncoder()
        te_ary = te.fit(transactions).transform(transactions)
        df = pd.DataFrame(te_ary, columns = te.columns_)

        frequent_itemsets = apriori(df, min_support = mini_support, use_colnames = True)
        num_itemsets = frequent_itemsets.shape[0]
        rules = association_rules(frequent_itemsets, metric = 'confidence',
                                    min_threshold = mini_threshold,
                                    num_itemsets=num_itemsets)

        filtered_rules = rules[(rules['lift'] >= mini_lift) &
                                (rules['antecedents'].apply(lambda x: len(x)>=mini_range))]
        
        if not filtered_rules.empty:
            col1, col2, col3 = st.columns(3)
            with col1:
                st.header("Transactions")
                st.dataframe(df)

            with col2:
                st.header("Rules Found")
                st.dataframe(filtered_rules)

            with col3:
                st.header("Visualization")
                fig, ax = plt.subplots()
                scatter = ax.scatter(filtered_rules['support'], filtered_rules['confidence'],
                                    alpha=0.5, c=filtered_rules['lift'], cmap='viridis')
                plt.colorbar(scatter, label='Lift')
                ax.set_title("Association Rules")
                ax.set_xlabel("Support")
                ax.set_ylabel("Confidence")
                st.pyplot(fig)

            st.header("Rules Resume")
            st.write(f"Total Rules Generated: {len(filtered_rules)}")
            st.write(f"Mean Support: {filtered_rules['support'].mean():.4f}")
            st.write(f"Mean Confidence: {filtered_rules['confidence'].mean():.4f}")
            st.write(f"Mean Lift: {filtered_rules['lift'].mean():.4f}")

            st.download_button(label = "Export to csv file",
                                data = filtered_rules.to_csv(index=False),
                                file_name = "association_rules.csv",
                                mime = 'text/csv')
        
        else:
            st.write("No rules were found with the defined parameters")

    except Exception as e:
        st.error(f'Process file error {e}')