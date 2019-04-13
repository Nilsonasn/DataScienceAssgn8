import pandas as pd

def GroupByCompany(readFile = "",write=False,writeFile=""):    
    df = pd.read_csv(readFile, dtype=str)
    companies = df['Symbol'].values
    companies = list(dict.fromkeys(companies))
    i = 0
    companyDF = []
    while (i<len(companies)):
        companyDF.append(df[df['Symbol']==companies[i]])
        #if(write==True and not writeFile == ""):
            #companyDF[i].to_csv(writeFile+'/'+companies[i]+'.csv')
        i = i +1
    return companyDF
    
print(GroupByCompany(readFile = "test.csv",write = False,writeFile = "../Stocks_By_Company"))


