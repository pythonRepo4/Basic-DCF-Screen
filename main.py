from Analyze import Interface as Analyze #@UnresolvedImport
from IndexData import Interface as IndexData #@UnresolvedImport
from HistoricalPricesData import Interface as HistoricalPricesData  #@UnresolvedImport
from EarningsData import Interface as EarningsData #@UnresolvedImport
import Utility


"""-----------------------------------------------------------------------------------
The following stocks can be analyzed using this program and database: 

['GOOGL', 'AAPL', 'CMCSA', 'CACC', 'FB', 'FAST', 'THRM', 'IPGP', 'QCOM', 'SWKS', 'WDFC', 'ACN', 'KMX', 'CMG', 'CVS', 'DG', 'ENVA',
'HD', 'GWW', 'DIS', 'WAB', 'AAP', 'ADS', 'MO', 'AMZN', 'AAL', 'AMAT', 'T', 'BBY', 'BA', 'CBS', 'CTL', 'CVX', 'CSCO', 'GLW', 'EMN', 
'XOM', 'FL', 'F', 'GE', 'GM', 'INTC', 'IBM', 'SJM', 'JNJ', 'M', 'MAR', 'MCD', 'MU', 'JWN', 'NVDA', 'SHW', 'SBUX', 'TGT', 'TSN', 'VZ',
'WMT', 'YUM', 'AMD', 'FIVE', 'FIZZ', 'PZZA']

Approximate intrinsic value is calculated using DCF with a 10% discount rate for all stocks (can be varied) and varying growth rates. 

-----------------------------------------------------------------------------------"""   
list = IndexData.getList()
badlist = []
screen = []

for i in list:
    try:
        Analyze.screen(i)
    except:
        print('error')
        badlist.append(i)




