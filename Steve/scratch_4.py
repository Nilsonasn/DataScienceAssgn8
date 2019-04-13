import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing

month_list = {'January':'01', 'February':'02', 'March':'03', 'April':'04', 'May':'05', 'June':'06', 'July':'07',
              'August':'08', 'September':'09','October':'10', 'November':'11', 'December':'12'}

path = 'Stocks/'
# path = 'C:/Users/Steven/.PyCharm2018.2/config/scratches/stocks/'
stocks = pd.DataFrame()
# test.to_csv('test1.csv')
for file in os.listdir(path):
    df = pd.read_csv(path + file)
    date = file.split(sep="-")
    date[4] = date[4].split('.', 1)[0]
    if date[2] in month_list:
        mon_yr = date[4] + '/' + month_list[date[2]] + '/' + date[3]
        df['Stock'] = date[1]
        df['day'] = date[1]
        df['date'] = mon_yr
        stocks = stocks.append(df, ignore_index=False, sort=False)
    # test.to_csv('test2.csv')

stocks = stocks.sort_values(by = ['Symbol', 'date'], ascending=[True, True])
# test.to_csv('test.csv')

stocks.index.freq = 'MS'
train, test = df.iloc[:130, 0], df.iloc[130:, 0]
model = ExponentialSmoothing(train, seasonal='mul', seasonal_periods=12).fit()
pred = model.predict(start=test.index[0], end=test.index[-1])