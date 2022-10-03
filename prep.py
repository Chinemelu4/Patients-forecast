import pandas as pd
import numpy as np

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


def prep(df):

    var=['Ozone (ppm)', 'Temperature','Patient Arrival_Resp']

    y = df['Patient Arrival_Resp'].copy()

    X=make_lags(df[var],lags=4)
    y = make_multistep_target(y, steps=30)

    y, X= y.align(X, join='inner', axis=0)


    y, X = y.align(X, join='inner', axis=0)

    return y, X
