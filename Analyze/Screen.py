"""-----------------------------------------------------------------------------------
Stock screener will make buy recommendations by using regressed price, discount cash flow, 
and ratios. 
-----------------------------------------------------------------------------------"""    

from Analyze import DiscountedModel  # @UnresolvedImport
from Analyze import GetData  # @UnresolvedImport
from Analyze import Ratios  # @UnresolvedImport
from Analyze import Regression  # @UnresolvedImport
from Analyze import ReproductionEPV  # @UnresolvedImport
from Analyze import Value  # @UnresolvedImport
from HistoricalPricesData import Interface as HistoricalPrices  # @UnresolvedImport
from RegressionData import Interface as RegressionData  # @UnresolvedImport
import Utility

def screen(tickerName):
    getData = GetData.getData(tickerName)
    f = Ratios.TickerFundamentals(tickerName, getData)
    fcfNow, fcfAvg, value, valueAvg = Value.getValue(tickerName, getData)
    debtToAssets = f.getDebt()
    goodwill = f.getGoodwill()
    ROIC = f.getROIC()[1][0]
#     return ROIC
    todaysPrice = HistoricalPrices.getTodaysPriceOffline(tickerName)
    price_thresholdBuy = todaysPrice + (todaysPrice) * .20
    
    print(tickerName)
    print("Todays Price = " + str(todaysPrice))
    print("ROIC = " + str(ROIC))
    print("FCF Now : " + "{:,}".format(fcfNow))
    print("FCF 3yr Avg : " + "{:,}".format(fcfAvg))
    print("Approximate Value (10% discount rate) at [no growth, low growth, high growth]: " + str(value))
    print("Approximate Value using 3yr Avg (10% discount rate) at [no growth, low growth, high growth]: " + str(valueAvg))
    if(debtToAssets > 0.75):
        print("WARNING : Debt is very high")
    if(goodwill > .5):
        print("WARNING : Intangible Assets very high")
    print("")


def showAnalysis(tickerName):
    getData = GetData.getData(tickerName)
    f = Ratios.TickerFundamentals(tickerName, getData)
    value = Value.getValue(tickerName, getData)
    debtToEquity = f.getDebt()[0][0]
    debtToAssets = f.getDebt()[1][0]
    goodwill = f.getGoodwill()[0]
    ROIC = sum(f.getROIC()[1])/len(f.getROIC()[1])
    
    todaysPrice = HistoricalPrices.getTodaysPriceOffline(tickerName)
    price_thresholdBuy = todaysPrice + (todaysPrice) * .20
 
    """Screen Debt to Equity / Debt to Assets / Goodwill to Assets
    average DtE  1.3734983030849515
    average DtA 0.3840499950252389
    average Goodwill to assets  0.26169776351155205
    """
    if(debtToEquity > 1.3 or debtToEquity < 0):
        print('Debt To Equity too high')
    if(debtToAssets > 0.4):
        print('Debt To Assets too high')
    if(goodwill > .3):
        print('Goodwill too high')

    if(debtToEquity > 1.3 or debtToEquity < 0):
        print("Debt is very high")
    if(debtToAssets > 0.75):
        return
    if(goodwill > .5):
        return
    print(tickerName + " - buy signal")
    print("Todays Price = " + str(todaysPrice))
    print("ROIC = " + str(ROIC))
    print("Value : " + str(value))
    print("")

def equityScreen(tickerName):
    getData = GetData.getData(tickerName)
    todaysPrice = HistoricalPrices.getTodaysPriceOffline(tickerName)
    
    equityValue = Value.getEquityValue(tickerName, getData)
    
    print(tickerName + " : " + str(todaysPrice))
    for i in equityValue:
        print(i)
        
# list = ['BRKB', 'UVE', 'AIG', 'CB', 'CINF', 'HIG', 'L', 'PGR', 'TRV', 'XL', 'ANAT', 'AFSI', 'ACGL', 'ESGR', 'NGHC', 'SIGI', 'Y', 'AFG', 'AHL', 'AXS', 'CNA', 'RE', 'FAF', 'KMPR', 'MKL', 'MCY', 'MTG', 'ORI', 'RDN', 'RNR', 'RLI', 'THG', 'VR', 'WRB', 'WTM', 'AMSF', 'AGII', 'EMCI', 'GBLI', 'IPCC', 'JRVR', 'SAFT', 'STFC', 'NAVG',
#         'BLMT', 'SFBC', 'SFST', 'C', 'JPM', 'PNC', 'STI', 'WFC', 'HOMB', 'BAC', 'GWB', 'STL', 'GNBC', 'NCBS', 'RNST', 'STBZ','OZRK', 'BBT', 'RF', 'HBHC', 'IBKC', 'PNFP', 'TRMK', 'BXS', 'FNB', 'FHN', 'CSFL']
#  
# for i in list:
#     print(i)
#     equityScreen(i)
#     print("")
    
