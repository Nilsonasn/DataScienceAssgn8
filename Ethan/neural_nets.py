import pandas as pd
import os
import datetime
import numpy as np
import glob
import datefinder
import dateutil.parser as dparser
import warnings
warnings.filterwarnings("ignore")


from sklearn.neural_network import MLPClassifier
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split

path = glob.glob("SCAP/*.csv")
#path = glob.glob("stocks/Nasdaq-Friday-April-20-2018.csv")

data = pd.DataFrame()

info = []

right = 0
total = 0

for f in path:
    data = pd.read_csv(f)

    for row in range(len(data)):
        if data['Close'][row] == '...':
            data['Close'][row] = None
        if data['Open'][row] == '...':
            data['Open'][row] = None
        if data['High'][row] == '...':
            data['High'][row] = None
        if data['Low'][row] == '...':
            data['Low'][row] = None
        if data['YTD % Chg'][row] == '...':
            data['YTD % Chg'][row] = None

    data = data.drop(['Div','Yield','P/E'], axis=1)
    data = data.drop(['Unnamed: 0'], axis=1)
    data = data.dropna()
    data = data.reset_index(drop=True)

    size = len(data)
    psize = int(size * .8)
    if size >= 5:
        train = data.iloc[:psize-1,1:16]
        test = data.iloc[psize-1:,1:16]

        features = ['Open','High','Low','YTD % Chg']

        X = train[features]
        y = train['Close']

        mlp = MLPRegressor(hidden_layer_sizes=(10, 10, 10), max_iter=10000)
        mlp.fit(X, y)

        predictions = mlp.predict(test[features])

        presize = len(predictions)
        beginning = float(y[0])

        temp = [data['Name'][0], predictions[presize-1]-beginning]
        info += [temp]
        print(data['Symbol'][0])



best = pd.DataFrame(info, columns = ['Name','total'])
best = best.sort_values('total', ascending=False)


print(best.head(3))