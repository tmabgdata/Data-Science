import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

st.set_page_config(page_title="Normality Test", layout="wide")
st.title("Normality Test")

with st.sidebar:
    upload_file = st.file_uploader("Upload File:", type=['csv'],
                                    accept_multiple_files=False)
    process_button = st.button("Run")

if process_button and upload_file is not None:
    try:
        data = pd.read_csv(upload_file, header=None)
        if data.empty or data.iloc[:,0].isnull().all():
            st.error("Empty File or Not Validate Data")
        else:
            col1, col2 = st.columns(2)
            with col1:
                fig_hist, ax_hist = plt.subplots()
                ax_hist.hist(data.iloc[:,0].dropna(), bins="auto", color='blue', alpha=0.7, rwidth=0.85)
                ax_hist.set_title("Histogram")
                st.pyplot(fig_hist)

            with col2:
                fig_qq, ax_qq = plt.subplots()
                stats.probplot(data.iloc[:,0].dropna(), dist="norm", plot=ax_qq)
                ax_qq.set_title("QQ Plot")
                st.pyplot(fig_qq)

            shapiro_test = stats.shapiro(data.iloc[:,0].dropna())
            st.write(f"P Value: {shapiro_test.pvalue:.5f}")
            if shapiro_test.pvalue > 0.05:
                st.success("There is insufficient evidence to reject the hypothesis of normality of the data")

            else:
                st.warning("There is sufficient evidence to reject the hypothesis of normality of the data")




    except Exception as e:
        st.error(f"File Prossessing Error: {e}")