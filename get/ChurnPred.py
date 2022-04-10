import pickle
import inflection
import pandas       as pd
from imblearn       import combine   as c



class ChurnScore(object):
    def __init__(self):
    
        # model load
        self.model=pickle.load(open('/home/tc0019/DS/topbottom/parameter/catboost_cv1.pkl', 'rb'))

        #parameters load
        self.age                    =pickle.load( open('/home/tc0019/DS/topbottom/parameter/age_scaler.pkl', 'rb' ))
        self.credit_score           =pickle.load( open('/home/tc0019/DS/topbottom/parameter/credit_score.pkl', 'rb' ))
        self.estimated_salary       =pickle.load( open('/home/tc0019/DS/topbottom/parameter/estimated_salary_scaler.pkl', 'rb' ))
        self.tenure                 =pickle.load( open('/home/tc0019/DS/topbottom/parameter/tenure_scaler.pk1', 'rb'))
        self.balance                =pickle.load( open('/home/tc0019/DS/topbottom/parameter/balance_scaler.pk1', 'rb'))
        self.num_of_products        =pickle.load( open('/home/tc0019/DS/topbottom/parameter/num_of_products_scaler.pk1', 'rb'))
        self.balance_by_age         =pickle.load( open('/home/tc0019/DS/topbottom/parameter/balance_by_age_scaler.pk1', 'rb'))
        self.balance_by_num_of_prod =pickle.load( open('/home/tc0019/DS/topbottom/parameter/balance_by_num_of_prod_scaler.pk1', 'rb'))
        self.num_of_prod_by_age     =pickle.load( open('/home/tc0019/DS/topbottom/parameter/num_of_prod_by_age_scaler.pk1', 'rb'))
        

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

    def data_preparation(self,df5):
        
        df5['age']=self.age.transform(df5[['age']].values)
        df5['credit_score'] = self.credit_score.transform(df5[['credit_score']].values)
        df5['estimated_salary']=self.estimated_salary.transform(df5[['estimated_salary']].values)
        df5['tenure'] = self.tenure.transform(df5[['tenure']].values)
        df5['balance'] = self.balance.transform(df5[['balance']].values)
        df5['num_of_products'] = self.num_of_products.transform(df5[['num_of_products']].values)
        df5['balance_by_age'] = self.balance_by_age.transform(df5[['balance_by_age']].values)
        df5['balance_by_num_of_prod'] = self.balance_by_num_of_prod.transform(df5[['balance_by_num_of_prod']].values)
        df5['num_of_prod_by_age'] = self.num_of_prod_by_age.transform(df5[['num_of_prod_by_age']].values)
        df5=pd.get_dummies(df5, prefix=['geography'], columns=['geography'])
        df5=pd.get_dummies(df5,prefix=['gender'],columns=['gender'])
        df5=pd.get_dummies(df5,prefix=['has_cr_card'],columns=['has_cr_card'])
        df5=pd.get_dummies(df5,prefix=['is_active_member'],columns=['is_active_member'])

        
        important_cols = ['credit_score', 'age', 'tenure', 'balance', 'num_of_products','estimated_salary', 'balance_by_age', 'num_of_prod_by_age','balance_by_num_of_prod', 'geography_Germany',
                          'gender_Female','gender_Male','is_active_member_0', 'is_active_member_1']

        return df5[important_cols]


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