# **BUSINESS UNDERSTANDING**

**Obs: To see the images in better quality please click on them, tks.**

## **COMPANY NAME?**

`Top Bottom Bank`

![image](https://user-images.githubusercontent.com/85264359/165324743-55ff8483-b15f-4857-87fd-a99a695016c0.png)


## **WHAT IS THE BUSINESS MODEL?**

TopBank is a large banking company. It operates mainly in European countries offering financial products, from bank accounts to investments, including some types of insurance and investment products.

The company's business model is of the service type, that is, it sells banking services to its customers through physical branches and an online portal.

The company's main product is a bank account, in which the customer can deposit his salary, make withdrawals, deposits and transfer to other accounts. This bank account has no cost to the customer and is valid for 12 months, that is, the customer needs to renew the contract for this account to continue using it for the next 12 months.

## **WHAT CHALLENGE DOES THIS PROJECT AIM TO OVERCOME?**

According to TopBank's Analytics team, each customer who has this bank account returns a monetary amount of 15% of their estimated salary amount, if it is less than average, and 20% if this salary is greater than average, during the current period of your account. This amount is calculated annually.

As a result for this project is expected to have these questions answered.

1. What is the company's current churn rate?
2. How the churn rate vary by monthly?
3. What is the expected return in terms of revenue if the company uses this model to avoid churn?
4. What is the model performance in find churn clients?
5. What is the bank profit if the recovery works as planed?

# **BUSINESS ASSUMPTIONS**
- **estimated_salary** will be considered as annual salary, the value 11.50 must be checked it may be an input error.
- To deal with imbalanced dataset I'm considering to give priority to models which use bagging.
- Due the lack of data, to calculate monthly churn the original dataset with lenth of 10k clients was divided by 12.

# *MIND MAP*

<!-- ![2022-02-03_07-39](https://user-images.githubusercontent.com/85264359/164578871-a73c9256-c26e-431c-9377-67c40ab8a1c7.png) -->
![image](https://user-images.githubusercontent.com/85264359/165290051-055883e3-728c-4773-8085-2b45ea0d0980.png)


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
1. What is the company's current churn rate?
2. How the churn rate vary by monthly?
3. What is the expected return in terms of revenue if the company uses this model to avoid churn?
4. What is the model performance in find churn clients?
5. What is the bank profit if the recovery works as planed?


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

### H2. Spain has the largest number of credit cards in the database.
**False** Spain has the lowest number of cards with 2477
**Note:** People who have a credit card give more churn
![image](https://user-images.githubusercontent.com/85264359/165285562-eae80212-9ff5-4304-947b-95f13d4f9494.png)

### H3. The female audience has a higher score than the male audience.
**False** Men and Women on average have the same score.
![image](https://user-images.githubusercontent.com/85264359/165285640-b8feed09-efc8-49ca-b044-f88441e1c942.png)

### H4. Men have more money than women in the bank.
**True** Men have more money in the bank than women and give less churn too.
![image](https://user-images.githubusercontent.com/85264359/165285705-ed34577c-455f-4c1a-a985-dd94da418b03.png)


# **MACHINE LEARNING APPLIED**
- Logistic Regression
- Decision Tree
- Random Forest
- SVM
- KNN
- Naive Bayes
- XGBoost
- Catboost

# Machine Learning Model Performance

**Single Performance**

![image](https://user-images.githubusercontent.com/85264359/173262089-63c64fc9-a2f2-4280-9c50-00982380fee3.png)

# Roc Curve of all models
Analysing these curves it's pretty simple, the algorithm which have the curve nearest to Y-axis up left corner is the one with the best performance, here we can spot at least 3 easily: Catboost, Random Forest and Xgboost. Even though they have a similar graph, catboost has a better Area Under the Curve.  

![model_roc_curves](https://user-images.githubusercontent.com/85264359/173262878-26843f59-b8fa-4570-96b6-ad89d60ec64c.png)

# Model performance on business values
It is now possible to analyze the metrics and compare the difference in performance between the current model used by the company (**Random Model**) and the model proposed by me.

Considering **42% of the base**(3186 customers) according to the chart it's possible to reach **around 83% of churn custumers**
![image](https://user-images.githubusercontent.com/85264359/173261856-4533e633-0914-4de0-b4fb-7fd3e7d4aef5.png)

Considering **42% of the base**(3186 customers) according tothe chart, it's possible to perform 2+ times better than a baseline model
- The lift curve uses the returned probability of a classification model to measure how the model is performing.
- The highest probability appear on the left of the graph, usually along with the highest Lift scores.
- The greater the area between the lift curve and the baseline, the better the model.
![image](https://user-images.githubusercontent.com/85264359/173261882-8a8ab6d0-cd6c-4ed5-aad2-8f4a1fb11693.png)

# **BUSINESS RESULTS**

**Answering the proposed business questions**

## Answers about the case



1. What is the company's current churn rate?
    - The base has 10k customers and 2037 of them exited the bank, it represents 20,37% of churn.



2. How the churn rate vary by monthly?
    - I made an assumption about this dataset, I divided the hole 10k clients by 12 and considered them the clients of each month of the year.
    - It goes between 17-22%



3. What is the expected return in terms of revenue if the company uses this model to avoid churn?
    - With a budget of $10.000 and coupons of $25 the expected ROI is **4198%**

        To calculate the Return of Investment (ROI), we'll use the **Mean Return** of all the Scenarios values. The ROI for each of the three options are:

        - **$200** ROI: **1388%**
        - **$100** ROI: **2299%**
        - **$50** ROI: **3225%**
        - **$25** ROI: **4198%**


4. What is the model performance in find churn clients?

    - With a  sample of 1593 customers, this model can classify correctly 1496 representing 88% of acertiveness.
<<<<<<< HEAD

                        precision    recall  f1-score   support

           0                  0.89      0.95      0.92      1593
           1                  0.74      0.52      0.61       407

           accuracy                               0.87      2000

           macro avg          0.82      0.74      0.77      2000

           weighted avg       0.86      0.87    ->0.86<-    2000




5. What is the bank profit if the recovery works as planed?
   - Simulation: **$25** coupon

        With a budget of $10.000,00, the **top 400 clients with the highest probabilities** would receive the coupon

        Of the top 400 clients, ***65%*** of them were **True Churns** and ***35%*** were **False Churns**

        Financial results:

        - If **all True Churn clients** were recovered - *Potential recovery*: **$1.049.386,00**
        - **False Churn** clients - *Waste*: **$3.500,00**

        Scenario analysis:




5. What is the bank profit if the recovery works as planed?
   - Simulation: **$25** coupon

        With a budget of $10.000,00, the **top 400 clients with the highest probabilities** would receive the coupon

        Of the top 400 clients, ***65%*** of them were **True Churns** and ***35%*** were **False Churns**

        Financial results:

        - If **all True Churn clients** were recovered - *Potential recovery*: **$1.049.386,00**
        - **False Churn** clients - *Waste*: **$3.500,00**

        Scenario analysis:


        - *Pessimistic*: **$419.754,00** recovered
        - *Realistic*: **$524.693,00** recovered
        - *Optimistic*: **$629.632,00** recovered
        - *Mean of scenarios*: **$419.754,00** recovered


# **BUSINESS SOLUTION**
 
**Google Sheets available to business team insert data and get prediction**
![image](https://user-images.githubusercontent.com/85264359/165323424-b36cfe69-8ab7-4ddb-8d6f-e1f2e42bf523.png)


**Clients Ranked accoding to their propensity score to leave the bank**
![image](https://user-images.githubusercontent.com/85264359/165323559-8770d0fd-2d08-4916-8227-cd60cb6d51fe.png)



**The following image explains the deployment architecture used to solve this problem**
![image](https://user-images.githubusercontent.com/85264359/165316902-00ae66c0-c5b5-4fe7-90a0-a4fcf3720f39.png)


**MLFlow with models trained and saved**
![image](https://user-images.githubusercontent.com/85264359/173261433-35becf27-c03f-463d-bac8-c2cb86f1fef6.png)

**MLFlow registration of catboost pre-deploy**
![image](https://user-images.githubusercontent.com/85264359/165322712-15bdd166-2386-422a-bfdf-36c55ace4cca.png)


**MLFlow catboost deployed, stage in production**
![image](https://user-images.githubusercontent.com/85264359/165322842-3688938a-e82f-4d9f-a7ea-4667337f4366.png)


# **CONCLUSIONS**
By applying LTR(learn to rank), which consists in rank the base in most prone clients to churn, it was possible to analyse their range and pass some options to business team act helping them to decide in which scenario it's the best to offer an coupon and try to recover the client and of course understand better how their clients behave when tend to leave the bank.

# Technologies

- Jupyter;
- VSCode;
- Mlflow;
- Google Scripts;
- Docker;
- Python.
 
# Deployment into production
- Back end: Heroku, Google Scripts ;
- Front end web: Google Sheets;
- Database: kaggle csv file.


# **LESSONS LEARNED**
- Register all models on MLFlow
- Shap method
- Wrapper method
- Learned a new model: Catboost

# **NEXT STEPS**
- Get more data.
- Combine different features.
- Test different embbedings and encodings.
- Work with more budget in an attempt to get back customers.
- Align with business team with range od probability of churn, they want to work with.
- Add analysis to understand if the churn occurences are diferent over clients with expected salary above and below the mean.


# Author

Djalma Luiz da Silva Junior



[<img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"/>](https://www.linkedin.com/in/djalmajunior07)

