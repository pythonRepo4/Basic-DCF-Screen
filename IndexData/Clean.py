from HistoricalPricesData import Interface as HistoricalPricesData #@UnresolvedImport
from EarningsData import Interface as EarningsData #@UnresolvedImport
# from RegressionData import Interface as RegressionData #@UnresolvedImport
from IndexData import Interface as IndexData #@UnresolvedImport


"""-----------------------------------------------------------------------------------
Clean databases. Sometimes tickers are removed from list. This does not delete ticker from
other databases so there is garbage left in these databases. This function will remove
from the following databases/tables: 

IndexData - listIndustry Table 
RegressionData
FundamentalsData
HistoricalPricesData
-----------------------------------------------------------------------------------"""
# def cleanOtherDatabases():
#     print("start")
#     temp = IndexData.getList()
#     currentList = []
#      
#     for i in temp:
#         currentList.append(i)
#          
#     earningsData = EarningsData.getAll()
#     for i in earningsData:
#         if(i[0] not in currentList):
#             EarningsData.deleteTicker(i[0])
#     EarningsData.vacuum()
      
#     regressionData = RegressionData.getAll()
#     for i in regressionData:
#         if(i[0] not in currentList):
#             RegressionData.deleteTicker(i[0])
#     RegressionData.vacuum()
#      
#     historicalData = HistoricalPricesData.getAll()
#     for i in historicalData:
#         if(i[0] not in currentList):
#             HistoricalPricesData.deleteTicker(i[0])
#     HistoricalPricesData.vacuum()
# 
#     print('complete')
# 
# cleanOtherDatabases()