from Analyze import Ratios #@UnresolvedImport
from Analyze import GetData #@UnresolvedImport

"""-----------------------------------------------------------------------------------

Approximates reproduction value and EPV as calculated by Greenwald. 

-----------------------------------------------------------------------------------"""      
def reproductionEPV(tickerName, getData = None):
    if(getData == None):
        data, variables, price, priceAvg, ones = GetData.getData(tickerName)
    else:
        data, variables, price, priceAvg, ones = getData
    
    """Reproduction value will be calculated first.
    Here, reproduction value is very rudimentary. It is the capital required 
    to reproduce the business by looking at balance sheet. This is the formula:
    
    + 100% of Cash and Equivalents / Short Term Investments 
    + 90% of Inventory TTM
    + x2.5 of SG&A TTM
    + 110% of Trade and Non-Trade Receivables
    + 80% of PP&E
    + x2.5 of R&D TTM
    + 100 % Tax Assets discounted at 10%
    + 50% of Goodwill and Intangible Assets
    + 85% of Investments (similar to cash)
    
    *For financial/insurance firms. This is usually 0 for other companies
    
    
    - 100% of Current Liabilites 
      (Account/Trade Payables, Current Debt, Other liabilites all in one)
    - Tax Liabilities discounted at 10%
    - 100% of Debt non current. 

    
    """
    
    """All data is in 'data' array. data[0] is most recent earnings data. To
    find index of variable, variableIndex[] will be used which is on GetData.py 
    See below. """
    
#     for i in data:
#         print(i)
#     
    reproduction = 0
    try:
        reproduction += (1) * float(data[0][variables.index('Cash and Equivalents-QB')])
        reproduction += (1) * float(data[0][variables.index('Investments Current-QB')])
        reproduction += (0.80) * float(data[0][variables.index('Inventory-QB')])  
        reproduction += (2) * float(data[0][variables.index('Selling, General and Administrative (SG&A) Expenses-T')])  
        reproduction += (0.8) * float(data[0][variables.index('Property, Plant & Equipment Net-QB')])
        reproduction += (1.1) * float(data[0][variables.index('Trade and Non-Trade Receivables-QB')])  
        reproduction += (2.5) *  float(data[0][variables.index('Research and Development (R&D) Expenses-T')])   
        reproduction += float(data[0][variables.index('Tax Assets-QB')]) / 1.1    
        reproduction += (0.20) * float(data[0][variables.index('Goodwill and Intangible Assets-QB')])
        reproduction += (0.90) * float(data[0][variables.index('Investments Non-Current-QB')]) 
     
        reproduction -= (1) * float(data[0][variables.index('Current Liabilities-QB')])
        reproduction -= float(data[0][variables.index('Tax Liabilities-QB')]) / 1.1   
        reproduction -= (1) * float(data[0][variables.index('Debt Non-Current-QB')])

    except:
        try:
            reproduction += (1) * float(data[0][variables.index('Cash and Equivalents-QB')])
            reproduction += (0.80) * float(data[0][variables.index('Inventory-QB')])  
            reproduction += (2) * float(data[0][variables.index('Selling, General and Administrative Expense-T')])  
            reproduction += (0.8) * float(data[0][variables.index('Property, Plant & Equipment Net-QB')])
            reproduction += (1) * float(data[0][variables.index('Trade and Non-Trade Receivables-QB')])  
            reproduction += (2.5) *  float(data[0][variables.index('Research and Development Expense-T')])   
            reproduction += float(data[0][variables.index('Tax Assets-QB')]) / 1.1    
            reproduction += (0.50) * float(data[0][variables.index('Goodwill and Intangible Assets-QB')]) 
            reproduction += (1) * float(data[0][variables.index('Investments-QB')]) 
    #         print("{:,}".format(reproduction))
              
    #         reproduction -= float(data[0][variables.index('Trade and Non-Trade Payables-QB')]) / 1.1   
    #         reproduction -= float(data[0][variables.index('Tax Liabilities-QB')]) / 1.1   
    #         reproduction -= (1) * float(data[0][variables.index('Deposit Liabilities-QB')]) 
    #         reproduction -= (1) * float(data[0][variables.index('Total Debt-QB')]) 
            reproduction -= (1) * float(data[0][variables.index('Total Liabilities-QB')]) 
        except:
            reproduction += (1) * float(data[0][variables.index('Cash and Equivalents-QB')])
            reproduction += (0.80) * float(data[0][variables.index('Inventory-QB')])  
            reproduction += (2) * float(data[0][variables.index('Selling, General and Administrative (SG&A) Expenses-T')])  
            reproduction += (0.8) * float(data[0][variables.index('Property, Plant & Equipment Net-QB')])
            reproduction += (1.1) * float(data[0][variables.index('Trade and Non-Trade Receivables-QB')])  
            reproduction += (2.5) *  float(data[0][variables.index('Research and Development (R&D) Expenses-T')])   
            reproduction += float(data[0][variables.index('Tax Assets-QB')]) / 1.1    
            reproduction += (0.20) * float(data[0][variables.index('Goodwill and Intangible Assets-QB')])
            reproduction += (1) * float(data[0][variables.index('Investments-QB')]) 
         
            reproduction -= (1) * float(data[0][variables.index('Total Liabilities-QB')])


#         print("{:,}".format(reproduction))

#     print("{:,}".format(reproduction))
 
    """
    EPV Value will be calculated here by looking at income statments and 
    making proper adjustments. EPV value is the value that can be extracted
    from the business with no growth and still leave operations intact 
     
    Start with EBIT
    + 20% Depreciation, Amortization & Accretion
    + 25% R&D
    + 25% SG&A
     
    + 100% Growth Capex
    - 100% Capex
    - 100% Interest
     
    Then, apply 37.5 % flat tax rate. 
     
    """
    
    """Calculate growth CAPEX. Growth CAPEX is the CAPEX required to support
    revenue/sales growth. This is ADDED to EPV because it is money that is not needed for operations
    at 0 % growth. """ 
    growth = (float(data[0][variables.index('Revenues-T')]) - float(data[4][variables.index('Revenues-T')])) 
    revenueT = float(data[0][variables.index('Revenues-T')])
    taxRate = 0 
    
    """Get average PPE/Sales """
    i = 0
    tempRatio = [] 
    while(i < len(data)):
        try:
            tempRatio.append(float(data[i][variables.index('Property, Plant & Equipment Net-QB')]) / float(data[i][variables.index('Revenues-T')]))
        except:
            pass
        i += 4
        
    if(len(tempRatio) == 0):
        ratioPPEtoRevenue = 0 
    else:
        ratioPPEtoRevenue = sum(tempRatio) / len(tempRatio)
      
    growthCAPEX = 0 
    if(growth < 0):
        growthCAPEX = 0
    else:
        growthCAPEX = ratioPPEtoRevenue * growth
      
    """Get Average Ebit and multiple by current revenue-T """
    i = 0
    tempMargin = []
    while(i < len(data)/2):
#     while(i<4):
        try:
#             print(float(data[i][variables.index('EBIT Margin-T')]))
            tempMargin.append(float(data[i][variables.index('EBIT Margin-T')]))
        except:
            pass
        i += 4
    ebitMargin = sum(tempMargin)/len(tempMargin)
#     print(ebitMargin)
#     print(growthCAPEX)
      
    try:
        epv = (1.0) * revenueT * ebitMargin              
        epv += (0.25) * float(data[0][variables.index('Depreciation & Amortization-QC')])      
        epv += (0.25) * float(data[0][ variables.index('Selling, General and Administrative (SG&A) Expenses-T')]) 
        epv += (0.25) * float(data[0][variables.index('Research and Development (R&D) Expenses-T')])    
        epv += (1) * growthCAPEX             
        """NOTE: CAPEX is ADDED here because it is already negative"""              
        epv += (1) * float(data[0][variables.index('Capital Expenditure-TC')])        
        epv -= (1) * float(data[0][variables.index('Interest Expense-T')])    
    except:
        epv = (1.0) * revenueT * ebitMargin              
        epv += (0.25) * float(data[0][variables.index('Depreciation & Amortization-QC')])      
        epv += (0.25) * float(data[0][ variables.index('Selling, General and Administrative Expense-T')]) 
        epv += (0.25) * float(data[0][variables.index('Research and Development Expense-T')])    
        epv += (1) * growthCAPEX             
        """NOTE: CAPEX is ADDED here because it is already negative"""              
        epv += (1) * float(data[0][variables.index('Capital Expenditure-TC')])        
        epv -= (1) * float(data[0][variables.index('Interest Expense-T')])    
     
    """Get approximate tax rate"""
    try:
        taxRate = float(data[0][variables.index('Income Tax Expense-T')]) / float(data[0][variables.index('Earnings before Tax-T')]) 
    except:
        taxRate = .35
     
#     print(taxRate)
    epv = epv * (1 - taxRate)        
 
    f = Ratios.TickerFundamentals(tickerName)
    g = f.getGrowth()
    ROIC = f.getROIC()[1][0]
    WACC = f.getWACC()[0]
    numShares = f.numShares()    
    cashDebt = f.getCashDebt()
  
    if(g > 0.03):
        g = 0.03
        
    if(WACC < 0.08):
        WACC = 0.08
    
    if(g > (0.75 * WACC)):
        g = 0.75 * WACC
        
    if(ROIC <= 0):
        ROIC = 1
        g = 1
        
    if(g > ROIC):
        ROIC = 10000
         
    reproduction /= numShares
      
    returnEpv = [["{0:.4f}".format(WACC-.025) + " WACC", epv/(WACC-.025)],
                 ["{0:.4f}".format(WACC-.01) + " WACC", epv/(WACC-.01)],
                 ["{0:.4f}".format(WACC) + " WACC", epv/WACC], 
                 ["{0:.4f}".format(WACC+.01) + " WACC", epv/(WACC+.01)],
                 ["{0:.4f}".format(WACC+.025) + " WACC", epv/(WACC+.025)]]
     
    """Make adjustment to add cash and subtract long term debt from EPV too for a shareholders equity value. """
    for i in returnEpv:
        try:
            i[1] += (1) * float(data[0][variables.index('Cash and Equivalents-QB')])
            i[1] -= (1) * float(data[0][variables.index('Debt Non-Current-QB')])
        except:
            i[1] += (1) * float(data[0][variables.index('Cash and Equivalents-QB')])
            i[1] -= (1) * float(data[0][variables.index('Total Debt-QB')])
        i[1] /= numShares
     
    M = (1 - (g/ROIC)) / (1 - (g/WACC))
     
    marginOfSaftey = []
     
    for i in returnEpv:
        marginOfSaftey.append([i[0], i[1] * M])
     
#     print('Reproduction = ' + str(reproduction))
#     print('EPV')
#     for i in returnEpv:
#         print(i)
         
    return [reproduction, returnEpv, marginOfSaftey]
