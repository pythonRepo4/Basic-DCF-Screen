from IndexData import Sqlite as sql #@UnresolvedImport
from IndexData import GetSector #@UnresolvedImport
from Variables import * #@UnresolvedImport
import csv
from urllib import request
from bs4 import BeautifulSoup
import Utility

"""-----------------------------------------------------------------------

Database is called IndexData.db 

This database has a table called "list" with column
(CC0)

This list contains stocks to be actively analyzed.
Contains tickers > 2B market cap

Table: listIndustry with [tickerName, Sector, Industry, Empty, Empty] 
(C1 TEXT, C2 TEXT, C3 TEXT, C4 TEXT, C5 TEXT)

------------------------------------------------------------------------"""
def getList():
    returnArray = []
    
    tempData = sql.executeReturn("SELECT * FROM 'list'")
    
    for i in tempData:
        returnArray.append(i[0])
    return returnArray


def getIndustry():
    returnArray = []
    
    tempData = sql.executeReturn("SELECT * FROM 'listIndustry'")
    
    for i in tempData:
        returnArray.append(i)
    return returnArray


"""-----------------------------------------------------------------------------------
Add, Delete Tickers
-----------------------------------------------------------------------------------"""
def deleteTicker(tickerName):
    sql.execute("DELETE FROM list WHERE CC0 = ?", [tickerName])
    
# deleteTicker("DLPH")

def deleteTickerIndustryList(tickerName):
    sql.execute("DELETE FROM listIndustry WHERE C1 = ?", [tickerName])
    
def addTicker(tickerName):
    sql.execute("INSERT INTO list VALUES (?)", [tickerName])
    
def getTickerIndustryList(tickerName):
    return sql.executeReturn("SELECT * FROM listIndustry WHERE C1 = '" + tickerName + "'")[0]

def getCompetitors(tickerName):    
    industry = getIndustry()
    ticker = ''
    competitors = []
    
    for i in industry:
        if(i[0] == tickerName):
            ticker = i
    
    if(ticker == ''):
        return []
    
    for i in industry:
        if(i[1] == ticker[1] and i[2] == ticker[2]):
            competitors.append(i[0])
    
    return competitors
    
"""-----------------------------------------------------------------------------------
Vacuum database. Removes empty tables in sqlite database.
-----------------------------------------------------------------------------------"""
def vacuum():
    sql.execute("VACUUM", None)


# full = getList()
# delete = []
# list = ["AAL", "AAP", "AAPL", "AMAT", "AMD", "AMZN", "BA", "BBY", "CACC", "CMCSA", "CMG", "CTL", "DG", "DIS", "ENVA", "CVS", "FAST", "F", "FB", "FIVE", 
#         "GE", "GM", "GOOGL", "GWW", "IBM", "INTC", "IPGP", "JNJ", "JWN", "M", "MCD", "MO", "MU", "NVDA", "PZZA", "QCOM", "SBUX", "SWKS", "TGT", "WMT", "XOM", 
#         "WAB", "WDFC", "FIZZ", "YUM", "TSN", "THRM", "KMX", "T", "SJM", "MAR", "ACN", "ADS", "CBS", "CSCO", "CVX", "GLW", "EMN", "FL", "HD", "SHW", "VZ", "DIS"]
# for i in full:
#     if(i not in list):
#         print(i)
#         deleteTicker(i)
#         deleteTickerIndustryList(i)
# full = getList()
# 
# for i in full:
#     print(i)





    