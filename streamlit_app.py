import streamlit as st 
import numpy as np
import pandas as pd
from xgboost import XGBRegressor
import pickle
from matplotlib import pyplot

st.header("Patient Forecast")

model=pickle.load(open('xg_model.pkl', 'rb'))

spectra = st.file_uploader("upload file", type={"csv","excel"})
if spectra is not None:
    df = pd.read_csv(spectra)




def make_lags(ts, lags, lead_time=1):
    return pd.concat(
        {
            f'y_lag_{i}': ts.shift(i)
            for i in range(lead_time, lags + lead_time)
        },
        axis=1)



def make_multistep_target(ts, steps):
    return pd.concat(
        {f'y_step_{i + 1}': ts.shift(-i)
         for i in range(steps)},
        axis=1)

var=['Ozone (ppm)', 'Temperature','Patient Arrival_Resp']

num=st.sidebar.number_input('number of days predicted for',min_value=1,max_value=30,step=1)
num=int(num)

if st.sidebar.button('Predict'):
    col=['y_step_1', 'y_step_2', 'y_step_3', 'y_step_4', 'y_step_5', 'y_step_6',
    'y_step_7', 'y_step_8', 'y_step_9', 'y_step_10', 'y_step_11',
    'y_step_12', 'y_step_13', 'y_step_14', 'y_step_15', 'y_step_16',
    'y_step_17', 'y_step_18', 'y_step_19', 'y_step_20', 'y_step_21',
    'y_step_22', 'y_step_23', 'y_step_24', 'y_step_25', 'y_step_26',
    'y_step_27', 'y_step_28', 'y_step_29', 'y_step_30']
    
    y = df['Patient Arrival_Resp'].copy()
    
    X=make_lags(df[var],lags=4)
    y = make_multistep_target(y, steps=30)

    y, X= y.align(X, join='inner', axis=0)


    y_pred_1= pd.DataFrame(model.predict(X), index=X.index, columns=col).reset_index(drop=True)
    
    y_new=y_pred_1.copy()
    y_new=y_new['y_step_1'].to_list()
    pred2=y_pred_1.tail(1).values.tolist()[0]
    li=[]
    for no in pred2:
        no=int(no)
        li.append(no)
    pred2=li.copy()
    tab=pd.DataFrame({'Predicted Count':pred2[0:num]},index=range(1,num+1))
    st.sidebar.write(tab)
    y_new.extend(pred2)
    y_new=y_new[0:(30+num)]
    added=pd.DataFrame(y_new).head(30)

    y.reset_index(drop=True,inplace=True)

    pyplot.plot(y_new,label=f'new (forecast) for {num} days')
    pyplot.plot(y['y_step_1'], color='red',label='Patient Arrival (actual)')
    pyplot.plot(added, color='green',label='Patient Arrival (model)')
    pyplot.legend()
    st.pyplot(pyplot)