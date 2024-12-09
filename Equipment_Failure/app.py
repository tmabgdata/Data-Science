import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

st.set_page_config(page_title="probability of equipment failures")
st.title("probability of equipment failures")

with st.sidebar:
    st.header("Settings")
    type = st.radio("Select Calculation", options=["Exact probability", "Less than", "More than"])
    occurrence = st.number_input("current_occurrence", min_value=1, max_value=99, value=2)
    process = st.button("process")

if process:
    lamb = occurrence
    start = lamb -2
    end = lamb +2
    x_vals = np.arange(start,end+1)

    if type == "Exact probability":
        probs = poisson.pmf(x_vals, lamb)
        tit = "Probabilities of occurrence"
    elif type == "Less than":
        probs = poisson.cdf(x_vals, lamb)
        tit = "Probabilities of occurrence equal to or less than"
    else:
        probs = poisson.sf(x_vals, lamb)
        tit = "Probabilities of occurrence more than"

    z_vals = np.round(probs, 4)

    labels = [f"{i} prob.: {p}" for i,p in zip(x_vals, z_vals)]

    fig, ax = plt.subplots()
    ax.bar(x_vals, probs, tick_label=labels, color = plt.cm.gray(np.linspace(0.4,0.8,len(x_vals))))
    ax.set_title(tit)
    plt.xticks(rotation = 45, ha = "right")
    plt.tight_layout()
    st.pyplot(fig)
