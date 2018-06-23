from HistoricalPricesData import Sqlite as sql #@UnresolvedImport
from HistoricalPricesData import Download #@UnresolvedImport
from IndexData import Interface as IndexData #@UnresolvedImport
from urllib import request
from bs4 import BeautifulSoup

"""-----------------------------------------------------------------------------------

This method will insert price history into sqlite database called HistoricalPrices.db
An array will be sent in the following table format: 

[0-date, 1-open, 2-high, 3-low, 4-close, 5-adj-price, 6-volume, 7-split-price ]

-----------------------------------------------------------------------------------"""
def insertMechanism(tickerName, data):
    sql.execute('DROP TABLE IF EXISTS ' + tickerName, None)
    sql.execute('CREATE TABLE ' + tickerName + '(CC0 TEXT, CC1 TEXT, CC2 TEXT, CC3 TEXT, CC4 TEXT, CC5 TEXT, CC6 TEXT, CC7 TEXT)', None)
    
    totalText = ''
    for i in data:
        totalText += '('
        for j in i:
            totalText += "'" + str(j) + "',"
        totalText = totalText[0:len(totalText) -1 ]
        totalText += '),'
#             tempArray.append(j)
#         totalText += valuesText + ','
    
    totalText = totalText[0:len(totalText)-1]
    sql.execute('INSERT INTO ' + tickerName + ' VALUES ' + totalText , None)
    
"""-----------------------------------------------------------------------------------

Inserts brand new historical prices. To do this, first add csv from Yahoo Finance into
ExcelData folder. 

-----------------------------------------------------------------------------------"""
def newHistoricalPrices(tickerName):
    insertMechanism(tickerName, Download.getHistoricalPrices(tickerName))

# list = ['SNFCA', 'SONC', 'SP', 'BRKB', 'SPTN', 'SPSC', 'STFC', 'STBZ', 'SNC', 'SMCI', 'RUN', 'SYKE', 'SYNA', 'TTEC', 'ABCO', 'CHEF', 'ENSG', 'FLIC', 'NAVG', 'PRSC', 'TOWN', 'TCBK', 'TBK',
#        'TRST', 'TTMI', 'FOXA', 'USCR', 'UCTT', 'UBSH', 'UBNK', 'UEIC', 'ULH', 'UVSP', 'VBTX', 'VIA', 'VSEC' , 'WSBF', 'WERN' , 'WSBC' , 'WABC', 'WING', 'WRLD', 'XCRA']
# list = ['BRKB']
# good = []
# for i in list:
#     try:
#         print(i)
#         newHistoricalPrices(i)
#         good.append(i)
#     except:
#         print(i + ' : error')
# print('complete')
# print(good)

"""-----------------------------------------------------------------------------------

Returns all historical price data of tickername in the format:
[0-date, 1-open, 2-high, 3-low, 4-close, 5-adj-price, 6-volume, 7-split-price ]

-----------------------------------------------------------------------------------"""
def getHistoricalPrices(tickerName):
    tempData = sql.executeReturn( 'SELECT * FROM ' + tickerName)
    
    data = []
    
    for i in tempData:
        temp = [] 
        for j in i:
            temp.append(j)
        data.append(temp)
    
    return data

"""-----------------------------------------------------------------------------------
 
Returns all historical price data of tickername in the format:
[0-date, 1-split-price ]
 
-----------------------------------------------------------------------------------"""
def getHistoricalSplit(tickerName):
    tempData = sql.executeReturn('SELECT * FROM ' + tickerName)
    data = []
     
    for i in tempData:
        data.append([i[0], float(i[7])])
     
    return data

"""-----------------------------------------------------------------------------------

Updates Historical Price by scraping Yahoo Finance

-----------------------------------------------------------------------------------"""
def updateHistoricalPrice(tickerName):
    tableName = tickerName
    
    tempData = sql.executeReturn('SELECT * FROM ' + tableName)
    sqlData = []
    for i in tempData:
        temp = []
        for j in i:
            temp.append(j)
        sqlData.append(temp)
        
    newData = Download.updateHistoricalPrice(tickerName, sqlData) #@Unresolved
    
#     for i in newData:
#         print(i)
    
    insertMechanism(tickerName, newData)

"""-----------------------------------------------------------------------------------
 
 Update all historical prices

-----------------------------------------------------------------------------------"""
def updateAllHistoricalPrices():
    list = IndexData.getList()
    badlist = []
     
    for i in list:
        try:
            print(i)
            updateHistoricalPrice(i)
        except:
            badlist.append(i)
    print(badlist)

"""-----------------------------------------------------------------------------------

 getAll will return all tables currently in HistoricalPrices.db. 
 removeTicker will remove that table from the database. 

-----------------------------------------------------------------------------------"""
def getAll():
    allTables = sql.executeReturn("SELECT name FROM sqlite_master WHERE type = 'table';")
    return allTables

'''-----------------------------------------------------------------------------------
This function returns current price of tickerName
Works As of 11/24/2016
-----------------------------------------------------------------------------------'''
def getTodaysPriceOffline(tickerName):
    historicalPrice = getHistoricalSplit(tickerName)[0][1]
    return float(historicalPrice)
    
def getTodaysPriceOnline(tickerName):
    url2 = "http://finance.yahoo.com/quote/" + tickerName
    url1 = "https://www.google.com/finance?q=" + tickerName 
    historicalPrice = getHistoricalSplit(tickerName)[0][1]
    return float(historicalPrice)
    
    todaysPrice = -1.1
    htmlStr = ''
    index0 = 0 
    index1 = 0
    counter = 0
    gotPrice = False

    """Try google finance first """
    try:
        tempWebFile = request.urlopen(url1).read()
        tempData = BeautifulSoup(tempWebFile, "lxml")
        html = tempData.prettify()
        
        lines = tempData.find_all('meta')
         
        payload = ''
        price = ''
        for i in lines:
            marker = 'meta content="'
            line = str(i)
            index0 = line.find(marker)
     
            if(index0 != None):
                payload = line[index0 + len(marker):]
    #             print(payload)
                 
                index2 = payload.find('"')
                 
                price = payload[:index2]
                price = price.replace(',','')
                 
                try:
                    todaysPrice = float(price)
                    if(todaysPrice > 1 and todaysPrice * (0.5) <= historicalPrice and historicalPrice <= todaysPrice * (1.5) ):
                        return todaysPrice
                except:
                    pass
    except:
        pass
            
    """If doesn't work, try Yahoo finance"""
    try:
        tempWebFile = request.urlopen(url2).read()
        tempData = BeautifulSoup(tempWebFile,"lxml")
        html = tempData.prettify()  

        lines = tempData.find_all('span')
         
        payload = ''
        price = ''
        for i in lines:
    #         print(i)
            marker = 'span class="Trsdu(0.3s) Fw(b)'
            line = str(i)
            index0 = line.find(marker)
     
            if(index0 != None):
                payload = line[index0:]
                 
                index1 = payload.find('>')
                index2 = payload.find('<')
                 
                price = payload[index1+1:index2]
                price = price.replace(',','')
                 
                try:
                    todaysPrice = float(price)
                    if(todaysPrice > 1 and todaysPrice * (0.5) <= historicalPrice and historicalPrice <= todaysPrice * (1.5)):
                        return todaysPrice
                except:
                    pass
    except:
        pass


    return historicalPrice

"""-----------------------------------------------------------------------------------
Delete / Vacuum
-----------------------------------------------------------------------------------"""
def deleteTicker(tickerName):
    sql.execute('DROP TABLE IF EXISTS ' + tickerName, None)
def vacuum():
    sql.execute("VACUUM", None)

