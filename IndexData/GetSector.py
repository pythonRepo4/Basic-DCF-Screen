from urllib import request
from bs4 import BeautifulSoup
import Utility


"""-----------------------------------------------------------------------

Will get the Sector / Industry of the stock from Yahoo Finance. 

Ex. JCP is Services / Department Stores

------------------------------------------------------------------------"""
def getSector(tickerName):
    yahooSite = "https://finance.yahoo.com/quote/" + tickerName + "/profile?p=" + tickerName
         
    tempWebFile = request.urlopen(yahooSite).read()
    tempData = BeautifulSoup(tempWebFile, "lxml")
    html = tempData.prettify()
    
    lines = tempData.find_all('strong')
    try:
        sector = Utility.removeTags(str(lines[0]))
        industry = Utility.removeTags(str(lines[1]))
    except:
        return ['', '']
    
    return [sector, industry]

def getBeta(tickerName):
    returnArray = []
    try:
        url2 = "http://finance.yahoo.com/quote/" + tickerName 
    
        tempWebFile = request.urlopen(url2).read()
        tempData = BeautifulSoup(tempWebFile,"lxml")
        html = tempData.prettify()  
        
        lines = tempData.find_all('span')
         
        payload = ''
        price = ''
        for i in range(0, len(lines)):
            tempLine = str(lines[i])
            marker = '>Beta'
#             print(tempLine)
            if marker not in tempLine:
                continue
            else:
                break  
    
        payload = str(lines[i+1])
        split = payload.split('>')
        for i in split:
            index1 = i.find('<')
             
            beta = -1
            try:
                beta = float(i[:index1])
                returnArray.append(beta)
            except:
                pass
        
        if(len(returnArray) == 0):
            returnArray.append(-111)
        
        for i in range(0, len(lines)):
            tempLine = str(lines[i])
            marker = '>Market Cap'
            if marker not in tempLine:
                continue
            else:
                break  
          
        payload = str(lines[i+1])
        split = payload.split('>')
        for i in split:
            index1 = i.find('<')
              
            marketCap = -1
            try:
                marketCap = i[:index1]
                BorM = marketCap[len(marketCap)-1]
                marketCap = float(marketCap[:len(marketCap)-1])
    
                if(marketCap > 0 and (BorM == 'B' or BorM == 'M')):
                    if(BorM == 'B'):
                        returnArray.append(float(marketCap) * 10**9)
                    elif(BorM == 'M'):
                        returnArray.append(float(marketCap) * 10**6)
                
            except:
                pass
#         
         
         
        return returnArray
    except: 
        return [-111,-1]
    
def getEPS(tickerName):
    try:
        url2 = "http://finance.yahoo.com/quote/" + tickerName 
        """If doesn't work, try Yahoo finance"""
    
        tempWebFile = request.urlopen(url2).read()
        tempData = BeautifulSoup(tempWebFile,"lxml")
        html = tempData.prettify()  
        
        lines = tempData.find_all('span')
         
        payload = ''
        price = ''
        for i in range(0, len(lines)):
            tempLine = str(lines[i])
            marker = '>EPS (TTM)'
            if marker not in tempLine:
                continue
            else:
                break  
        
        payload = str(lines[i+1])
        split = payload.split('>')
        for i in split:
            index1 = i.find('<')
            
            eps = -1
            try:
                eps = float(i[:index1])
                if(eps > 0):
                    return eps
            except:
                pass
        return -1 
    except: 
        return -1

#         price = price.replace(',','')
#                  
#                 try:
#                     todaysPrice = float(price)
#                     if(todaysPrice > 1 and todaysPrice * (0.5) <= historicalPrice and historicalPrice <= todaysPrice * (1.5)):
#                         return todaysPrice


