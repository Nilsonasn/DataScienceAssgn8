import pandas as pd
import os
import datetime
import numpy as np
import glob
import datefinder
import dateutil.parser as dparser

path = glob.glob("min/first/*.csv")
#path = glob.glob("stocks/Nasdaq-Friday-April-20-2018.csv")

data = pd.DataFrame()

# for f in path:
#     matches = list(datefinder.find_dates(f))
#     if len(matches) > 0:
#         d = matches[0]
#         stock = pd.read_csv(f)
#         stock['date'] = d
#         data = data.append(stock)
#     else:
#         datetime.datetime.strptime(f, '%a-%b-%d-%Y-%H_%M-PM')
#     data = data.append(stock)

for f in path:
    stock = pd.read_csv(f)
    data = data.append(stock).reset_index(drop=True)

print(data)

path = glob.glob("min/last/*.csv")

temp = pd.DataFrame()

# for f in path:
#     matches = list(datefinder.find_dates(f))
#     if len(matches) > 0:
#         d = matches[0]
#         stock = pd.read_csv(f)
#         stock['date'] = d
#         temp = temp.append(stock)

for f in path:
    stock = pd.read_csv(f)
    temp = temp.append(stock).reset_index(drop=True)

both = pd.merge(data,temp, on=['Name'], how='left',indicator='Exist')
both['Exist'] = np.where(both.Exist == 'both', True, False)
for row in range(len(both)):
    if both['Exist'][row]:
        if both['Close_y'][row] == '...':
            both['Close_y'][row] = None
    else:
        both = both.drop([row])

both = both.drop(['Div_x','Yield_x','P/E_x','Div_y','Yield_y','P/E_y'], axis=1)
both = both.dropna()

x = 9995

both['sum'] = x / both['Open_x']
both['sum'] = both['sum'].astype(int)

both['Close_y'] = both['Close_y'].astype(float)

both['total'] = both['sum']*both['Close_y']

print(both['sum'])
print(both.sort_values('total', ascending=False))
