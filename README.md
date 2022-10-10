# Patients-forecast

## Problem
A hospital specializing in treating respiratory infections are looking to be able to efficiently manage resources efficiently, from medical utilities, medical disposables, waste, personel etc. They want to be able to plan adequately for future use helping them in their monthly planning and budgeting.

## Solution
From interaction with the personels in the hospital I discovered that the key driver of resource usage is the number of patients comming into the hospital, based on my analysis I discovered that there is a direct relationship between the number of pattients on a daily basis and the amount of resources both human and material expended. Therefore, in other to adequately determine the resources used, it is imperative to be able to estimate the number of patients comming into the hospital.

How do I then estimate the number of patients to be expecting on a monthly basis? Further consultations reveal that some respiratory issues are weather and environment related. Out of the several weather conditions that were analyzed, I discovered that temperature and the ozone reading was highly correlated to a significant level with number of patients comming in.

Based on this findings,I built a time-series model using this features (temperature and ozone) that would be able to estimate between 1-30 days in the future the number of expected patients daily. 

## Monitoring and evalutation

The project was experimentation intensive and I had to track the results of several experimentation techniques, from the number of suitable lags, algorithms performance and size, duration of input data etc. In other, to monitor this effectively, I used mlflow to track and monitor the artifacts and results of each experiment.

![Alt text](./img.png?raw=true "Optional Title")

## Prototype
I used streamlit for a prototype deployment in other to show how the model works before deployment

![Alt text](./img2.png?raw=true "Optional Title")

## Deployment
I used flask to build an API and also dockerized it for seamless deployment anywhere. I also intergrated cloud deployment using AWS Lambda
