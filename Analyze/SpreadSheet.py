from Analyze import GetData
from Analyze import Ratios
import Utility

"""-----------------------------------------------------------------------------
Gets annual income information (end of FY TTM): Revenues, Gross Margin, RDA, SG&A,
EBIT (Op income), Net Income, CAPEX, approximate FCF.  
-----------------------------------------------------------------------------"""
def annualIncome(tickerName):
    ticker = Ratios.TickerFundamentals(tickerName)
    """ 
    0 - dates
    1 - revenues
    2 - gross margin
    3 - RD & SGA / Gross Margin 
    4 - op margin 
    5 - reinvestment rate
    6 - profit margin
    7 - net income per share
    8 - fcf per share
    9 - cash/debt
    10 - ROIC

    """
    temp = Utility.invert(ticker.spreadSheet())
    spreadSheet = []
    
    
    for i in temp:
        add = ""
        for j in i:
            add = str(j) + ":" + add
        spreadSheet.append(add)
    
    for i in spreadSheet:
        print(i)


# annualIncome("FB")
