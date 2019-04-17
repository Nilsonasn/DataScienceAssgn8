import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing

month_list = {'January':'01', 'February':'02', 'March':'03', 'April':'04', 'May':'05', 'June':'06', 'July':'07',
              'August':'08', 'September':'09','October':'10', 'November':'11', 'December':'12'}

<<<<<<< HEAD
path = '../Stocks/SCAP/'
=======
# stocks = pd.read_csv('test.csv')
# stocks = stocks.replace('...', 0)

path = 'Stocks/'
>>>>>>> 7ca966c5a2730caf8428af878369bd09613018c4
# path = 'C:/Users/Steven/.PyCharm2018.2/config/scratches/stocks/'
# path = 'C:/Users/slamr/.PyCharm2018.3/config/scratches/Stocks/'
stocks = pd.DataFrame()
# test.to_csv('test1.csv')
for file in os.listdir(path):
    df = pd.read_csv(path + file)
    date = file.split(sep="-")
    date[4] = date[4].split('.', 1)[0]
    if date[2] in month_list:
        mon_yr = month_list[date[2]] + '/' + date[3] + '/' +  date[4]
        df['Stock'] = date[0]
        df['day'] = date[1]
        df['date'] = pd.to_datetime(mon_yr)
        stocks = stocks.append(df, ignore_index=True, sort=False)
    # test.to_csv('test2.csv')
#
stocks = stocks.sort_values(by = ['Symbol','date'], ascending=[True,True]).replace('...',0)
# stocks = stocks.sort_values(by = ['date'], ascending=[True]).replace('...',0)
# bhtg = stocks[stocks['Symbol' ] == 'BHTG'].set_index('date')
# bhtg.to_csv('bhtg.csv')
stocks.to_csv('test.csv')

compuniquenames = stocks.Symbol.unique()
companydict = {elem : pd.DataFrame(ignore_index = True) for elem in compuniquenames}

for key in companydict.keys():
    companydict[key] = stocks[:][stocks.Symbol == key]





#
# ####### Holt Winters ########
# alog = pd.read_csv('C:/Users/slamr/.PyCharm2018.3/config/scratches/Stocks_by_company/ALOG.csv',
#                    parse_dates=['date'])
# ea = pd.read_csv('C:/Users/slamr/.PyCharm2018.3/config/scratches/Stocks_by_company/EA.csv',
#                    parse_dates=['date'])
# imdz = pd.read_csv('C:/Users/slamr/.PyCharm2018.3/config/scratches/Stocks_by_company/IMDZ.csv',
#                    parse_dates=['date'])
# oclr = pd.read_csv('C:/Users/slamr/.PyCharm2018.3/config/scratches/Stocks_by_company/OCLR.csv',
#                    parse_dates=['date'])
# 
# eighty = int(len(alog) * .8)
# bhtg.index.freq = 'd'
# train, test = bhtg.iloc[:eighty, 5], bhtg.iloc[eighty:, 5]
# model = ExponentialSmoothing(train, seasonal='mul', seasonal_periods=12).fit()
# pred = model.predict(start=test.index[0], end=test.index[-1])
#
# plt.plot(train.index, train, label='Train')
# plt.plot(test.index, test, label='Test')
# plt.plot(pred.index, pred, label='Holt-Winters')
# plt.legend(loc='best')
# plt.show()