from EarningsData import Interface as EarningsData #@UnresolvedImport
import Utility
'''-------------------------------------------------------

Gets data of ticker name. Returns data, variables, price, priceAvg, and ones arrays

---------------------------------------------------------'''    
def getData(tickerName):
#     print(tickerName)
    price, priceAvg = [], []
    ones = []
    
    ''' Data about stock ticker '''
    data = EarningsData.getData(tickerName)
    variables = data[0]
    data = data[1:]
#     data = Utility.invert(data)
     
#     for i in variables:
#         print(i)
#     print(variables)
#     for i in data:
#         print(i)
#     print(len(data))
     
    '''Extract price, priceAvg, and create ones array '''
    for i in range(0,len(data)):
        temp1 = data[i][len(data[0])-2]
        temp2 = data[i][len(data[0])-1]
        if(temp1 == ' ' or temp2 == ' ' or temp1 == '' or temp2 == ''):
            break
        price.append(float(temp1))
        priceAvg.append(float(temp2))
        ones.append(1)
    
    ''' ---------See if ML analysis works------'''
#     price, priceAvg = [], []
#     ones = []
# #     data = sql.executeReturn('SELECT * FROM TROW')
# #     variables = data[0]
# #     data = data[1:len(data)-3]
#     temp = sql.executeReturn('SELECT * FROM TROW')
#     for i in range(0,len(data)):
#         temp1 = data[i][len(temp[0])-2]
#         temp2 = data[i][len(temp[0])-1]
#         if(temp1 == ' ' or temp2 == ' '):
#             break
#         price.append(float(temp1))
#         priceAvg.append(float(temp2))
#         ones.append(1)

#     print([data, variables, price, priceAvg, ones])
    return [data, variables, price, priceAvg, ones]

getData('FB')