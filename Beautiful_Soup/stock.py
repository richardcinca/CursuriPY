

import bs4 as bs
import urllib.request
import os
import datetime
import pandas_datareader.data as web
import pandas as pd
import requests
import matplotlib as plt

URL = urllib.request.urlopen("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")

soup_object = bs.BeautifulSoup(URL, features='lxml')
# print(soup_object)

table = soup_object.find('table',{"class":"wikitable sortable"},{"id":"constituents"})
# print(table)

def get_SpCompanies():
    list=[]
    for row in table.findAll("tr")[1:]:
        ticker= row.findAll("td")[0].text[:-1]
        # print(ticker)
        ticker_name = row.findAll("td")[1].text

        company={"symbol":f"{ticker}","company_name":f"{ticker_name}"}
        list.append(company)
    return list

sp_companies = get_SpCompanies()
print(sp_companies)

#############################
def config_startDate():
    while True:
        try:
            year=int(input("Year: "))
            month=int(input("  Month: "))
            day=int(input("     Day: "))
            start=datetime.datetime(year,month,day)
            return start
        except:
            print('Invalid input')

def config_endDate():
    while True:
        try:
            year=int(input("Year: "))
            month=int(input("  Month: "))
            day=int(input("     Day: "))
            end=datetime.datetime(year,month,day)
            return end
        except:
            print('Invalid input')

#############################
def searcher():
    sp_companies = get_SpCompanies()
    name=''
    symbols_list=[]
    while name!='exit.search':
        name = input('Please select company:')
        if name=='exit.search':
            break
        else:
            print(name)
            # name=input('Please select company:')
            for company in list(sp_companies):
                # print(company.get('company_name'))
                if name == company.get('company_name') or name == company.get('symbol'):
                    # print('YES')
                    # print(company.get('symbol'))
                    symbols_list.append(company.get('symbol'))
                    break
                elif name in company.get('company_name'):
                    print('Are you looking for:  ',company.get('company_name'))
                    name = input("Is this what you are looking for: ")
                    if name == "no":
                        break
                    elif name == "yes":
                        print(input('  press enter to append the company:  '))
                        name = company.get('company_name')
                        symbols_list.append(company.get('symbol'))
                        print(f"   '{company.get('company_name')}' was appended")
                        break
            else:
                print("  The company was not found")
    print(symbols_list)

    start=config_startDate()
    end=config_endDate()

    IEX_CLOUD_API_TOKEN = 'Tpk_059b97af715d417d9f49f50b51b1c448'
    token = IEX_CLOUD_API_TOKEN

    col_names = ['Symbol', 'CompanyName', 'Volume', 'Open', 'Low', 'High', 'Close']
    empty_df = pd.DataFrame(columns=col_names)

    for ticker in symbols_list:
        print(ticker)
        df = web.DataReader(f'{ticker}', 'yahoo', start, end)
        df.to_csv(f'{ticker}.csv')

    for ticker in symbols_list:
        api_url = f"https://sandbox.iexapis.com/stable/stock/{ticker}/quote?token={token}"
        data = requests.get(api_url).json()
        df = pd.DataFrame({
            'Symbol': [data['symbol']],
            'CompanyName': [data['companyName']],
            'Volume': [data['latestVolume']],
            'Open': [data['open']],
            'Low': [data['low']],
            'High': [data['high']],
            'Close': [data['close']]
        })
        empty_df = empty_df.append(df, ignore_index=True)

    return "Success"


#############################
def make_dir():
    directory=input("Please name the folder where you will save your work today: ")
    parent_dir="C:/Users/Richard/Desktop/scoalainformala/CursuriPY/Beautiful_Soup/"
    path=os.path.join(parent_dir,directory)
    os.mkdir(path)
    return f"Your directory named '{directory}' has been created"
# make_dir()

#################################





searcher()

