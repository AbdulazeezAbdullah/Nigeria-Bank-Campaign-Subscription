import streamlit as st
from predict_page import show_predict_page

st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)

logo = st.sidebar.image('bank.png')

information = st.sidebar.subheader('Background Information')
description = st.sidebar.markdown("Kowepe bank of Nigeria conducted marketing campaigns via phone calls with their clients. The purpose of these campaigns is to prompt their clients to subscribe to a specific financial product of the bank (term deposit). This survey had been conducted with some selected individuals that the bank feel is the best representative of their clients so as to minimize the cost of the total client survey.  \n  \nYou have been contacted as a data scientist to find patterns and build predictive models on this dataset with the aim of forecasting the percentage of potential customers for the financial products of the bank.  \n  \nDatasource: https://www.kaggle.com/c/data-science-nigeria-bank-campaign-subscriptions/overview")

show_predict_page()