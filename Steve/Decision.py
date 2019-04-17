import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from sklearn import preprocessing
from sklearn.tree import DecisionTreeRegressor

le = preprocessing.LabelEncoder()
regressor = DecisionTreeRegressor(random_state=0)


##### decision tree regressor#####
####Read in the data

nyse = pd.read_csv('nyse.csv',#'C:/Users/slamr/.PyCharm2018.3/config/scratches/Stocks_by_company/ALOG.csv',
                   parse_dates=['date'])
nyse = nyse[['date', 'Symbol', 'Open', 'Close']]
nyse['date'] = nyse['date'].dt.strftime('%Y-%m-%d')
nyse['date'] = le.fit_transform(nyse['date'])
train = nyse[['Open', 'Close']]
train = np.array(train)
eighty = int(len(train) * .8)
test = train[eighty:, 0:1]
X = train[:eighty, 0:1]
y = train[:eighty, 1:]
y_test = train[eighty:, 1:]
regressor.fit(X, y)
y_pred = regressor.predict(test)

X_grid = np.arange(min(X), max(X), 0.01)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color='red', label = 'Original')
plt.plot(X_grid, regressor.predict(X_grid), color='blue', label = 'regressor')
plt.plot(y_pred, color = 'green', label = 'prediction')
plt.title('NYSE (Decision Tree Regression)')
plt.xlabel('date')
plt.ylabel('Profit')
plt.legend(loc='best')
plt.show()
#
#
# bhtg = pd.read_csv('C:/Users/slamr/.PyCharm2018.3/config/scratches/Stocks_by_company/BHTG.csv',
#                    parse_dates=['date'])
# bhtg = bhtg[['date', 'Close']]
# bhtg['date'] = bhtg['date'].dt.strftime('%Y-%m-%d')
#
# bhtg['date'] = le.fit_transform(bhtg['date'])
# bhtg = np.array(bhtg)
# eighty = int(len(bhtg) * .8)
# test = bhtg[eighty:, 1:]
# X = bhtg[:, 0:1]
# y = bhtg[:, 1]
# regressor.fit(X, y)
# y_pred = regressor.predict(test)
#
# X_grid = np.arange(min(X), max(X), 0.01)
# X_grid = X_grid.reshape((len(X_grid), 1))
# plt.scatter(X, y, color='red', label = 'Original')
# plt.plot(X_grid, regressor.predict(X_grid), color='blue', label = 'regressor')
# plt.plot(y_pred, color = 'green', label = 'prediction')
# plt.title('ALOG (Decision Tree Regression)')
# plt.xlabel('date')
# plt.ylabel('Profit')
# plt.legend(loc='best')
# plt.show()
