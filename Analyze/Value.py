from Analyze import Ratios #@UnresolvedImport
from Analyze import GetData #@UnresolvedImport
import Utility

def getPerShareValue(tickerName, getData = None):
    f = Ratios.TickerFundamentals(tickerName, getData)
    fcf = f.getFCF()
    ROIC = f.getROIC()[1]
    IR = f.reinvestment()
    NOPLAT = f.getNOPLAT()
    numShares = f.numShares()
    cashDebt = f.getCashDebt()
    
    fcfPerShare = []
    for i in range(0, len(fcf)):
        fcfPerShare.append(Utility.myFloat(fcf[i]) / Utility.myFloat(numShares[i]))
        
    cashDebtShare = []
    for i in range(0, len(cashDebt)):
        cashDebtShare.append(Utility.myFloat(cashDebt[i]) / Utility.myFloat(numShares[i]))
        
    cashDebt = cashDebtShare[0]
    fcfNow = fcfPerShare[0]
    try:
        fcf_3yr = (fcfPerShare[0] + fcfPerShare[1] + fcfPerShare[2]) / 3
    except:
        fcf_3yr = (fcfPerShare[0] + fcfPerShare[1]) / 2
        
    return fcfNow, fcf_3yr, cashDebt


def getValue(tickerName, getData = None):   
    f = Ratios.TickerFundamentals(tickerName, getData)
    fcf = f.getFCF()
    ROIC = f.getROIC()[1]
    IR = f.reinvestment()
    NOPLAT = f.getNOPLAT()
    numShares = Utility.myFloat(f.numShares()[0])
    cashDebt = Utility.myFloat(f.getCashDebt()[0])
    
    """Possible growth values """
    g = []
    for i in range(0, len(ROIC)):
        g.append(ROIC[i] * (IR[i]/NOPLAT[i]))
    g = sum(g[0:3]) / 3

    """FCF 3 & 5 YR CAGR """
    try:
        fcf_3yr = (abs(fcf[0]) / abs(fcf[3])) ** (1/3) - 1
        fcf_5yr = (abs(fcf[0]) / abs(fcf[5])) ** (1/5) -1
        fcf_3yrAverage = sum(fcf[0:3]) / 3
    except:
        fcf_3yr = g
        fcf_5yr = g
        fcf_3yrAverage = fcf[0]

    """Value: No Growth, Low Growth, Approximate Growth """
    discountRate = .1
    lowGrowth = 0.025
    """
    No Growth,
    Low Growth, 
    High Growth + Terminal Value
    """
    """Estimate High Growth"""
    highGrowth = (g + fcf_3yr + fcf_5yr) / 3
    if(highGrowth < 0):
        highGrowth = .04
    if(highGrowth > .40):
        highGrowth = .35
        
    highGrowthMultiplier = 0 
    for i in range(0, 6):
        highGrowthMultiplier += (1 + highGrowth) ** (i) / (1 + discountRate) ** (i+1)
    highGrowthMultiplier += (1 + lowGrowth) * (1 + highGrowth) ** 5 / (discountRate - lowGrowth) / (1+discountRate) ** 5
    
    value = [(fcf[0] / discountRate / numShares) + (cashDebt / numShares),              
             (fcf[0] / (discountRate - lowGrowth) / numShares) + (cashDebt / numShares),
             highGrowthMultiplier * fcf[0] / numShares + (cashDebt/numShares)
             ]
    
    valueAvg = [(fcf_3yrAverage / discountRate / numShares) + (cashDebt / numShares),              
                (fcf_3yrAverage / (discountRate - lowGrowth) / numShares) + (cashDebt / numShares), 
                highGrowthMultiplier * fcf_3yrAverage / numShares + (cashDebt/numShares)
                ]
  
#     print("FCF Now : " + "{:,}".format(fcf[0]))
#     print("FCF 3yr Avg : " + "{:,}".format(fcf_3yrAverage))
#     print("High Growth : " +  str(highGrowth))
#     print(value)
#     print(valueAvg)
     
    return fcf[0], fcf_3yrAverage, value, valueAvg


# list = ['AMWD', 'BIIB', 'EXPO', 'FB', 'FAST', 'IPGP', 'LNTH', 'ORLY', 'ROST', 'SWKS', 'ULTA', 'AZO', 'FDS', 'GPS', 'HD', 'OOMA', 'PSTG', 'RHT', 'ROL', 'TSE', 'UNH', 'AMZN', 'AMAT', 'BBY', 'HRB', 'CHRW', 'CELG', 'CNC', 'CI', 'CLX', 'CL', 'EW', 'EA', 'GRMN', 'HAS', 'HUM', 'KLAC', 'LB', 'LRCX', 'LYB', 'MAS', 'MCD', 'MTD', 'MU', 'MSFT', 'MNST', 'MSI', 'NVDA', 'REGN', 'RHI', 'ROK', 'SHW', 'SPGI', 'TXN', 'HSY', 'UPS', 'VAR', 'INCY', 'MXIM', 'SIRI', 'ABMD', 'ALGN', 'AZPN', 'CDNS', 'CDK', 'CBPO', 'CRUS', 'CGNX', 'FIVE', 'LOPE', 'HA', 'HQY', 'LSTR', 'LOGI', 'LULU', 'LITE', 'MASI', 'MTCH', 'PZZA', 'PPC', 'SAFM', 'STMP', 'BIO', 'BURL', 'BWXT', 'CC', 'ENR', 'EPAM', 'GDDY', 'GGG', 'HLF', 'LPI', 'LEA', 'LII', 'LPX', 'RBA', 'RES', 'NOW', 'TNH', 'THO', 'TTC', 'VEEV', 'WBC', 'WSM', 'YELP', 'MIK', 'TREX', 'PZZA', 'ADP', 'PZZA', 'ADP', 'DENN', 'IRBT', 'KBAL', 'MSBI', 'QLYS', 'RUTH', 'PRSC', 'UCTT', 'WING']
# 
# for i in list:
#     print(i)
#     getValue(i)
#     print("")

# getValue("SBUX")





