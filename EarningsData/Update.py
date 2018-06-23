from EarningsData import Download #@UnresolvedImport
from EarningsData import ReadExcel #@UnresolvedImport
from EarningsData import SqliteMethods #@UnresolvedImport
from IndexData import Interface as IndexData #@UnresolvedImport
import Utility

"""-----------------------------------------------------

While performing update, sometimes the variable name from 
stockrow.com changes. For example, "Earnings per Basic Share-Q" was
changed to "EPS-Q". This method will return these possible changes. 

-------------------------------------------------------"""  
def compare(variable):
    list = [
[ 'dates'  ,'dates'],
[ 'Revenues-Q'  ,'Revenues-Q'],
[ 'Revenue Growth-Q'  ,'Revenue Growth-Q'],
[ 'Cost of Revenue-Q'  ,'Cost of Revenue-Q'],
[ 'Gross Profit-Q'  ,'Gross Profit-Q'],
[ 'Research and Development Expense-Q'  ,'Research and Development Expense-Q'],
[ 'Selling, General and Administrative Expense-Q'  ,'Selling, General and Administrative Expense-Q'],
[ 'Operating Expenses-Q'  ,'Operating Expenses-Q'],
[ 'Operating Income-Q'  ,'Operating Income-Q'],
[ 'Interest Expense-Q'  ,'Interest Expense-Q'],
[ 'Earnings before Tax-Q'  ,'Earnings before Tax-Q'],
[ 'Income Tax Expense-Q'  ,'Income Tax Expense-Q'],
[ 'Net Income to Non-Controlling Interests-Q'  ,'Net Income to Non-Controlling Interests-Q'],
[ 'Net Income from Discontinued Operations-Q'  ,'Net Income from Discontinued Operations-Q'],
[ 'Net Income-Q'  ,'Net Income-Q'],
[ 'Preferred Dividends Income Statement Impact-Q'  ,'Preferred Dividends Income Statement Impact-Q'],
[ 'Net Income Common Stock-Q'  ,'Net Income Common Stock-Q'],
[ 'EPS-Q'  ,'Earnings per Basic Share-Q'],
[ 'EPS Diluted-Q'  ,'Earnings per Diluted Share-Q'],
[ 'Weighted Average Shares-Q'  ,'Weighted Average Shares-Q'],
[ 'Dividends per Basic Common Share-Q'  ,'Dividends per Basic Common Share-Q'],
[ 'Gross Margin-Q'  ,'Gross Margin-Q'],
[ 'EBITDA Margin-Q'  ,'EBITDA Margin-Q'],
[ 'EBIT Margin-Q'  ,'EBIT Margin-Q'],
[ 'Profit Margin-Q'  ,'Profit Margin-Q'],
[ 'Free Cash Flow Margin-Q'  ,'Free Cash Flow Margin-Q'],
[ 'EBITDA-Q'  ,'Earnings Before Interest, Taxes & Depreciation Amortization (EBITDA)-Q'],
[ 'EBIT-Q'  ,'Earning Before Interest & Taxes (EBIT)-Q'],
[ 'Consolidated Income-Q'  ,' '],
[ 'Revenues-T'  ,'Revenues-T'],
[ 'Revenue Growth-T'  ,'Revenues-T'],
[ 'Cost of Revenue-T'  ,'Cost of Revenue-T'],
[ 'Gross Profit-T'  ,'Gross Profit-T'],
[ 'Research and Development Expense-T'  ,'Research and Development Expense-T'],
[ 'Selling, General and Administrative Expense-T'  ,'Selling, General and Administrative Expense-T'],
[ 'Operating Expenses-T'  ,'Operating Expenses-T'],
[ 'Operating Income-T'  ,'Operating Income-T'],
[ 'Interest Expense-T'  ,'Interest Expense-T'],
[ 'Earnings before Tax-T'  ,'Earnings before Tax-T'],
[ 'Income Tax Expense-T'  ,'Income Tax Expense-T'],
[ 'Net Income to Non-Controlling Interests-T'  ,'Net Income to Non-Controlling Interests-T'],
[ 'Net Income from Discontinued Operations-T'  ,'Net Income from Discontinued Operations-T'],
[ 'Net Income-T'  ,'Net Income-T'],
[ 'Preferred Dividends Income Statement Impact-T'  ,'Preferred Dividends Income Statement Impact-T'],
[ 'Net Income Common Stock-T'  ,'Net Income Common Stock-T'],
[ 'EPS-T'  ,'Earnings per Basic Share-T'],
[ 'EPS Diluted-T'  ,'Earnings per Diluted Share-T'],
[ 'Weighted Average Shares-T'  ,'Weighted Average Shares-T'],
[ 'Dividends per Basic Common Share-T'  ,'Dividends per Basic Common Share-T'],
[ 'Gross Margin-T'  ,'Gross Margin-T'],
[ 'EBITDA Margin-T'  ,'EBITDA Margin-T'],
[ 'EBIT Margin-T'  ,'EBIT Margin-T'],
[ 'Profit Margin-T'  ,'Profit Margin-T'],
[ 'Free Cash Flow Margin-T'  ,'Free Cash Flow Margin-T'],
[ 'EBITDA-T'  ,'Earnings Before Interest, Taxes & Depreciation Amortization (EBITDA)-T'],
[ 'EBIT-T'  ,'Earning Before Interest & Taxes (EBIT)-T'],
[ 'Consolidated Income-T'  ,' '],
[ 'Cash and Equivalents-QB'  ,'Cash and Equivalents-QB'],
[ 'Trade and Non-Trade Receivables-QB'  ,'Trade and Non-Trade Receivables-QB'],
[ 'Inventory-QB'  ,'Inventory-QB'],
[ 'Property, Plant & Equipment Net-QB'  ,'Property, Plant & Equipment Net-QB'],
[ 'Goodwill and Intangible Assets-QB'  ,'Goodwill and Intangible Assets-QB'],
[ 'Tax Assets-QB'  ,'Tax Assets-QB'],
[ 'Total Assets-QB'  ,'Total Assets-QB'],
[ 'Trade and Non-Trade Payables-QB'  ,'Trade and Non-Trade Payables-QB'],
[ 'Deferred Revenue-QB'  ,'Deferred Revenue-QB'],
[ 'Tax Liabilities-QB'  ,'Tax Liabilities-QB'],
[ 'Deposit Liabilities-QB'  ,'Deposit Liabilities-QB'],
[ 'Total Liabilities-QB'  ,'Total Liabilities-QB'],
[ 'Accumulated Other Comprehensive Income-QB'  ,'Accumulated Other Comprehensive Income-QB'],
[ 'Accumulated Retained Earnings (Deficit)-QB'  ,'Accumulated Retained Earnings (Deficit)-QB'],
[ 'Shareholders Equity-QB'  ,'Shareholders Equity-QB'],
[ 'Investments-QB'  ,'Shareholders Equity (USD)-QB'],
[ 'Total Debt-QB'  ,'Total Debt (USD)-QB'],
[ 'Depreciation & Amortization-QC'  ,'Depreciation, Amortization & Accretion-QC'],
[ 'Share Based Compensation-QC'  ,'Share Based Compensation-QC'],
[ 'Operating Cash Flow-QC'  ,'Net Cash Flow from Operations-QC'],
[ 'Capital Expenditure-QC'  ,'Capital Expenditure-QC'],
[ 'Net Cash Flow - Business Acquisitions and Disposals-QC'  ,'Net Cash Flow - Business Acquisitions and Disposals-QC'],
[ 'Net Cash Flow - Investment Acquisitions and Disposals-QC'  ,'Net Cash Flow - Investment Acquisitions and Disposals-QC'],
[ 'Investing Cash Flow-QC'  ,'Net Cash Flow from Investing-QC'],
[ 'Issuance (Repayment) of Debt Securities-QC'  ,'Issuance (Repayment) of Debt Securities-QC'],
[ 'Issuance (Purchase) of Equity Shares-QC'  ,'Issuance (Purchase) of Equity Shares-QC'],
[ 'Payment of Dividends & Other Cash Distributions-QC'  ,'Payment of Dividends & Other Cash Distributions-QC'],
[ 'Financing Cash Flow-QC'  ,'Net Cash Flow from Financing-QC'],
[ 'Effect of Exchange Rate Changes on Cash-QC'  ,'Effect of Exchange Rate Changes on Cash-QC'],
[ 'Net Cash Flow / Change in Cash & Cash Equivalents-QC'  ,'Net Cash Flow / Change in Cash & Cash Equivalents-QC'],
[ 'Free Cash Flow-QC'  ,'Free Cash Flow-QC'],
[ 'Depreciation & Amortization-TC'  ,'Depreciation, Amortization & Accretion-TC'],
[ 'Share Based Compensation-TC'  ,'Share Based Compensation-TC'],
[ 'Operating Cash Flow-TC'  ,'Net Cash Flow from Operations-TC'],
[ 'Capital Expenditure-TC'  ,'Capital Expenditure-TC'],
[ 'Net Cash Flow - Business Acquisitions and Disposals-TC'  ,'Net Cash Flow - Business Acquisitions and Disposals-TC'],
[ 'Net Cash Flow - Investment Acquisitions and Disposals-TC'  ,'Net Cash Flow - Investment Acquisitions and Disposals-TC'],
[ 'Investing Cash Flow-TC'  ,'Net Cash Flow from Investing-TC'],
[ 'Issuance (Repayment) of Debt Securities-TC'  ,'Issuance (Repayment) of Debt Securities-TC'],
[ 'Issuance (Purchase) of Equity Shares-TC'  ,'Issuance (Purchase) of Equity Shares-TC'],
[ 'Payment of Dividends & Other Cash Distributions-TC'  ,'Payment of Dividends & Other Cash Distributions-TC'],
[ 'Financing Cash Flow-TC'  ,'Net Cash Flow from Financing-TC'],
[ 'Effect of Exchange Rate Changes on Cash-TC'  ,'Effect of Exchange Rate Changes on Cash-TC'],
[ 'Net Cash Flow / Change in Cash & Cash Equivalents-TC'  ,'Net Cash Flow / Change in Cash & Cash Equivalents-TC'],
[ 'Free Cash Flow-TC'  ,'Free Cash Flow-TC'],
[ 'Book Value per Share-QM'  ,'Book Value per Share-QM'],
[ 'Tangible Book Value per Share-QM'  ,'Tangible Assets Book Value per Share-QM'],
[ 'FCF per Share-QM'  ,'Free Cash Flow per Share-QM'],
[ 'Interest Debt per Share-QM'  ,'Interest Debt per Share-QM'],
[ 'Cash per Share-QM'  ,'Cash per Share-QM'],
[ 'Debt to Equity Ratio-QM'  ,'Debt to Equity Ratio-QM'],
[ 'Total Debt To Total Assets-QM'  ,'Total Debt To Total Assets-QM'],
[ 'Interest Coverage-QM'  ,'Interest Coverage-QM'],
[ 'Income Quality-QM'  ,'Income Quality-QM'],
[ 'Payout Ratio-QM'  ,'Payout Ratio-QM'],
[ 'Intangible Assets out of Total Assets-QM'  ,'Intangible Assets out of Total Assets-QM'],
[ 'Selling, General and Administrative Expense of Revenue-QM'  ,'Selling, General and Administrative Expense of Revenue-QM'],
[ 'Research and Development Expense of Revenue-QM'  ,'Research and Development Expense of Revenue-QM'],
[ 'Tangible Asset Value-QM'  ,'Tangible Asset Value-QM'],
[ 'Invested Capital-QM'  ,'Invested Capital-QM'],
[ 'ROE-TM'  , 'Return on Average Equity-TM'],
[ 'ROA-TM'  ,'Return on Average Assets-TM' ],
[ 'Return on Sales-TM' , 'Return on Sales-TM'],
[ 'FCF per Share-TM'  ,'Free Cash Flow per Share-TM'],
[ 'Sales per Share-TM'  ,'Sales per Share-TM'],
[ 'EBIT Growth-QG'  ,'EBIT Growth-QG'],
[ 'EPS Growth-QG'  ,'Earnings per Basic Share Growth-QG'],
[ 'EPS Diluted Growth-QG'  ,'Earnings per Diluted Share Growth-QG'],
[ 'EV/EBIT-TM', 'Enterprise Value over EBIT-TM']

            ]
    
    new = []
    old = []
    
    for i in list:
        new.append(i[0])
        old.append(i[1])
        
    try:
        index = new.index(variable)
    except:
        return '-111111'
    
    return old[index]
    
    
"""-----------------------------------------------------

update function will do following:
- Delete Excel files associated with tickerName from stockrow.com and yahoo finance.
- Download new Excel files
- Retrieve current data in sql and extract data from new Excel files. 
- Take new data extracted from Excel files and then add older data not in new data

-------------------------------------------------------"""  
def update(tickerName):
#     Download.deleteAll(tickerName)
#     Download.downloadAll(tickerName)
     
    """Get data from excel files that were downloaded above """
    newData = ReadExcel.readExcel(tickerName)
    """Get current earnings data"""
    tempSQLData = SqliteMethods.getData(tickerName)
      
#     for i in newData:
#         print(i)
#         
#     for i in tempSQLData:
#         print(i)
#     print(len(tempSQLData))
     
    sqlData = []
    """Flip data from tempSQLData diagonally across matrix """
    for i in range(0,len(tempSQLData[0])):
        temp = []
        for j in range(0,len(tempSQLData)):
            temp.append(tempSQLData[j][i])
        sqlData.append(temp)
         
    """ 
    At this point, newData and sqlData is in the form:
    date    9/5/2017, 5/5/2017,.....
    revenue 500, 400,.... 
    """
         
    """Find which sqlData is not in newData. """
    newDates = newData[0][1:]
    oldDates = sqlData[0][1:]
    addDates = []
 
    for i in oldDates:
        if(i not in newDates):
            addDates.append(i)
             
    """Take data not in newData and add it in 
    First find what the variables are in newData. Then, try to find that
    variable with the corresponding add date and add it in. If the variable is not found,
    simply add ' ' 
     
    Try to find the row/
    """
     
    oldVariables = tempSQLData[0]
         
    for i in addDates:
        """Find index of addDate in sqlData """
        column = sqlData[0].index(i)
         
        for j in newData:
            currentVariable = j[0] 
            try:
                row = oldVariables.index(currentVariable)
            except:
                try:
                    row = oldVariables.index(compare(currentVariable))
                except:
                    row = -1
             
            if(row < 0):
                j.append(' ')
            else:
                j.append(sqlData[row][column])
     
    temp = newData
    newData = []            
    for i in range(0, len(temp[0])):
        tempLine = []
        for j in range(0,len(temp)):
            tempLine.append(temp[j][i])
        newData.append(tempLine)
         
#     for i in newData:
#         print(i)
#         print(len(i))
#     print(len(newData))
                 
    SqliteMethods.insertSQL(tickerName, newData)
    return newData


"""-----------------------------------------------------

Will attempt an update if today's month is 4 months ahead of
last date on 

-------------------------------------------------------"""  
def updateByDate(tickerName):
    data = SqliteMethods.getData(tickerName)
    """Last earnings date of ticker """
    lastDate = data[1][0].split('/')
    print(lastDate)
    month = float(lastDate[1])
    year = float(lastDate[0])

    """Todays date. """
    today = Utility.getTodaysDate().split('/')
    currentMonth = float(today[0])
    currentYear = float(today[2])

    
    difference = 0 
    if(currentYear == year):
        difference = currentMonth - month
    elif((currentYear - 1) == year):
        difference = (12-month) + currentMonth
      
    """If current month and current year is more than 4 months away, try update """
    if(difference > 4):
        print('Attempting update......')
        update(tickerName)
        """Display date after update"""
        data = SqliteMethods.getData(tickerName)
        """Last earnings date of ticker """
        lastDate = data[1][0].split('/')
        print("Date After update :", end = '') 
        print(lastDate)
    else:
        print('No Update')
        

def updateAll():
    list = IndexData.getList()
#     list = ['BRKB', 'MKL', 'UVE', 'AIG', 'CB', 'CINF', 'HIG', 'L', 'PGR', 'TRV', 'XL', 'ANAT', 'AFSI', 'ACGL', 'ESGR', 'NGHC', 'SIGI', 'Y', 'AFG', 'AHL', 'AXS', 'CNA', 'RE', 'FAF', 'KMPR', 'MKL', 'MCY', 'MTG', 'ORI', 'RDN', 'RNR', 'RLI', 'THG', 'VR', 'WRB', 'WTM', 'BLMT', 'SFBC', 'SFST', 'WBKC', 'C', 'JPM', 'PNC', 'STI', 'WFC', 'HOMB', 'BAC', 'GWB', 'STL']
    badlist = []
    
    for i in list:
        try:
            print(i)
            updateByDate(i)
        except:
            badlist.append(i)
    
    print(badlist)