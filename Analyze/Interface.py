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
    list = IndexData.getList()
    buyList = []
    badList = []
      
    print('start')
    for i in list:
        if("Financial" in IndexData.getTickerIndustryList(i)[1]):
            continue
        try:
#             roic = screen(i)
#             if(roic > .3 and roic < .5):
#                 print(i)
#                 print(roic)
#                 buyList.append(i)
            if(screen(i) == True):
                buyList.append(i)
        except:
            print(i + ' ERROR')
            badList.append(i)
            

    print(badList)
    print(buyList)

# screenAll()

