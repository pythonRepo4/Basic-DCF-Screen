from EarningsData import Sqlite as sql #@UnresolvedImport


"""-----------------------------------------------------------------------------------

Returns earnings data from EarningsData.db

-----------------------------------------------------------------------------------"""
def getData(tickerName):   
    tempData = sql.executeReturn('SELECT * FROM ' + tickerName)
    data = []
    
    for i in tempData:
        tempArr = []
        for j in i:
            tempArr.append(j)
        data.append(tempArr)
    
    return data

"""-----------------------------------------------------------------------------------

Inserts into tickername (in stock.db) data variable. Data variable contains dates/
price/earnings data. Data will be fed into sqldata base as something like.

(dates, Revenue-Q,......etc)
(11/9/2016, 855000,......etc)

-----------------------------------------------------------------------------------"""
def insertSQL(tickerName, data):           
    """IF read directly from excel, data comes in like this:
    date...9/16/2016
    Revenue... 5000
    etc. """
    
    """If it is the other way around ex:
    date revenue etc...
    9/16/2016 """
    """Flip it so that it is input correctly """
    if('Price' not in data[0]):
        tempData = data
        data = []
        for i in range(0,len(tempData[0])):
            tempArray = []
            for j in range(0,len(tempData)):
                tempArray.append(tempData[j][i])
#             print(tempArray)
            data.append(tempArray)
             
    """ Make text CC1 TEXT, CC2 TEXT, .... """
    columnText = '('
    questionText = ''
              
    for i in range(0,len(data[0])):
        columnText += 'CC' + str(i) + ' TEXT,'
        questionText += '?,'
    columnText = columnText[0:len(columnText)-1] + ')'
    questionText = questionText[0:len(questionText)-1]
        
    """ Fix Data. Sometimes data comes in with rows that are mostly empty. Drop these rows"""
    temp = data
    data = []
    for i in temp:
        empty = 0
        for j in i:
            if(j == '' or j == ' ' or j == None):
                empty += 1
        
        if empty > 20:
            pass
        else:
            data.append(i)
            

    sql.execute('DROP TABLE IF EXISTS ' + tickerName, None)
    sql.execute('CREATE TABLE ' + tickerName + columnText, None)
      
    totalText = ''
    for i in data:
        totalText += '('
        for j in i:
            totalText += "'" + str(j) + "',"
        totalText = totalText[0:len(totalText) -1 ]
        totalText += '),'
    totalText = totalText[0:len(totalText)-1]
      
    sql.execute('INSERT INTO ' + tickerName + ' VALUES ' + totalText , None)

"""-----------------------------------------------------------------------------------

 getAll will return all tables currently in HistoricalPrices.db. 
 removeTicker will remove that table from the database. 

-----------------------------------------------------------------------------------"""
def getAll():
    allTables = sql.executeReturn("SELECT name FROM sqlite_master WHERE type = 'table';")
    return allTables

def deleteTicker(tickerName):
    sql.execute('DROP TABLE IF EXISTS ' + tickerName, None)

"""-----------------------------------------------------------------------------------

Vacuum database. Removes empty tables in sqlite database.

-----------------------------------------------------------------------------------"""
def vacuum():
    sql.execute("VACUUM", None)   
    
