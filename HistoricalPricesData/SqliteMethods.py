from HistoricalPricesData import Sqlite as sql #@UnresolvedImport #@UnusedVariable
from HistoricalPricesData import Download #@UnresolvedImport
from IndexData import Interface as IndexData #@UnresolvedImport

"""-----------------------------------------------------------------------------------

This method will insert price history into sqlite database called HistoricalPrices.db
An array will be sent in the following table format: 

[0-date, 1-open, 2-high, 3-low, 4-close, 5-adj-price, 6-volume, 7-split-price ]

-----------------------------------------------------------------------------------"""
def insertMechanism(tickerName):
    data = Download.getHistoricalPrices(tickerName)
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
def updateAll():
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

def removeTicker(tickerName):
    sql.execute('DROP TABLE IF EXISTS ' + tickerName, None)
    
"""-----------------------------------------------------------------------------------

Vacuum database. Removes empty tables in sqlite database.

-----------------------------------------------------------------------------------"""
def vacuum():
    sql.execute("VACUUM", None)
