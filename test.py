import requests
import pickle 
import datasets
import requests
import base64
import pandas as pd
import prep 

df=pd.read_csv("data.csv")

url="http://localhost:9696/predict"

dic=df.to_json() 

response=requests.post(url,json=dic)
print(response.json())


#this part is for local ttesting before using flask after loading df

# y1, X=prep.prep(df)
# pred=predict.predict(X)
# ab=pd.DataFrame({'Predicted Count':pred})
# ab['Predicted Count']=ab['Predicted Count'].apply(lambda x:int(x))
# print(ab)
