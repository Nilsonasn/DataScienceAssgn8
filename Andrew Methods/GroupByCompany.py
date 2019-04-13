import pandas as pd

def GroupByCompany(readFile = "",write=False,writeFile=""):    
    df = pd.read_csv(readFile)
    companies = df['Symbol'].values
    companies = list(dict.fromkeys(companies))
    i = 0
    companyDF = []
    while (i<len(companies)):
        companyDF.append(df[df['Symbol']==companies[i]])
        if(write==True and not writeFile == ""):
            companyDF[i].to_csv(writeFile+'/'+companies[i]+'.csv')
        i = i +1
    return companyDF
    
GroupByCompany(readFile = "../Stocks/Nasdaq-Friday-April-20-2018.csv",write = False,writeFile = "../Stocks_By_Company")


