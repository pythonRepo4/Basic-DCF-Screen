from HistoricalPricesData import Interface as historicalPrices #@UnresolvedImport
from urllib import request
from bs4 import BeautifulSoup
import Utility

"""-----------------------------------------------------------------------------------

Input is ticker symbol and array of dates which are earnings dates.
Earnings dates are sometimes not accurate and must be approximated by adding +1 to the month
This will return array with columns as follows:

Date, Price on Date, 3 Month Average Price between earnings
Historical Prices will come from sql table with tickerName + '_Historical' NOT excel.

-----------------------------------------------------------------------------------"""
def getHistoricalPrices(tickerName, dates):
    """If noAdjust is None, use adjustedDate to add 1 month to quarterly dates to estimate
    when financial data came out. Otherwise, dates is exact dates from Zacks"""
    eps_date = ""
    priceArray = []
    priceArray.append("Price")
    averageArray = []
    averageArray.append("Average Price")
    
    ''' Variables for Average'''
    averageDates = []
    averageSum = 0
    averageCount = 0
    returnArray = []    
    priceHistory = historicalPrices.getHistoricalSplit(tickerName)
    
#     for i in dates:
#         print(i)
#          
#     for i in priceHistory:
#         print(i)
    
    for i in dates:
        '''Skip if first element of array is not a date'''
        if(i == 'dates-adj' or i == 'dates' or i == 'date' or i == 'Exact Dates' or i == 'Exact Date'):
            continue
         
        eps_date = str(i).split("/")
        '''Finds correct price in Yahoo prices sheet''' 
        '''averageDates is index of where dates are found in Yahoo! csv file'''
        for j in range(0 , len(priceHistory)):
            sql_date = priceHistory[j][0].split("/")
            price = str(priceHistory[j][1])
              
            """0 - year, 1 - month, 2 - day"""
            """Could not find same exact date but went back """
            if(eps_date[0] == sql_date[0] and int(eps_date[1]) == int(sql_date[1]) and int(eps_date[2]) > int(sql_date[2])):
                priceArray.append(price) 
                averageDates.append(j)           
                break
            #"""Same Date"""i
            elif(eps_date[0] == sql_date[0] and int(eps_date[1]) == int(sql_date[1]) and int(eps_date[2]) == int(sql_date[2])):
                priceArray.append(price)
                averageDates.append(j)
                break
            #"""If month is 1 and rolls back to past year at 12 """
            elif((int(eps_date[0])-1) == (int(sql_date[0])) and int(eps_date[1]) == 1 and int(sql_date[1]) == 12):
                priceArray.append(price)
                averageDates.append(j)       
                break
              
            #"""Year is same, but month rolls back 1"""
            elif(eps_date[0] == sql_date[0] and int(eps_date[1]) > int(sql_date[1])):
                priceArray.append(price)
                averageDates.append(j)
                break
    
#     print(dates)
#     for i in priceHistory:
#         print(i)
#     print(priceArray)
#     print(averageDates)
     
    """This next section will find the average price over specified 3 months
    averageDates ex. ['2016-09-30', '2016-07-01', '2016-04-01', '2015-12-31'] 
    First Date will iterate for approximately 3 months"""
    averageCount = 0
    averageSum = 0
    for i in range(0,averageDates[0]):   
        try:
            price = float(str(priceHistory[i][1]))
            averageSum = averageSum + price
            averageCount += 1
        except:
            break
        
    averageArray.append(str(averageSum/averageCount))
     
#     for i in range(0,len(dates)):
#         print(dates[i] + " : " + str(averageDates[i]))
 
    '''Now find average of rest of the dates'''
    for i in range(1,len(averageDates)):
        averageSum = 0
        averageCount = 0
         
#         print(averageDates[i])
         
        """Range should be averageDate[i-1] + 1 and averageDates[i] + 1 because in loop above that
        appends averageDates, conditional statement happens and then simply appends. Does not iterate +1 """ 
        for j in range(averageDates[i-1]+1,averageDates[i]+1):
            try:
                price = float(str(priceHistory[j][1]))
            except:
                break
             
            averageSum = averageSum + price
            averageCount += 1
         
        averageArray.append(str(averageSum/averageCount))
 
    returnArray.append(dates)
    returnArray.append(priceArray)
    returnArray.append(averageArray)    
 
    return returnArray



# """-----------------------------------------------------
# 
# getPrices will first adjust quarterlyDates. QuarterlyDates is the end
# of the fiscal quarter, not when the earnings date came out. QuarterlyDates
# will be adjusted to match approximate date when earnings data came out
# and when market reacted to it. 
# 
# -------------------------------------------------------"""
# def getPrices(tickerName, quarterlyDates):
#     """Find next earnings date from nasdaq"""
#     nasdaqWebsite = "https://www.nasdaq.com/earnings/report/" + tickerName.lower()
#     tempWebFile = request.urlopen(nasdaqWebsite).read()
#     tempData = BeautifulSoup(tempWebFile, "lxml")
#     html = tempData.prettify()
#     
#     """Earnings dates are in a table. Use <tr> to try to find it"""
#     lines = tempData.find_all('table')
#     keyword = "<th>Date<br/>Reported</th>"
#     payload = ''
#     
#     for i in lines:
#         if(str(i).find(keyword) > 0):
#             payload = str(i)
#             break
#     
#     exactDate = ''
#     """Earnings dates in payload are in format MM/DD/YYYY. So, use split('/')
#     and first one that has array length of 3"""
#     for i in payload.splitlines():
#         tempLine = Utility.removeTags(i)
# #         print(tempLine)
#         if(tempLine == None):
#             continue
#         
#         if(len(tempLine.split('/')) == 3):
#             exactDate = tempLine
#             break
#         
#     """Switch to YYYY/MM/DD. If not found, make adjustment automatically 30 days"""
#     correspondingDate = ''
#     try:
#         tempArray = exactDate.split('/')
#         exactDate = tempArray[2] + "/" + tempArray[0] + "/" + tempArray[1]
#         """Now attempt to find adjustment. First see earnings date exactDate corresponds to by
#         finding which month is in a 2 month range."""
#         exactDateMonth = float(exactDate.split('/')[1])
#         for i in quarterlyDates:
#             if(i == 'dates' or i == 'Dates' or i == 'dates ' or i == 'Dates '):
#                 continue
#             
#             quarterlyDateMonth = float(i.split('/')[1])
#             
#             """See if a exactDate fits in a window between quarterlyDateMonth + 2 months"""
#             if(quarterlyDateMonth > exactDateMonth): 
#                 quarterlyDateMonth -= 12
#             
#     #         print(exactDateMonth - quarterlyDateMonth)
#             if((exactDateMonth - quarterlyDateMonth) <= 2 and (exactDateMonth - quarterlyDateMonth) >=0):
#                 correspondingDate = i 
#                 break
#     except:
#         pass
#         
#     
# 
# #     print(exactDate)
# #     print(correspondingDate)
#     
#     adjustment = 0 
#     monthDays = [31,28,31,30,31,30,31,31,30,31,30,31]   
#     """If no correspdoning date is found, estimate adjustment at 30 """
#     if(correspondingDate == ''):
#         adjustment = 30
#     else:
#         """With corresponding dates of exactDate and QuarterlyDateMonth, try to estimate adjustment by counting
#         difference between corrMonth and exactMonth, then adding days. And then subtracting (exactDay - corrDay)"""
#         exactMonth, exactDay = float(exactDate.split('/')[1]), float(exactDate.split('/')[2])
#         corrMonth, corrDay = float(correspondingDate.split('/')[1]), float(correspondingDate.split('/')[2])
#                 
#         for i in range(0,2):
#             if(corrMonth == exactMonth):
#                 break
#             adjustment += monthDays[int(corrMonth - 1)]
#             corrMonth += 1
#             if(corrMonth > 12):
#                 corrMonth -= 12
#         
#         adjustment += (exactDay - corrDay)
# 
# #     print(adjustment)
#     """Now adjust all dates by adding adjustment days to each date"""
#     count = 0
#     newDates = []
#     for i in quarterlyDates:
#         if(i == 'dates'):
#             continue
#         
#         eps_dateStr = str(i).split("/")
#         eps_dateInt = [int(eps_dateStr[0]), int(eps_dateStr[1]), int(eps_dateStr[2])]
#          
#         ''' Make eps_date go ahead 30 days '''
#         '''0 - Year, 1 - Month, 2 - Day'''
#         while(count < adjustment):
#             eps_dateInt[2] = eps_dateInt[2] + 1
#              
#             '''If day passes to next month, month will be updated '''
#             if(monthDays[eps_dateInt[1]-1] < eps_dateInt[2]):
#                 eps_dateInt[2] = 1
#                 if(eps_dateInt[1] == 12):
#                     eps_dateInt[1] = 1
#                     eps_dateInt[0] += 1
#                 else:
#                     eps_dateInt[1] += 1
#             count += 1
#         count  = 0 
#          
#         newDates.append(str(eps_dateInt[0]) + '/' + str(eps_dateInt[1]) + '/' +str(eps_dateInt[2]))
#     
#     newDates.insert(0, 'dates')
# #     print(newDates)
#     
#     return getHistoricalPrices(tickerName, newDates)

    
#      
# dates = ['dates', '2017/6/30', '2017/3/31', '2016/12/31', '2016/9/30', '2016/6/30', '2016/3/31', '2015/12/31', '2015/9/30', '2015/6/30', '2015/3/31', '2014/12/31', '2014/9/30', '2014/6/30', '2014/3/31', '2013/12/31', '2013/9/30', '2013/6/30', '2013/3/31', '2012/12/31', '2012/9/30', '2012/6/30', '2012/3/31', '2011/12/31', '2011/9/30', '2011/6/30', '2011/3/31', '2010/12/31', '2010/9/30', '2010/6/30', '2010/3/31', '2009/12/31', '2009/9/30', '2009/6/30', '2009/3/31', '2008/12/31', '2008/9/30', '2008/6/30', '2008/3/31', '2007/12/31', '2007/9/30']
# prices = getPrices('MKL', dates)
# for i in range(0, len(prices[0])):
#     print(prices[0][i] + " : " + prices[1][i] + " : " + prices[2][i])
