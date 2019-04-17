import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from sklearn import preprocessing
from sklearn.tree import DecisionTreeRegressor
le = preprocessing.LabelEncoder()
regressor = DecisionTreeRegressor(random_state = 0)


####### Holt Winters ########
df = pd.read_csv('C:/Users/Steven/.PyCharm2018.2/config/scratches/test1.csv',  parse_dates=['date'])
alog = pd.read_csv('C:/Users/slamr/.PyCharm2018.3/config/scratches/Stocks_by_company/ALOG.csv',
                   parse_dates=['date'])
ea = pd.read_csv('C:/Users/slamr/.PyCharm2018.3/config/scratches/Stocks_by_company/EA.csv',
                   parse_dates=['date'])
imdz = pd.read_csv('C:/Users/slamr/.PyCharm2018.3/config/scratches/Stocks_by_company/IMDZ.csv',
                   parse_dates=['date'])
oclr = pd.read_csv('C:/Users/slamr/.PyCharm2018.3/config/scratches/Stocks_by_company/OCLR.csv',
                   parse_dates=['date'])

bhtg = pd.read_csv('C:/Users/slamr/.PyCharm2018.3/config/scratches/Stocks_by_company/BHTG.csv',
                   parse_dates=['date'])
bhtg = bhtg.drop(bhtg.filter(regex='Unnamed').columns, axis=1)
bhtg.reset_index(drop = True)
eighty = int(len(bhtg) * .8)
bhtg.index.freq = 'd'
train, test = bhtg.iloc[:eighty, 5], bhtg.iloc[eighty:, 5]
model = ExponentialSmoothing(train, seasonal='mul', seasonal_periods=12).fit()
pred = model.predict(start=test.index[0], end=test.index[-1])

plt.plot(train.index, train, label='Train')
plt.plot(test.index, test, label='Test')
plt.plot(pred.index, pred, label='Holt-Winters')
plt.title('Holt-Winters')
plt.legend(loc='best')
plt.show()

