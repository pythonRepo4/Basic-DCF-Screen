from RegressionData import Sqlite as sql #@UnresolvedImport #@UnusedVariable

def insertRegressionData(tickerName, multipleLinear):
    tableName = tickerName 
    
    sql.execute('DROP TABLE IF EXISTS ' + tableName, None)
    sql.execute('CREATE TABLE ' + tableName + '(CC0 REAL, CC1 REAL, CC2 TEXT)', None)
    
    for i in multipleLinear:
        tempArray = [i[0],i[1],str(i[2])]
        sql.execute('INSERT INTO ' + tableName + ' VALUES (?,?,?)', tempArray)
        
        
def getRegressionData(tickerName):
    tableName = tickerName
    
    tempData = sql.executeReturn('SELECT * FROM ' + tableName)
    ML = []

    """Each i should have 
    [radjusted (float), regPrice (float), keywords (str) """
    for i in tempData:
        data = []
        data.append(float(i[0]))
        data.append(float(i[1]))
        
        keywordAdd = []
        stringToList = str(i[2])
        stringToList = stringToList[1:len(stringToList) - 2]
        
        keywordStr = stringToList.split("',")
    
        for keywords in keywordStr:
            tempKeywords = keywords.strip()[1:]

            keywordAdd.append(tempKeywords)
            
        data.append(keywordAdd)
        ML.append(data)
    
    return ML

def getAll():
    allTables = sql.executeReturn("SELECT name FROM sqlite_master WHERE type = 'table';")
    return allTables

def deleteTicker(tickerName):
    sql.execute('DROP TABLE IF EXISTS ' + tickerName, None)

# list = sql.executeReturn11('SELECT * FROM list')
# 
# count = 0
# while(list[count][0] != 'CHKP'):
#     count += 1
#     
# while(count < len(list)):
#     try:
#         i = list[count]
#         print(i)
#         data = getML(i[0])
#         insertML(i[0], data)
#         count +=1 
#     except:
#         count += 1
#         pass

# data = getML('AAPL')
# for i in data:
#     print(i)

"""-----------------------------------------------------------------------------------

Vacuum database. Removes empty tables in sqlite database.

-----------------------------------------------------------------------------------"""
def vacuum():
    sql.execute("VACUUM", None)