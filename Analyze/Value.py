from Analyze import Ratios #@UnresolvedImport
from Analyze import GetData #@UnresolvedImport
import Utility

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
#  
#     print("FCF Now : " + "{:,}".format(fcf[0]))
#     print("FCF 3yr Avg : " + "{:,}".format(fcf_3yrAverage))
#     print("High Growth : " +  str(highGrowth))
#     print(value)
#     print(valueAvg)
#     
    return fcf[0], fcf_3yrAverage, value, valueAvg


# list = ["AAL", "AAP", "AAPL", "AMAT", "AMD", "AMZN", "BA", "BBY", "CACC", "CMCSA", "CMG", "CTL", "DG", "DIS", "ENVA", "CVS", "FAST", "F", "FB", "FIVE", 
#         "GE", "GM", "GOOGL", "GWW", "IBM", "INTC", "IPGP", "JNJ", "JWN", "M", "MCD", "MO", "MU", "NVDA", "PZZA", "QCOM", "SBUX", "SWKS", "TGT", "WMT", "XOM", 
#         "WAB", "WDFC", "FIZZ", "YUM", "TSN", "THRM", "KMX", "T", "SJM", "MAR", "ACN", "ADS", "CBS", "CSCO", "CVX", "GLW", "EMN", "FL", "HD", "SHW", "VZ", "DIS"]
# for i in list:
#     print(i)
#     print(getValue(i))
#     print("")


# def getEquityValue(tickerName, getData = None):
#     f = Ratios.TickerFundamentals(tickerName, getData)
#     ROE, CAGR = f.getROE()
#     equity = f.getEquity() * .85
#     numShares = f.numShares() 
#     
# #     print("{:,}".format(equity))
# #     print("{:,}".format(numShares))
#     
#     ROEtotal = sum(ROE)/len(ROE)
#     ROErecent = sum(ROE[0:4])/len(ROE[0:4])
#     
#     ROEpossible = sorted([CAGR, ROEtotal, ROErecent])
#     
#     if(ROEpossible[1] < 0): 
#         print('Possible negative value')
#         print(ROEpossible)
#     
#     WACC = .09
#     g = .025
#     
#     multiplier = ROEpossible[1] / (WACC-g)
#     
#     value = [["ROE = " + "{0:.4f}".format(ROEpossible[0]) , equity * (ROEpossible[0] / (WACC - (g - 0.005))) / numShares],
#              ["ROE = " + "{0:.4f}".format(ROEpossible[1]) , equity * (ROEpossible[1] / (WACC - g)) / numShares],
#              ["ROE = " + "{0:.4f}".format(ROEpossible[2]) , equity * (ROEpossible[2] / (WACC - (g + 0.005))) / numShares]
#         ]
#     
# #     for i in value:
# #         print(i)
#     return value





