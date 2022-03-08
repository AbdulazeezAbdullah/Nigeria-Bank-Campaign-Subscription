# Nigeria-Bank-Campaign-Subscription

Kowepe bank of Nigeria conducted marketing campaigns via phone calls with their clients. The purpose of these campaigns is to prompt their clients to subscribe to a specific financial product of the bank (term deposit). This survey had been conducted with some selected individuals that the bank feel is the best representative of their clients so as to minimize the cost of the total client survey.

You have been contacted as a data scientist to find patterns and build predictive models on this dataset with the aim of forecasting the percentage of potential customers for the financial products of the bank

Data Description
Context The dataset contains information about marketing campaigns that were conducted via phone calls from a Nigerian banking institution to their clients. The purpose of these campaigns is to prompt their clients to subscribe to a specific financial product of the bank (term deposit). After each call was conducted, the client had to inform the institution about their intention of either subscribing to the product (indicating a successful campaign) or not (unsuccessful campaign). The final output of this survey will be a binary result indicating if the client subscribed ('yes') to the product or not ('no').

The data has been split into two groups: - training set (train.csv) - test set (test.csv) The training set should be used to build your machine learning models. For the training set, we provide the outcome (also known as the “ground truth”) for each customer

The dataset several rows (instances of calls to clients) and 21 columns (variables) which are describing certain aspects of the call. Please note that there are cases where the same client was contacted multiple times - something that practically doesn't affect the analysis as each call will be considered independent from another even if the client is the same.

Content The predictor variables (features) contained in the dataset can be divided into the following five sections 

1. Variables that describing attributes related directly to the client:
age
job : type of job (e.g. 'admin', 'technician', 'unemployed', etc)
marital: marital status ('married', 'single', 'divorced', 'unknown')
education: level of education ('basic.4y', 'high.school', 'basic.6y', 'basic.9y','professional.course', 'unknown','university.degree','illiterate')
default: if the client has credit in default ('no', 'unknown', 'yes')
housing: if the client has housing a loan ('no', 'unknown', 'yes')
loan: if the client has a personal loan ? ('no', 'unknown', 'yes')

2. Variables related to the last contact of the current campaign:
contact: type of communication ('telephone', 'cellular')
month: month of last contact
dayofweek: day of last contact
duration: call duration (in seconds)

3. Other variables related to the campaign(s):
campaign: number of contacts performed during this campaign and for this client
pdays: number of days passed by after the client was last contacted from a previous campaign
previous: number of contacts performed before this campaign and for this client
poutcome: outcome of previous marketing campaign ('nonexistent', 'failure', 'success')

4. Socioeconomic variables:
emp_var_rate: employment variation rate - quarterly indicator
cons_price_idx: consumer price index - monthly indicator
cons_conf_idx: consumer confidence index - monthly indicator
euribor3m: euribor 3 month rate - daily indicator
nr_employed: number of employees - quarterly indicator

Of course, the dataset also containt the variable subscribed which is the target variable, indicating if the client subscribed to the product ('yes':1) or not ('no':0).
