import pickle
import pandas   as pd
from flask      import Flask, request, Response
from get.ChurnPred import ChurnScore
import os

model=pickle.load(open('model/catboost_cv1.pkl', 'rb'))


app=Flask(__name__)

@app.route('/')
def home():
    """Return a friendly HTTPS greeting."""
    return 'Hello Churn Predictions API is running'


@app.route('/getpred', methods=['POST'])
def getpred():
    test_json = request.get_json()
   
    if test_json: # there is data
        if isinstance( test_json, dict ): # unique example
            test_raw = pd.DataFrame( test_json, index=[0] )
            
        else: # multiple example
            test_raw = pd.DataFrame( test_json, columns=test_json[0].keys() )


        pipeline=ChurnScore()

        # data cleaning
        df1=pipeline.data_cleaning(test_raw)

        #feature engeneering
        df2=pipeline.feature_engeneering(df1)

        # data preparation
        df5=pipeline.data_preparation(df2)

        # prediction  
        df_response=pipeline.get_predictions(model,df5)

        return df_response
    else:
        return Response( '{}', status=200, mimetype='application/json' )

if __name__ == '__main__':
    port=os.environ.get('PORT',5000)
    app.run('0.0.0.0', port=port)
