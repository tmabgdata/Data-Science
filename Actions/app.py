import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
from datetime import date

st.set_page_config(page_title="Actions Viewer", layout="wide")
st.title("Actions Viewer")

with st.sidebar:
    selected_company = st.selectbox("Select the company to view:",
                                 ['AAPL','GOOGL','MSFT','AMZN','TSLA'] )
    start_date = st.date_input("Start Date", value=date(2020,1,1))
    end_date = st.date_input("End Date", value=date(2020,1,15))
    generate_charts = st.button("Generate Charts")

if generate_charts :
    data = yf.download(selected_company, start=start_date, end=end_date)
    if data.size > 0:
        tab1, tab2, tab3, tab4 = st.columns(4)
        with tab1:
            fig_close = go.Figure()
            fig_close.add_trace(go.Scatter(x=data.index, y=data['Adj Close'],
                            mode='lines', name='Adjusted Close Price'))
            fig_close.update_layout(title=f'Price History for {selected_company}',
                            xaxis_title='Date', yaxis_title='Price')
            st.plotly_chart(fig_close, use_container_width=True)
        with tab2:
            fig_volume = go.Figure()
            fig_volume.add_trace(go.Bar(x=data.index, y=data['Volume']))
            fig_volume.update_layout(title=f'Trading Volume for {selected_company}',
                            xaxis_title='Date', yaxis_title='Volume')
            st.plotly_chart(fig_volume, use_container_width=True)
        with tab3:
            fig_candle = go.Figure(data=[go.Candlestick(x=data.index,
                            open=data['Open'],
                            high=data['High'],
                            low=data['Low'],
                            close=data['Close'])])
            fig_candle.update_layout(title=f'Candlestick Chart for {selected_company}',
                            xaxis_title='Date', yaxis_title='Price')
            st.plotly_chart(fig_candle, use_container_width=True)
        with tab4:
            st.dataframe(data)

    else:
        st.error("Error loading data, please try again")