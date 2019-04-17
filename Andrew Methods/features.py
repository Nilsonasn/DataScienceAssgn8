import pandas as pd
from sklearn.tree import DecisionTreeRegressor
pd.options.mode.chained_assignment = None  # default='warn'

def AddFeature():
    Holidays = {"01/01/2018","01/15/2018","02/02/2018","02/13/2018","02/14/2018","02/19/2018","03/11/2018","03/17/2018","04/01/2018","05/05/2018","05/16/2018","05/28/2018","06/14/2018","06/17/2018","07/04/2018","09/03/2018","09/11/2018","10/08/2018","10/31/2018","11/04/2018","11/1/2018","11/23/2018","12/25/2018","12/31/2018","01/01/2019","01/21/2019","02/02/2019","02/14/2019","02/18/2019"}
    df = pd.read_csv("../Stocks_By_Company/NYSE/CRL.csv")
    print(df.shape)
    rows = df.shape[0]
    cols=df.shape[1]
    i = 0
    df["Holiday"]=0
    features = ["Open","High","Low","Net Chg","% Chg","52 Wk High","52 Wk Low","P/E","YTD % Chg","Holiday"]
    
    while(i<rows):
        if(df["date"][i] in Holidays):
            df["Holiday"][i]=1
        else:
            df["Holiday"][i]=0
        i=i+1            

    df = df.dropna(axis = 0, how ='any')

    print(df.shape)
    
    print(df.info())
    y = df["Close"]
    X = df[features]
    
    dt = DecisionTreeRegressor(min_samples_split=40, random_state=99)
    dt.fit(X, y)
    print(dt.feature_importances_)
    
def GroupByCompany(df):    
    companies = df['Symbol'].values
    companies = list(dict.fromkeys(companies))
    i = 0
    companyDF = []
    while (i<len(companies)):
        companyDF.append(df[df['Symbol']==companies[i]])        
        i = i +1
    return companyDF    

    
AddFeature();    
