from EarningsData import SqliteMethods #@UnresolvedImport
from EarningsData import Update #@UnresolvedImport
from EarningsData import Download #@UnresolvedImport
from EarningsData import ReadExcel #@UnresolvedImport

"""-----------------------------------------------------------------------------------
Returns earnings data from EarningsData.db
-----------------------------------------------------------------------------------"""
def getData(tickerName):       
    return SqliteMethods.getData(tickerName)

"""-----------------------------------------------------------------------------------
Download brand new stock data. NOTE, must first have price data in HistoricalPricesData
-----------------------------------------------------------------------------------"""
def fundamentalData(tickerName):
    Download.deleteAll(tickerName)
    Download.downloadAll(tickerName)
    data = ReadExcel.readExcel(tickerName)
    SqliteMethods.insertSQL(tickerName, data)

# list = ['SNFCA', 'SONC', 'SP', 'BRKB', 'SPTN', 'SPSC', 'STFC', 'STBZ', 'SNC', 'SMCI', 'RUN', 'SYKE', 'SYNA', 'TTEC', 'ABCO', 'CHEF', 'ENSG', 'FLIC', 'NAVG', 'PRSC', 'TOWN', 'TCBK', 'TBK',
#        'TRST', 'TTMI', 'FOXA', 'USCR', 'UCTT', 'UBSH', 'UBNK', 'UEIC', 'ULH', 'UVSP', 'VBTX', 'VIA', 'VSEC' , 'WSBF', 'WERN' , 'WSBC' , 'WABC', 'WING', 'WRLD', 'XCRA']
# list = ['BRKB']
# good = []
# for i in list:
#     try:
#         print(i)
#         fundamentalData(i)
#         good.append(i)
#     except:
#         print(i + ' : error ')
#    
# print(good)
# print('complete')


"""-----------------------------------------------------------------------------------
Update earnings data
-----------------------------------------------------------------------------------"""
def update(tickerName):
    updateData = Update.update(tickerName)


def updateByDate(tickerName):
    Update.updateByDate(tickerName)
    
def updateAll():
    Update.updateAll()

"""-----------------------------------------------------------------------------------
Get all 
-----------------------------------------------------------------------------------"""
def getAll():
    return SqliteMethods.getAll()

"""-----------------------------------------------------------------------------------
Delete/Vacuum
-----------------------------------------------------------------------------------"""
def deleteTicker(tickerName):
    SqliteMethods.deleteTicker(tickerName)

def vacuum():
    SqliteMethods.vacuum()

# all = getAll()
# for i in all:
#     print(i)

# deleteTicker("TCO")