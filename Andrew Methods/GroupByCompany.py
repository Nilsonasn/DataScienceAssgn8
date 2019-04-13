import pandas as pd

def GroupByCompany():
    df = pd.read_csv("../Stocks/Nasdaq-Friday-April-20-2018.csv")
    companies = df['Symbol'].values
    companies = list(dict.fromkeys(companies))
    i = 0
    companyDF = []
    while (i<len(companies)):
        companyDF.append(df[df['Symbol']==companies[i]])
        companyDF[i].to_csv('../Stocks_By_Company/'+companies[i]+'.csv')
        i = i +1
    print(companyDF[1])
    
    
GroupByCompany() 
