from Analyze import Ratios #@UnresolvedImport
from Analyze import Regression #@UnresolvedImport
from Analyze import Screen #@UnresolvedImport
from Analyze import Value #@UnresolvedImport
from IndexData import Interface as IndexData #@UnresolvedImport


"""-----------------------------------------------------------------------------------
Analysis Functions
-----------------------------------------------------------------------------------""" 
def updateSingleRegression(tickerName):
    Regression.MLanalysis(tickerName)
    
def showAnalysis(tickerName):
    Screen.showAnalysis(tickerName)

def screen(tickerName):
    return Screen.screen(tickerName)


"""-----------------------------------------------------------------------------------
Screen All
-----------------------------------------------------------------------------------""" 
def screenAll():
#     noBuy = ["IDCC", ""]
    list = IndexData.getList()
#     list = ['ROL', 'TSE', 'UNH', 'AMAT', 'BBY', 'HRB', 'CHRW', 'CELG', 'CI', 'CLX', 'CL', 'EW', 'EA', 'GRMN', 'HAS', 'HUM', 'KLAC', 'LB', 'LRCX', 'LYB', 'MAS', 'MCD', 'MTD', 'MU', 'MSFT', 'MNST', 'MSI', 'NVDA', 'REGN', 'RHI', 'ROK', 'SHW', 'TXN', 'HSY', 'UPS', 'VAR', 'INCY', 'MXIM', 'SIRI', 'ABMD', 'AZPN', 'CDNS', 'CDK', 'CBPO', 'CRUS', 'CGNX', 'FIVE', 'LOPE', 'HA', 'HQY', 'LSTR', 'LOGI', 'LULU', 'LITE', 'MTCH', 'PZZA', 'PPC', 'SAFM', 'STMP', 'BIO', 'BURL', 'BWXT', 'CC', 'ENR', 'EPAM', 'GDDY', 'GGG', 'HLF', 'LPI', 'LEA', 'LII', 'LPX', 'RES', 'NOW', 'TNH', 'THO', 'TTC', 'VEEV', 'VC', 'WBC', 'WSM', 'YELP', 'PZZA', 'PZZA', 'DENN', 'IRBT', 'KBAL', 'QLYS', 'RUTH', 'PRSC', 'UCTT', 'WING']
    buyList = []
    badList = []
      
    print('start')
    for i in list:
        if("Financial" in IndexData.getTickerIndustryList(i)[1]):
            continue
        try:
            Screen.simpleAnalysis(i)
#             roic = Screen.getROIC(i)
#             print(i)
#             print(roic)
#             if(roic > .3 and roic < .5):
#                 print(i)
#                 print(roic)
#                 buyList.append(i)

#             """Screen """
#             if(screen(i) == True):
#                 buyList.append(i)
        except:
            print(i + ' ERROR')
            badList.append(i)
            

    print(badList)
    print(buyList)
