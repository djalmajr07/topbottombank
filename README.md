# **BUSINESS UNDERSTANDING**

## **COMPANY NAME?**

`Top Bottom Bank`

## **WHAT IS THE BUSINESS MODEL?**

TopBank is a large banking company. It operates mainly in European countries offering financial products, from bank accounts to investments, including some types of insurance and investment products.

The company's business model is of the service type, that is, it sells banking services to its customers through physical branches and an online portal.

The company's main product is a bank account, in which the customer can deposit his salary, make withdrawals, deposits and transfer to other accounts. This bank account has no cost to the customer and is valid for 12 months, that is, the customer needs to renew the contract for this account to continue using it for the next 12 months.

## **WHAT CHALLENGE DOES THIS PROJECT AIM TO OVERCOME?**

According to TopBank's Analytics team, each customer who has this bank account returns a monetary amount of 15% of their estimated salary amount, if it is less than average, and 20% if this salary is greater than average, during the current period of your account. This amount is calculated annually.

As a result for this project is expected to have these questions answered.
* *What is the company's current Churn rate?*
* *How does the churn rate vary by month?*
* *What is the expected return in terms of revenue, if the company uses its model to avoid churn?*
* *How does the model perform in classifying customers as churns?*

# **BUSINESS ASSUMPTIONS**
- **estimated_salary** will be considered as annual salary, the value 11.50 must be checked it may be an input error.
- Imbalanced dataset, must be balanced to get a best performance.

# *MIND MAP*

![2022-02-03_07-39](https://user-images.githubusercontent.com/85264359/164578871-a73c9256-c26e-431c-9377-67c40ab8a1c7.png)

### **Dataset Description**

|Feature | Definition |  
|-------------| -------------- |
|RowNumber | The column number |
|CustomerID | Unique customer identifier |
|Surname | Customer's last name |
|CreditScore | The customer's Credit score for the consumer market |
|Geography | The country where the customer resides |
|Gender | The gender of the customer |
|Age | The age of the customer |
|Tenure | Number of years the client has been active |
|Balance | Monetary amount the customer has in their bank account |
|NumOfProducts | The number of products purchased by the customer at the bank |
|HasCrCard | Indicates whether or not the customer has a credit card |
|IsActiveMember | Indicates if the customer made at least one movement in the bank account within 12 months |
|EstimateSalary | Estimate of the client's monthly salary |
|Exited | Indicates whether or not the client is in Churn |

**References:**
https://www.kaggle.com/datasets/mervetorkan/churndataset

# **SOLUTION STRATEGY**

### IOT METHOD


### Input
1. Low purchase recurrence.
2. Customers ceasing to buy after a certain period.

## Output
1. What is the company's current Churn rate?
2. How does the churn rate vary by month?
3. What is the expected return in terms of revenue, if the company uses its model to avoid churn?
4. How does the model perform in classifying customers as churns?


## Tasks

1. What is the company's current Churn rate?
    - Annual, semiannual or monthly.
    - If 1 out of 20 customers cancel your product every month, that means the churn rate for your product will be 5%.
    - Find churn rate and do the monthly churn.

2. How does the churn rate vary by month?
    - Calculate monthly churn.
    - MRR CHURN = SUM (MRR of canceled customers)

3.What is the expected return in terms of revenue, if the company uses its model to avoid churn?
 - if this client is recovered how much he brings me based on salary
     - threshold
     - sorted list of people who are going to churn
     - which people to recover
     - LTV
     - Roc curve

4. How does the model perform in classifying customers as churns?
    - Show Recall, Precision and Acc.
    - Search for different reporting metrics.
    - make the score

# **PROJECT CYCLE**

## `Step 00. Settings and Data Extraction`
* Import of required libraries, packages and functions.
* Loading and checking available data via a CSV file.

## `Step 01. Data Description`
* Renaming of columns and checking the size of the dataset (assessing the need for tools to handle large volumes of data).
* Verification of data types in each column and type changes that are necessary for better treatment by the algorithms later
* Verification of missing data and decision on how to treat them (removal, artificial resampling, solution infeasibility)
* Brief statistical description of the numerical and categorical attributes in order to detect anomalies that are outside the scope of the problem, as well as the presence of possible outliers that will impact the performance of the algorithms later.

## `Step 02. Data Filtering`
* Filtering rows and deleting columns that do not contain information relevant to modeling or do not help to solve the problem.

## `Step 03. Feature Engineering`
Creation of variables (features) relevant to solving the problem

## `Step 04. Exploratory Data Analysis
* Isolated analysis of each feature and its relationship with the others.
* Exploration of the data in order to obtain an intuition of their distribution in the data space (embedding exploration).

## `Step 05. Data Preparation`
* Data preparation to help machine learning models learn and perform more accurately.
* Selection of the embedding space best suited to the problem

## `Step 06. Feature Selection`
* Selection of the most relevant features to train the models

## `Step 07. Hyperparameter Fine Tuning`
* Testing different machine learning models and selecting the one with the best performance based on the chosen metrics (silhouette score)
* Choosing the best values for each parameter from the tested models that maximize performance

## `Step 08. Model Training`
* Training the models with the best parameters found and measuring their performance

## `Step 09. Cluster Analysis`
* Visual inspection of the data space assembled by each model
* Analysis of the profile (attributes) of each cluster for each model trained
* Choice of the final model that presents the best performance

## `Step 10. Exploratory Data Analysis for Business`
* Creation and testing of business hypotheses and elaboration of answers to business questions

## `Step 11. Deploy to Production`
* Planning and implementation of the model deployment architecture
* Creation of the database that will be used to solve the problem


# **TOP 3 INSIGHTS**


# **BUSINESS RESULTS**

**Answering the proposed business questions**

1. What is the company's current Churn rate?
    - The base has 10k customers and 2037 of them exited the bank, it represents 20.37% of churn.



2. How does the churn rate vary by month?
    - I made an assumption about this dataset, I divided the hole 10k clients by 12 and considered them the clients of each month of the year.
    - It goes between 17-22%



3. What is the expected return in terms of revenue, if the company uses its model to avoid churn?
    - average of how much the bank invoices per customer and decide how much to give as a coupon, offer 3 strategies.



4. How does the model perform in classifying customers as churns?

    - With a sample of 1593 customers, this model can correctly classify 1496 representing 88% of assertiveness.

     CatBoost Accuracy = 0.91
           
           
     ![image](https://user-images.githubusercontent.com/85264359/164581465-7e044927-e5d1-4c4d-bd2d-17502459efdd.png)

5. What is the bank's profit with this customer?
   - On average the amount the bank earns is $18,761.21 by clients.

   - If offered $50 coupon to 200, it's possible to convert $3,752,242.00 from churn clients.
   - If offered $28.6 coupon to 350, it's possible to convert $9,380,604.00 from churn clients.
   - If offered $16.6 coupon to 600, it's possible to convert $11,256,724.70 from churn clients.

The bank is losing $6727686.22 in this dataframe because of the churn



The return of all clients in this dataframe are: $33355060.65

Using the knapsack approach with an incentive list with coupons of $200, $100 and $50 depending of the probability to client's churn can give:

Recovered Revenue: $2201386.62

Churn Loss Recovered: 32.72%

Investment: $10000

Profit: $2191386.62

ROI: 21913.87%

Potential clients recovered with the model: 133 clients


# **BUSINESS SOLUTION**

**The following image explains the deployment architecture used to solve this problem**


# **CONCLUSIONS**


# **LESSONS LEARNED**


