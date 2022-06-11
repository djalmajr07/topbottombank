import pickle
import inflection
import pandas       as pd
from imblearn       import combine   as c



class ChurnScore(object):
    def __init__(self):
    
        # model load
        self.model=pickle.load(open('model/catboost_cv1.pkl', 'rb'))

        #parameters load
        self.age                    =pickle.load( open('parameter/age_scaler.pkl', 'rb' ))
        self.credit_score           =pickle.load( open('parameter/credit_score_scaler.pkl', 'rb' ))
        self.estimated_salary       =pickle.load( open('parameter/estimated_salary_scaler.pkl', 'rb' ))
        self.tenure                 =pickle.load( open('parameter/tenure_scaler.pk1', 'rb'))
        self.balance                =pickle.load( open('parameter/balance_scaler.pk1', 'rb'))
        self.num_of_products        =pickle.load( open('parameter/num_of_products_scaler.pk1', 'rb'))
        self.balance_by_age         =pickle.load( open('parameter/balance_by_age_scaler.pk1', 'rb'))
        self.balance_by_num_of_prod =pickle.load( open('parameter/balance_by_num_of_prod_scaler.pk1', 'rb'))
        self.num_of_prod_by_age     =pickle.load( open('parameter/num_of_prod_by_age_scaler.pk1', 'rb'))
        

    def data_cleaning(self, df_raw):

        cols_old=['RowNumber', 'CustomerId', 'Surname', 'CreditScore', 'Geography',
            'Gender', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard',
            'IsActiveMember', 'EstimatedSalary', 'Exited']

        snakecase = lambda x: inflection.underscore(x)
        cols_new = list(map(snakecase, cols_old))
        df_raw.columns = cols_new
        # self.df1 = df_raw

        return df_raw

    def feature_engeneering(self, df1):
        # df1['num_of_products'] = df1['num_of_products'].astype(float)
        # df1['age'] = df1['age'].astype(float)
        # df1['balance'] = df1['balance'].astype(float)

        df1['num_of_prod_by_age']=df1['num_of_products']/df1['age']
        df1['balance_by_num_of_prod']=df1['balance']/df1['num_of_products']
        df1['balance_by_age']=df1['balance']/df1['age']

        cols_drop = ['row_number','customer_id','surname']
        df1 = df1.drop(cols_drop, axis=1)

        return df1

    def data_preparation(self,df2):
        

        df2.loc[df2['geography']=='France', 'geography_France']=1 
        df2.loc[df2['geography']=='Germany', 'geography_Germany']=1 
        df2.loc[df2['geography']=='Spain', 'geography_Spain']=1 

        df2.loc[df2['gender']=='Female', 'gender_Female']=1 
        df2.loc[df2['gender']=='Male', 'gender_Male']=1 

        df2.loc[df2['has_cr_card']==0, 'has_cr_card_0']=1 
        df2.loc[df2['has_cr_card']==1, 'has_cr_card_1']=1 

        df2.loc[df2['is_active_member']==0, 'is_active_member_0']=1 
        df2.loc[df2['is_active_member']==1, 'is_active_member_1']=1 

        df2=df2.fillna(0)

        df2['age']=self.age.transform(df2[['age']].values)
        df2['credit_score'] = self.credit_score.transform(df2[['credit_score']].values)
        df2['estimated_salary']=self.estimated_salary.transform(df2[['estimated_salary']].values)
        df2['tenure'] = self.tenure.transform(df2[['tenure']].values)
        df2['balance'] = self.balance.transform(df2[['balance']].values)
        df2['num_of_products'] = self.num_of_products.transform(df2[['num_of_products']].values)
        df2['balance_by_age'] = self.balance_by_age.transform(df2[['balance_by_age']].values)
        df2['balance_by_num_of_prod'] = self.balance_by_num_of_prod.transform(df2[['balance_by_num_of_prod']].values)
        df2['num_of_prod_by_age'] = self.num_of_prod_by_age.transform(df2[['num_of_prod_by_age']].values)


        
        important_cols = ['credit_score', 'age', 'tenure', 'balance', 'num_of_products','estimated_salary', 'balance_by_age', 'num_of_prod_by_age','balance_by_num_of_prod', 'geography_Germany',
                          'gender_Female','gender_Male','is_active_member_0', 'is_active_member_1']

        return df2[important_cols]


    def get_predictions(self, model,df3):

        yhat_proba = self.model.predict_proba(df3)

        # transform yhat_proba to 1D-array
        yhat_proba_1d = yhat_proba[:, 1].tolist()

        # df3['customer_id']=self.df1.customer_id
        
        # include in df3
        df3 = df3.copy()
        df3['prob_churn'] = yhat_proba_1d
        
        # reset index
        df3.reset_index(drop=True, inplace=True)
        return df3.to_json(orient='records')
