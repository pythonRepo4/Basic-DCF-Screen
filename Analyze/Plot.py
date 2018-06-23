import Utility
import matplotlib.pyplot as plt
import datetime
import numpy as np
from Analyze import Ratios as Ratios #@UnresolvedImport

"""-----------------------------------------------------------------------------------
Matplotlib requires dates to be in format YYYY-MM-DD. Dates usually come in format
YYYY/MM/DD
-----------------------------------------------------------------------------------"""   
def convertDates(dates):
    returnDates = []
    for i in dates:
        returnDates.append(datetime.datetime.strptime(i, "%Y/%m/%d"))
    return returnDates

"""-----------------------------------------------------------------------------------
Simple plot function 
-----------------------------------------------------------------------------------"""   
def plot(tickerName, x, y, x_axis , y_axis):
    plt.title(tickerName)
    plt.plot(x, y)
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    plt.show()
    
"""-----------------------------------------------------------------------------------
Plotting my P/B calculation
-----------------------------------------------------------------------------------""" 
def plotBook(tickerName):
#     book, dates = Ratios.getBookArray(tickerName) 
    book, dates = Ratios.getTangibleBookArray(tickerName) 
    plot(tickerName, convertDates(dates), book, 'Dates', 'Book')

def plotROIC(tickerName):
    _, roic, dates = Ratios.getROIC(tickerName)
    plot(tickerName, convertDates(dates), roic, 'Dates', 'ROIC')
    
def plotEBIT(tickerName):
    EBIT, dates = Ratios.getEBIT(tickerName)
    plot(tickerName, convertDates(dates), EBIT, 'Dates', 'EBIT')
    

# list = ['BLMT', 'SFBC', 'SFST', 'WBKC', 'C', 'JPM', 'PNC', 'STI', 'WFC', 'HOMB', 'BAC', 'GWB', 'STL']
# list = ['MU']
# for i in list:
#     plotBook(i)
#     plotROIC(i)
#     plotEBIT(i)

