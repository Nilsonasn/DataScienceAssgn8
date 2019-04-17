import os
import pandas as pd

month_list = {'January':'01', 'February':'02', 'March':'03', 'April':'04', 'May':'05', 'June':'06', 'July':'07',
              'August':'08', 'September':'09','October':'10', 'November':'11', 'December':'12'}
days_list = {'Monday':'01', 'Tuesday':'02', 'Wednesday':'03', 'Thursday':'04', 'Friday':'05', 'Saturday':'06', 'Sunday':'07'}
# stocks = pd.read_csv('test.csv')
# stocks = stocks.replace('...', 0)

print('Nasdaq stocks')
path = 'Stocks/Nasdaq/'####Your Stocks Dir####    'C:/Users/Steven/Documents/GitHub/DataScienceAssgn8/Stocks/Nasdaq/'

stocks = pd.DataFrame()

for file in os.listdir(path):
    df = pd.read_csv(path + file)
    date = file.split(sep="-")
    date[4] = date[4].split('.', 1)[0]
    if date[2] in month_list:
        mon_yr = month_list[date[2]] + '/' + date[3] + '/' +  date[4]
        df['Stock'] = date[0]
        df['day'] = date[1]
        df['day_num'] = days_list[date[1]]
        df['date'] = pd.to_datetime(mon_yr)
        stocks = stocks.append(df, ignore_index=True, sort=False)


stocks = stocks.sort_values(by = ['Symbol','date'], ascending=[True,True]).replace('...',0)
stocks = stocks.replace('...', 0)
stocks.to_csv('nasdaq.csv')

print('NYCE stocks')
path = 'Stocks/NYSE/'####Your Stocks Dir####    'C:/Users/Steven/Documents/GitHub/DataScienceAssgn8/Stocks/Nasdaq/'
stocks = pd.DataFrame()

for file in os.listdir(path):
    df = pd.read_csv(path + file)
    date = file.split(sep="-")
    date[4] = date[4].split('.', 1)[0]
    if date[2] in month_list:
        mon_yr = month_list[date[2]] + '/' + date[3] + '/' +  date[4]
        df['Stock'] = date[0]
        df['day'] = date[1]
        df['day_num'] = days_list[date[1]]
        df['date'] = pd.to_datetime(mon_yr)
        stocks = stocks.append(df, ignore_index=True, sort=False)


stocks = stocks.sort_values(by = ['Symbol','date'], ascending=[True,True]).replace('...',0)
stocks = stocks.replace('...', 0)
stocks.to_csv('nyse.csv')


print('SCAP stocks')
path = 'Stocks/SCAP/'####Your Stocks Dir####    'C:/Users/Steven/Documents/GitHub/DataScienceAssgn8/Stocks/Nasdaq/'
stocks = pd.DataFrame()

for file in os.listdir(path):
    df = pd.read_csv(path + file)
    date = file.split(sep="-")
    date[4] = date[4].split('.', 1)[0]
    if date[2] in month_list:
        mon_yr = month_list[date[2]] + '/' + date[3] + '/' +  date[4]
        df['Stock'] = date[0]
        df['day'] = date[1]
        df['day_num'] = days_list[date[1]]
        df['date'] = pd.to_datetime(mon_yr)
        stocks = stocks.append(df, ignore_index=True, sort=False)


stocks = stocks.sort_values(by = ['Symbol','date'], ascending=[True,True]).replace('...',0)
stocks = stocks.replace('...', 0)
stocks.to_csv('scap.csv')