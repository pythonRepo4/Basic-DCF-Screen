import Utility 
from HistoricalPricesData import Interface as priceInterface #@UnresolvedImport
from Analyze import GetData #@UnresolvedImport
from IndexData import Interface as IndexData 

from os import path
import sys
sys.path.insert(0, 'D:\\Eclipse Library\\SEC_Scrape')
sys.path.insert(0, 'D:\\Eclipse Library')
from SEC_Scrape.SQL.SQLMethods import getDebtData as opLease

class TickerFundamentals:
    tickerName = ''
    data = []
    variables = []
    price = []
    priceAvg = []
    ones = []
    
    """This initialization method will get data from getData once so sql is not continually queried"""
    def __init__(self, tickerName, getData = None):
        self.tickerName = tickerName
        if(getData == None):
            self.data, self.variables, self.price, self.priceAvg, self.ones = GetData.getData(tickerName)
        else:
            self.data, self.variables, self.price, self.priceAvg, self.ones = getData

    """Will return an array of variable (Revenues-T, EPS-T, etc) for all dates"""
    def getVariable(self, variable, variableOth = None):
        variableArray = []
        if(variableOth == None):
            variableOth = " 3333 333 "
        
        j = 0 
        """Go back 10 years or until j < len(data) """
        while(j < len(self.data) and j < 40):
            count = 0
            tempVar = ""
            for i in self.variables:
                if(i == variable or i == variableOth):
                    tempVar = self.data[j][count]
                count += 1
            
            variableArray.append(tempVar)
            j += 4
        
        return variableArray

    def numShares(self):
        return self.getVariable("Weighted Average Shares-Q")
    
    def getEquity(self):
        return self.getVariable("Shareholders Equity-QB")
    
    def getDebt(self):
        debt = self.getVariable("Total Debt-QB")
        assets = self.getVariable("Total Assets-QB")
        
        try:
            return Utility.myFloat(debt[0]) / Utility.myFloat(assets[0])
        except:
            return 0
        
    def getGoodwill(self):
        goodwill = self.getVariable("Goodwill and Intangible Assets-QB")
        assets = self.getVariable("Total Assets-QB")
        
        try:
            return Utility.myFloat(goodwill[0]) / Utility.myFloat(assets[0])
        except:
            return 0

    def getCashDebt(self):
        cash = self.getVariable("Cash and cash equivalents-QB", "Cash and Equivalents-QB")
        investments = self.getVariable("Investments-QB")
        debt = self.getVariable("Total Debt-QB")
        deposits = self.getVariable("Deposit Liabilities-QB")
        cashDebt = []

        for i in range(0, len(cash)):
            cashDebt.append(Utility.myFloat(cash[i]) + Utility.myFloat(investments[i]) - Utility.myFloat(debt[i]) - Utility.myFloat(deposits[i]))
        
        return cashDebt
    
    """Gets R&D + 10% of SGA which will later be capitalized """
    def getRD_SGA(self):
        rd = self.getVariable("Research and Development (R&D) Expenses-T")
        sga = self.getVariable("Selling, General and Administrative (SG&A) Expenses-T")
        rdaArray = []
        
        if(len(rd) < 1 or len(sga) < 1): 
            rd = self.getVariable("Research and Development Expense-T")
            sga = self.getVariable("Selling, General and Administrative Expense-T")
        
        for i in range(0, len(rd)):
            rdaArray.append(Utility.myFloat(rd[i]) + Utility.myFloat(sga[i]) * 0.10)

        return rdaArray

    """Returns capitalized RD & SGA with a 4 year amortization period. Will return an array with [RD & SGA Cap, Amorization]"""
    def getCapitalizedRDSGA(self):
        rdaArray = self.getRD_SGA()
        RDSGA = []
        
        """If data does not go far back enough, amortizationLength is = rdaArray length """
        amortizationLength = 4
        if(len(rdaArray) <= 4):
            for i in range(0, len(rdaArray)):
                RDSGA.append([0,0])
            return RDSGA
        
        i = 0 
        amortizationPercentage = 1 / amortizationLength
        while(i < len(rdaArray) - amortizationLength):
            RDA_SGA_Capitalization = 0
            amortization = 0
            
            """Capitalize previous RDA/SGA. Then find amortization back 4 years """
            for j in range(1, amortizationLength + 1):
                RDA_SGA_Capitalization += Utility.myFloat(rdaArray[i + j]) * (1 - amortizationPercentage * j)
                amortization += Utility.myFloat(rdaArray[i + j]) * (amortizationPercentage)
                
            RDSGA.append([RDA_SGA_Capitalization, amortization])
            i += 1
            
        """Now approximate both RDA_SGA_Cap and amortization back so that it is same length as rdaArray"""
        years = len(RDSGA) - 1 
        try:
            cagrCap = (RDSGA[0][0]/RDSGA[years][0])**(1/years)
            cagrAmor = (RDSGA[0][1]/RDSGA[years][1])**(1/years)
        except: 
            cagrCap = 1.02
            cagrAmor = 1.02
            
        i = len(RDSGA) - 1
        while(len(RDSGA) < len(rdaArray)):
            RDSGA.append([RDSGA[i][0] / cagrCap, RDSGA[i][1] / cagrAmor])
            i += 1
        
        return RDSGA
    
    def getOpLeases(self):
        """Add operating lease. Find approx cost of debt """
        interest = self.getVariable("Interest Expense-T")
        totalDebt = self.getVariable("Total Debt-QB")
        
        PVOpLease= []
        currentYear = []
        yearStart = 2017
        for i in range(0, len(interest)):
            try:
                costOfDebt = Utility.myFloat(interest[i]) / Utility.myFloat(totalDebt[i])
            except:
                costOfDebt = .025
            operatingLeases = opLease(self.tickerName, yearStart - i)

            tempPV = 0
            if(operatingLeases == None):
                PVOpLease.append(0)
                currentYear.append(0)
                continue
            
            for j in range(0, len(operatingLeases)):
                tempPV += (operatingLeases[j]) / (1 + costOfDebt) ** (j+1)
            
            PVOpLease.append(tempPV)
            currentYear.append(operatingLeases[0])
        
#         print(PVOpLease)
        """Approximate PVOpLease CAGR"""
        lastIndex = 0 
        while(PVOpLease[lastIndex] > 0):
            lastIndex += 1
            if(lastIndex == len(PVOpLease)):
                break
        lastIndex -= 1
        
        try:
            CAGR = (PVOpLease[0] / PVOpLease[lastIndex]) ** (1/lastIndex)
            if(CAGR > 1.15):
                CAGR = 1.1
            
            for i in range(lastIndex + 1, len(PVOpLease)):
                PVOpLease[i] = PVOpLease[i - 1] / CAGR
                currentYear[i] = currentYear[i - 1]/CAGR
        except:
            pass
        
        """Now calculate depreciation simply by dividing PVOpLease by 8 """
        depreciation = []
        for i in PVOpLease:
            depreciation.append(i/8)
        
#         print("PV Op Lease")
#         for i in PVOpLease:
#             print(i)
            
        return PVOpLease, currentYear, depreciation

    def getNOPLAT(self):
        NOPLATarray = []
        rdaArray = self.getRD_SGA()
        RDAmortization = self.getCapitalizedRDSGA()
        operatingLease, currentYear, leaseDepr = self.getOpLeases()
        
        EBIT = self.getVariable("Earnings before Tax-T")

        """NOPLAT is calculated as EBIT + current research + SG&A - RDSGA amortiziation 
        LESS adjusted taxes. (Effective Tax Rate not actual paid)  """
        for i in range(0, len(EBIT)):
            _ , RDamor = RDAmortization[i] 
            taxRate = .25
            NOPLAT = (Utility.myFloat(EBIT[i]) + Utility.myFloat(rdaArray[i]) - RDamor) * (1 - taxRate) + currentYear[i] - leaseDepr[i]
            NOPLATarray.append(NOPLAT)
#             print(str(EBIT[i]) + " : " + str(rdaArray[i]) + " : " + str(RDamor) + " : " + str(currentYear[i]) + " : " + str(leaseDepr[i]) )
#             print(NOPLAT)
#         print("NOPLAT")
#         for i in NOPLATarray:
#             print(i)
        return NOPLATarray
        
    def getInvestedCapital(self):  
        investedCapital = []
        RDAmortization = self.getCapitalizedRDSGA()
        cash = self.getVariable("Cash and Equivalents-QB")
        currentAssets = self.getVariable("Current Assets-QB")
        currentLiabilities = self.getVariable("Current Liabilities-QB")
        ppe = self.getVariable("Property, Plant & Equipment Net-QB")
        goodwill = self.getVariable("Goodwill and Intangible Assets-QB")
        shareholdersEquity = self.getVariable("Shareholders Equity-QB")
        investments = self.getVariable("Investments-QB")
        totalDebt = self.getVariable("Total Debt-QB")
        nonCurrent = self.getVariable("Investments Non-Current-QB")
        totalAssets = self.getVariable("Total Assets-QB")
        totalLiabilities = self.getVariable("Total Liabilities-QB")
        operatingLease, _, leaseDepr = self.getOpLeases()
        
        """----------------------------------------------------------------
        Invested Capital is capital used to 
        There are two methods to calculate invested capital:
        
        1) Invested Capital w/ Goodwill = Current Assets - Current Liabilities - Excess Cash + Fixed Assets (PPE) + Goodwill + PV of Op Leases
                                        
                                        
        2) Invested Capital w/ Goodwill = Shareholders Equity + Total Debt - Cash * .95 + PV of Op Leases
        ----------------------------------------------------------------"""
        for i in range(0, len(cash)):
            researchCap, researchAmor = RDAmortization[i] 
            investedCapital1 = Utility.myFloat(currentAssets[i]) - Utility.myFloat(currentLiabilities[i]) - (0.80 * Utility.myFloat(cash[i])) + Utility.myFloat(ppe[i]) \
            + Utility.myFloat(goodwill[i]) + researchCap - researchAmor + operatingLease[i]
            
            investedCapital2 = Utility.myFloat(totalAssets[i]) - Utility.myFloat(totalLiabilities[i]) + Utility.myFloat(totalDebt[i]) + researchCap - researchAmor - \
            (.80 * Utility.myFloat(cash[i])) - Utility.myFloat(nonCurrent[i]) + operatingLease[i]
            if(investedCapital2 < 0): 
                investedCapital2 = Utility.myFloat(totalDebt[i]) + researchCap - researchAmor - (.80 * Utility.myFloat(cash[i])) - Utility.myFloat(nonCurrent[i]) + operatingLease[i]
                
#             """If investedCapital1 is much smaller than investedCapital2, investedCapital1 may not have Investments  """
#             if(investedCapital1 < investedCapital2 * 0.75):
#                 investedCapital1 = (0.9) * Utility.myFloat(cash[i]) + Utility.myFloat(investments[i])
    
            
            investedCapital.append([investedCapital1, investedCapital2])
        
#         print("invested cap")
#         for i in investedCapital:
#             print(i)
            
        return investedCapital
    
    def getFCF(self):
        FCF = []
        netIncome = self.getVariable("Net Income-T")
        capEX = self.getVariable("Capital Expenditure-TC")
        operatingCashFlow = self.getVariable("Operating Cash Flow-TC")
        stockBasedCompensation = self.getVariable("Share Based Compensation-TC")
        getFCF = self.getVariable("Free Cash Flow-TC")
        
        for i in range(0, len(netIncome)):
            FCFtemp = Utility.myFloat(operatingCashFlow[i]) + Utility.myFloat(capEX[i])- Utility.myFloat(stockBasedCompensation[i])
            FCFtemp = Utility.myFloat(getFCF[i]) - Utility.myFloat(stockBasedCompensation[i])
            FCF.append(FCFtemp)

        return FCF
        
    def getROIC(self):
        """ROIC is calculated as NOPLAT/Invested Capital"""
        NOPLAT = self.getNOPLAT()
        investedCapital = self.getInvestedCapital()
        dates = self.getVariable("dates")
        
#         for i in NOPLAT:
#             print(i)
#             
#         print(" ")
#         
#         for i in investedCapital:
#             print(i)

        returnROIC = []
        returnROICavg = []
        
        i = 0
        while(i + 1 < len(investedCapital)):
            try:
                ROIC1 = NOPLAT[i] / investedCapital[i + 1][0]
            except:
                ROIC1 = 0 
             
             
            try:
                ROIC2 = NOPLAT[i] / investedCapital[i + 1][1]
            except:
                ROIC2 = 0 
                 
            """Append date, ROIC1, ROIC2
            If NOPLAT is less than or equal to 0, return 0 for ROIC
            """
            if(NOPLAT[i] <= 0):
                returnROIC.append([0, 0])
                returnROICavg.append(0)
            else:
                returnROIC.append([ROIC1, ROIC2])
                returnROICavg.append((ROIC1+ROIC2)/2)
            
            dates.append(self.data[i][0])
            
            i += 1
            
    #     for i in returnROIC:
    #         print(i)
    #     
    #     for i in returnROICavg:
    #         print(i)
     
        return [returnROIC, returnROICavg]
    
    def reinvestment(self):
        reinvestment = []
        rd = self.getRD_SGA()
        rdCapitalization = self.getCapitalizedRDSGA()
        CAPEX = self.getVariable("Capital Expenditure-TC")
        deprAmortization = self.getVariable("Depreciation & Amortization-TC")
        currentAssets = self.getVariable("Current Assets-QB")
        currentLiabilities = self.getVariable("Current Liabilities-Q")
        cash = self.getVariable("Cash and Equivalents-QB")
        
        """Reinvestment of Capital is as follows: CAPEX - depreciation + RD - RDamor + change in working cap - change in excess cash"""
        for i in range(0, len(rd)- 1): 
            _, rdAmor = rdCapitalization[i]
            reinvestment.append(-1 * Utility.myFloat(CAPEX[i]) - Utility.myFloat(deprAmortization[i]) + Utility.myFloat(rd[i]) - Utility.myFloat(rdAmor)
                     + Utility.myFloat(currentAssets[i]) - Utility.myFloat(currentLiabilities[i]) 
                     - (Utility.myFloat(currentAssets[i+1]) - Utility.myFloat(currentLiabilities[i+1])) - ((.8) * Utility.myFloat(cash[i]) - (.8) * Utility.myFloat(cash[i+1])))

        reinvestment.append(reinvestment[-1])
        return reinvestment
    
    def getROE(self):
        Tequity = self.getVariable("Shareholders Equity-QB")
        Tdividends = self.getVariable("Payment of Dividends & Other Cash Distributions-TC")
        Trepurchases = self.getVariable("Issuance (Purchase) of Equity Shares-TC")
        weightAverageShares = self.getVariable("Weighted Average Shares Diluted-T", "Weighted Average Shares-T")
        
        equity = []
        dividends = []
        repurchases = []
        for i in range(0, len(Tequity)):
            equity.append(Utility.myFloat(Tequity[i]) / Utility.myFloat(weightAverageShares[i]))
            dividends.append(Utility.myFloat(Tdividends[i]) / Utility.myFloat(weightAverageShares[i]))
            repurchases.append(Utility.myFloat(Trepurchases[i]) / Utility.myFloat(weightAverageShares[i]))
        
        for i in equity:
            print(i)
            
        changeInEquity = []
        i = 1
        while(i < len(equity)):
            changeInEquity.append(equity[i-1]- equity[i])
            i += 1
        
        """Comprehensive income = Change in Equity + Dividends + Buybacks. 
        As of July 2018, I believe this approximates comprehensive income which is 
        net income + unrealized gains/losses + pension gains/losses + currency effects. 
        
        Comprehensive income is an idea of what a financial company firm can make including realized gains, 
        net income gained from fees, trading etc, and unrealized gains on the balance sheet. 
         """
        ROE = []
        i = 0
        while(i < len(changeInEquity)):
            ROE.append((changeInEquity[i] - dividends[i] - repurchases[i]) / equity[i+1])
            i += 1
        
        
        return ROE
            
        
    
    """-----------------------------------------------------------------------------
    Returns revenues, gross margin, operating margin, net income, 
    -----------------------------------------------------------------------------"""
    def spreadSheet(self):
        spreadSheet = []

        fcf = self.getFCF()
        NOPLAT = self.getNOPLAT()
        RD_SGA = self.getRD_SGA()
        _ ,roic = self.getROIC()
        numShares = self.numShares()
        reinvestment = self.reinvestment()
        cashDebt = self.getCashDebt()
        date = []
       
        i = len(roic)
        while(i < len(fcf)):
            roic.append(roic[-1])
            i += 1
        
        revenues = self.getVariable("Revenue-T", "Revenues-T")
        gross = self.getVariable("Gross Profit-T")
        operating = self.getVariable("Operating Income-T")
        netIncome = self.getVariable("Net Income-T")
        averagePrice = self.getVariable("Average Price")
    
        
        """Get first dates"""
        j = 0 
        while(j < len(self.data)):
            """Get date (first date)"""
            count = 0 
            for i in self.variables:
                if(i == 'dates'):
                    temp = self.data[j][count]
                    break
                count += 1
            date.append(temp)
            j += 4
        
        """ 
        0 - dates
        1 - revenues
        2 - gross margin
        3 - RD & SGA / Gross Margin 
        4 - op margin 
        5 - reinvestment rate
          - profit margin
        6 - net income per share
        7 - fcf per share
          - cash/debt
        8 - ROIC
          - AveragePrice
        """

        for i in range(0, len(revenues)):
            spreadSheet.append([date[i], Utility.myFloat(revenues[i]),
                                str(round(Utility.myFloat(gross[i])/Utility.myFloat(revenues[i]), 4)), 
                                str(round(Utility.myFloat(RD_SGA[i])/Utility.myFloat(gross[i]), 4)), 
                                str(round(Utility.myFloat(operating[i])/Utility.myFloat(revenues[i]), 4)), 
                                str(round(Utility.myFloat(reinvestment[i])/Utility.myFloat(NOPLAT[i]) , 4)),
                                str(round(Utility.myFloat(netIncome[i])/Utility.myFloat(revenues[i]), 4)),
                                str(round(Utility.myFloat(netIncome[i])/Utility.myFloat(numShares[i]), 4)),
                                str(round(Utility.myFloat(fcf[i])/Utility.myFloat(numShares[i]), 4)),
                                str(round(Utility.myFloat(fcf[i])/Utility.myFloat(revenues[i]), 4)), 
                                str(round(Utility.myFloat(cashDebt[i])/Utility.myFloat(numShares[i]), 4)), 
                                str(round(roic[i], 4)),
                                str(round(Utility.myFloat(averagePrice[i]),2)) ])
         
        return spreadSheet
    


             
 
# t = TickerFundamentals("MKL")
# value = t.getROE()
# for i in value:
#     print(i)
       
     
    