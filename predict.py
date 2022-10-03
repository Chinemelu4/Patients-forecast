import pickle
from urllib import request
import pandas as pd 
import base64
import pickle 
import prep
from flask import Flask, request, jsonify

with open('xg_model.pkl','rb') as f_in:
    (model)=pickle.load(f_in)

col=['y_step_1', 'y_step_2', 'y_step_3', 'y_step_4', 'y_step_5', 'y_step_6',
    'y_step_7', 'y_step_8', 'y_step_9', 'y_step_10', 'y_step_11',
    'y_step_12', 'y_step_13', 'y_step_14', 'y_step_15', 'y_step_16',
    'y_step_17', 'y_step_18', 'y_step_19', 'y_step_20', 'y_step_21',
    'y_step_22', 'y_step_23', 'y_step_24', 'y_step_25', 'y_step_26',
    'y_step_27', 'y_step_28', 'y_step_29', 'y_step_30']

def predict(X):
    y_pred_1= pd.DataFrame(model.predict(X), index=X.index, columns=col).reset_index(drop=True)
    pred2=y_pred_1.tail(1).values.tolist()[0]
    return pred2

#stop here to carry out test with test.py without using flask

app= Flask('patients-prediction')

@app.route('/predict', methods=['POST'])


def predict_endpoint():
    dic=request.get_json()
    df=pd.DataFrame(eval(dic))

    y1,X=prep.prep(df)
    pred=predict(X)
    #tab=pd.DataFrame({'Predicted Count':pred})
    #tab['Predicted Count']=tab['Predicted Count'].apply(lambda x:int(x))
    pred=[round(item) for item in pred]
    result = {'duration':pred}
    return result

if __name__ =="__main__":
    app.run(debug=True, host="0.0.0.0", port=9696)