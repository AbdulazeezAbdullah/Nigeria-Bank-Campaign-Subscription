

import streamlit as st
import sys
import numpy as np
import sklearn


def load_model():
    with open('Gradient_Boost_Model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

data = load_model()

campaign_model = data["model"]

marital_encode = data["marital_encoder"]
education_encode = data["education_encoder"]
default_encode = data["default_encoder"]
loan_encode = data["loan_encoder"]
housing_encode = data["housing_encoder"]
contact_encode = data["contact_encoder"]
month_encode = data["month_encoder"]
day_of_week_encode = data["day_of_week_encoder"]
poutcome_encode = data["poutcome_encoder"]

def show_predict_page():
    st.header("Customer Churn Prediction")

    st.subheader("We need some informatuion to predict the customers who will subscribe or not")
    
    housing = (
                    'no', 'yes', 'unknown'
    )
    
    poutcome = (
                    'failure', 'nonexistent', 'success'
    )
    
    contact = (
                    'cellular', 'telephone'
    )
    
    day_of_the_week = (
                        'mon', 'tue', 'wed', 'thu', 'fri'
    )
    
    defaultt = (
                    'no', 'unknown', 'yes'        
    )
    
    education = (
                    'basic.4y',
                    'basic.6y',
                    'basic.9y',
                    'high.school',
                    'university.degree',
                    'professional.course',  
                    'illiterate',
                    'unknown'
    )
    
    loan = (
                'no', 'yes', 'unknown'
        
    )
    
    marital = (
                    'single',
                    'married',  
                    'divorced', 
                    'unknown'        
    )
    
    months = (
                    'mar', 'apr', 'may',  'jun', 'jul',  'aug', 'sep',  'oct', 'nov', 'dec'
    )
    
    st.write('  \n')
    # Variables that describe attribute related directly to the client
    st.write('Client Details')
    Marital = st.selectbox('Client marital status', marital)
    Education = st.selectbox('Client level of education', education)
    Default = st.selectbox('Client has credit in default', defaultt)
    Housing = st.selectbox('Client has a housing loan', housing)
    Loan = st.selectbox('Client has a personal loan', loan)
    
    st.write('  \n')
    # Socio-economic variable
    st.write('Socio-economic Details')
    Emp_var_rate = st.slider('Employment variation rate - quarterly indicator', min_value=-3.50, max_value=1.45, step=0.01)
    cons_price_idx = st.slider('Consumer price index - monthly indicator', min_value=46., max_value=48., step=0.0005)   
    cons_conf_idx = st.slider('Consumer confidence index - monthly indicator', min_value=-40., max_value=-15., step=0.01) 
    euribor3m = st.slider('Euribor 3 month rate', min_value=1.5, max_value=6.5, step=0.001)
    nr_employed = st.slider('Number of employees', min_value=4800, max_value=5300, step=1)
    
    st.write('  \n')
    # Variables related to the last contact of the current campaign
    st.write('Last Contact Info.')
    Contact = st.selectbox('Type of communication', contact)
    Month = st.selectbox('Month of last contact', months)
    Day_of_week = st.selectbox('Day of last contact', day_of_the_week)
    Duration = st.slider('Call duration (in seconds)', min_value=1., max_value=100., step=0.1)
    
    st.write('  \n')
    # Other variables for the campaign
    st.write('Others')
    previous = st.slider('No. of contacts performed before this campaign for the client', min_value=0, max_value=7, step=1)
    pdays = st.slider('No. of days passed by after client was last contacted from a previous campaign', min_value=0, max_value=999, step=1)
    Poutcome = st.selectbox('Outcome of previous marketing campaign', poutcome)
    Campaign = st.slider('No. of contacts performed during this campaign for the client', min_value=1, max_value=50, step=1)
    
    input = st.button('Predict Subscription')
    
    classes = ['not subscribe','subscribe']
    
    if input:
        input = np.array([[Campaign, cons_conf_idx,	cons_price_idx,	Contact, Day_of_week, Default, Duration, Education, Emp_var_rate, euribor3m, Housing, Loan, Marital, Month, 
                           nr_employed, pdays, Poutcome, previous]])
        
        input[:, 3] = contact_encode.transform( input[:, 3])
        input[:, 4] = day_of_week_encode.transform( input[:, 4])
        input[:, 5] = default_encode.transform( input[:, 5])
        input[:, 7] = education_encode.transform(input[:, 7])
        input[:, 10] = housing_encode.transform(input[:, 10])
        input[:, 11] = loan_encode.transform(input[:, 11])
        input[:, 12] = marital_encode.transform( input[:, 12])
        input[:, 13] = month_encode.transform( input[:, 13])
        input[:, 16] = poutcome_encode.transform( input[:, 16])
               
        
        predictions = campaign_model.predict(input)
        
        for category in predictions:
            campaign_category = classes[category]
    
        st.subheader(f'The client will  {campaign_category}')
