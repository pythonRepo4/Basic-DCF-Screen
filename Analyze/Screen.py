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
    todaysPrice = HistoricalPrices.getTodaysPriceOffline(tickerName)
    price_thresholdBuy = todaysPrice + (todaysPrice) * .20

    if(value[0] > price_thresholdBuy):
        if(debtToAssets > 0.75):
            print("Debt is very high")
        if(goodwill > .5):
            print("Goodwill very high")
        print(tickerName + " - buy signal")
        print("Todays Price = " + str(todaysPrice))
        print("ROIC = " + str(ROIC))
        print("FCF Now : " + "{:,}".format(fcfNow))
        print("FCF 3yr Avg : " + "{:,}".format(fcfAvg))
        print("Value : " + str(value))
        print("Value Avg : " + str(valueAvg))
        print("")
        return True
    
def getROIC(tickerName):
    getData = GetData.getData(tickerName)
    f = Ratios.TickerFundamentals(tickerName, getData)
    ROIC = f.getROIC()[1][0]
    return ROIC

def simpleAnalysis(tickerName):
    getData = GetData.getData(tickerName)
    fcf, fcf_3yr, cashDebt = Value.getPerShareValue(tickerName, getData)
    todaysPriceOffline = float(HistoricalPrices.getTodaysPriceOffline(tickerName))
    
    equity = todaysPriceOffline - cashDebt
    multiplier = equity / fcf
    multiplier_3yr = equity / fcf_3yr
    
    if(0 < multiplier and multiplier < 15):
        pass
    else:
        return
    
    todaysPriceOffline = str("{:,}".format(todaysPriceOffline))
    equity = str("{:,}".format(equity))
    multiplier = str("{:,}".format(multiplier))
    multiplier_3yr = str("{:,}".format(multiplier_3yr))
    
    output = ""
    output += tickerName.ljust(6) + " | Todays Price = " + todaysPriceOffline.ljust(6) + " | equity = " + equity.ljust(6) \
        + " | multiplier = " + multiplier.ljust(6) + " | 3yr_multiplier = " + multiplier_3yr.ljust(6)
    print(output)
        
# list = ['BRKB', 'UVE', 'AIG', 'CB', 'CINF', 'HIG', 'L', 'PGR', 'TRV', 'XL', 'ANAT', 'AFSI', 'ACGL', 'ESGR', 'NGHC', 'SIGI', 'Y', 'AFG', 'AHL', 'AXS', 'CNA', 'RE', 'FAF', 'KMPR', 'MKL', 'MCY', 'MTG', 'ORI', 'RDN', 'RNR', 'RLI', 'THG', 'VR', 'WRB', 'WTM', 'AMSF', 'AGII', 'EMCI', 'GBLI', 'IPCC', 'JRVR', 'SAFT', 'STFC', 'NAVG',
#         'BLMT', 'SFBC', 'SFST', 'C', 'JPM', 'PNC', 'STI', 'WFC', 'HOMB', 'BAC', 'GWB', 'STL', 'GNBC', 'NCBS', 'RNST', 'STBZ','OZRK', 'BBT', 'RF', 'HBHC', 'IBKC', 'PNFP', 'TRMK', 'BXS', 'FNB', 'FHN', 'CSFL']
#  
# for i in list:
#     print(i)
#     equityScreen(i)
#     print("")
    
