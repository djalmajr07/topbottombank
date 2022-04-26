import pickle
import inflection
import pandas       as pd
from imblearn       import combine   as c



class ChurnScore(object):
    def __init__(self):
    
        # model load
        self.model=pickle.load(open('/usr/src/topbottombank/src/model/catboost_cv1.pkl', 'rb'))

        #parameters load
        self.age                    =pickle.load( open('/usr/src/topbottombank/src/parameter/age_scaler.pkl', 'rb' ))
        self.credit_score           =pickle.load( open('/usr/src/topbottombank/src/parameter/credit_score.pkl', 'rb' ))
        self.estimated_salary       =pickle.load( open('/usr/src/topbottombank/src/parameter/estimated_salary_scaler.pkl', 'rb' ))
        self.tenure                 =pickle.load( open('/usr/src/topbottombank/src/parameter/tenure_scaler.pk1', 'rb'))
        self.balance                =pickle.load( open('/usr/src/topbottombank/src/parameter/balance_scaler.pk1', 'rb'))
        self.num_of_products        =pickle.load( open('/usr/src/topbottombank/src/parameter/num_of_products_scaler.pk1', 'rb'))
        self.balance_by_age         =pickle.load( open('/usr/src/topbottombank/src/parameter/balance_by_age_scaler.pk1', 'rb'))
        self.balance_by_num_of_prod =pickle.load( open('/usr/src/topbottombank/src/parameter/balance_by_num_of_prod_scaler.pk1', 'rb'))
        self.num_of_prod_by_age     =pickle.load( open('/usr/src/topbottombank/src/parameter/num_of_prod_by_age_scaler.pk1', 'rb'))
        

    def data_cleaning(self, df1):

        cols_old=['RowNumber', 'CustomerId', 'Surname', 'CreditScore', 'Geography',
            'Gender', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard',
            'IsActiveMember', 'EstimatedSalary', 'Exited']

        snakecase = lambda x: inflection.underscore(x)
        cols_new = list(map(snakecase, cols_old))
        df1.columns = cols_new
        self.df1 = df1

        return df1

    def feature_engeneering(self, df2):

        df2['balance_by_age']=df2['balance']/df2['age']
        df2['num_of_prod_by_age']=df2['num_of_products']/df2['age']
        df2['balance_by_num_of_prod']=df2['balance']/df2['num_of_products']
        cols_drop = ['row_number','customer_id','surname']
        df2 = df2.drop(cols_drop, axis=1)
        
        return df2

    def data_preparation(self,df3):
    
        df3 = pd.get_dummies( df3, prefix=['geography'], columns=['geography'] )
        df3 = pd.get_dummies( df3, prefix=['gender'], columns=['gender'] )
        df3 = pd.get_dummies( df3, prefix=['has_cr_card'], columns=['has_cr_card'] )
        df3 = pd.get_dummies( df3, prefix=['is_active_member'], columns=['is_active_member'] )
        
        df3['age']=self.age.transform(df3[['age']].values)
        df3['credit_score'] = self.credit_score.transform(df3[['credit_score']].values)
        df3['estimated_salary']=self.estimated_salary.transform(df3[['estimated_salary']].values)
        df3['tenure'] = self.tenure.transform(df3[['tenure']].values)
        df3['balance'] = self.balance.transform(df3[['balance']].values)
        df3['num_of_products'] = self.num_of_products.transform(df3[['num_of_products']].values)
        df3['balance_by_age'] = self.balance_by_age.transform(df3[['balance_by_age']].values)
        df3['balance_by_num_of_prod'] = self.balance_by_num_of_prod.transform(df3[['balance_by_num_of_prod']].values)
        df3['num_of_prod_by_age'] = self.num_of_prod_by_age.transform(df3[['num_of_prod_by_age']].values)
       


        print(df3.columns)
        
        
        important_cols = ['credit_score', 'age', 'tenure', 'balance', 'num_of_products','estimated_salary', 'balance_by_age', 'num_of_prod_by_age','balance_by_num_of_prod', 'geography_Germany',
                          'gender_Female','gender_Male','is_active_member_0', 'is_active_member_1']

        return df3[important_cols]


    def get_predictions(self, model,dataframe):

        yhat_proba = self.model.predict_proba(dataframe)

        # transform yhat_proba to 1D-array
        yhat_proba_1d = yhat_proba[:, 1].tolist()

        dataframe['customer_id']=self.df1.customer_id
        
        # include in dataframe
        dataframe = dataframe.copy()
        dataframe['prob_churn'] = yhat_proba_1d
        
        # reset index
        dataframe.reset_index(drop=True, inplace=True)
        return dataframe.to_json(orient='records')