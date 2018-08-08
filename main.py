# from Analyze import Interface as Analyze #@UnresolvedImport
from Analyze import Interface as Analyze #@UnresolvedImport
from IndexData import Interface as IndexData #@UnresolvedImport
from RegressionData import Interface as RegressionData #@UnresolvedImport
from HistoricalPricesData import Interface as HistoricalPricesData  #@UnresolvedImport
from EarningsData import Interface as EarningsData #@UnresolvedImport
import Utility

"""Big Store Retailers """
# list = ['WMT', 'PSMT', 'DG', 'COST', 'DLTR', 'TGT', 'BIG', 'BURL']
"""Home Improvement Stores """
# list = ['HD', 'LOW']
"""Biotech """
# ['AMGN', 'BIIB', 'GILD', 'IMMY', 'JAGX', 'NK', 'PSTI', 'RXII', 'ALXN', 'CELG', 'ILMN', 'REGN', 'VRTX', 'BMRN', 'INCY', 'ACAD', 'ALNY', 'TECH', 'BLUE', 'CBPO', 'CLVS', 'EXEL', 'ICPT', 'JAZZ', 'JUNO', 'KITE', 'LGND', 'OPK', 'SGEN', 'TSRO', 'RARE', 'XON']
"""Consumer Goods"""
# ['KO', 'DPS', 'MNST', 'PEP', 'FIZZ', 'CCE']
"""Regional Airlines"""
# ['ALGT', 'LUV', 'ALK', 'HA', 'JBLU', 'AAL', 'DAL', 'UAL', 'SAVE']
"""P&C Insurance"""
# ['BRKB', 'UVE', 'AIG', 'CB', 'CINF', 'HIG', 'L', 'PGR', 'TRV', 'XL', 'ANAT', 'AFSI', 'ACGL', 'ESGR', 'NGHC', 'SIGI', 'Y', 'AFG', 'AHL', 'AXS', 'CNA', 'RE', 'FAF', 'KMPR', 'MKL', 'MCY', 'MTG', 'ORI', 'RDN', 'RNR', 'RLI', 'THG', 'VR', 'WRB', 'WTM', 'AMSF', 'AGII', 'EMCI', 'GBLI', 'IPCC', 'JRVR', 'SAFT', 'STFC', 'NAVG']
"""Money Center Banks """
# ['BLMT', 'SFBC', 'SFST', 'C', 'JPM', 'PNC', 'STI', 'WFC', 'HOMB', 'BAC', 'GWB', 'STL', 'GNBC', 'NCBS', 'RNST', 'STBZ']
"""Regional - SE Banks """
# ['OZRK', 'BBT', 'RF', 'HBHC', 'IBKC', 'PNFP', 'TRMK', 'BXS', 'FNB', 'FHN', 'CBF', 'CSFL', 'CTBI', 'NCOM', 'PSTB', 'RBCAA']
"""Oil and Gas"""
# ['CVX', 'XOM', 'IMO', 'EQGP','APC', 'APA', 'COG', 'CHK', 'XEC', 'COP', 'DVN', 'EOG', 'EQT', 'HES', 'MRO', 'MUR', 'NFX', 'NBL', 'OXY', 'PXD', 'RRC', 'SWN', 'CRZO', 'FANG', 'GPOR', 'PDCE', 'BSM', 'CPE', 'CNX', 'CLR', 'EGN', 'ENLK', 'EPD', 'KOS', 'LPI', 'MTDR', 'NFG', 'OAS', 'PE', 'RICE', 'SM', 'WPX']
"""High ROIC"""
# ['AHGP', 'ARLP', 'GOOGL', 'AMWD', 'AMGN', 'ANSS', 'AAPL', 'ATRI', 'BIIB', 'CBOE', 'CERN', 'CTSH', 'CPRT', 'DORM', 'EBIX', 'EXPO', 'FFIV', 'FB', 'FAST', 'GNTX', 'THRM', 'GILD', 'HNNA', 'IDXX', 'ISRG', 'IPGP', 'IRMD', 'JBHT', 'JKHY', 'LNTH', 'MANH', 'MKTX', 'EGOV', 'ODFL', 'ORLY', 'PYPL', 'QCOM', 'ROST', 'SEIC', 'SWKS', 'SYNT', 'TROW', 'TXRH', 'CAKE', 'ULTA', 'UTMD', 'WDFC', 'WINA', 'ACN', 'AYI', 'AZO', 'CHE', 'CMI', 'DPZ', 'DCI', 'FDS', 'GPS', 'GPC', 'HD', 'HRL', 'MMS', 'NEU', 'NKE', 'NUS', 'OOMA', 'PII', 'PRLB', 'RHT', 'RMD', 'ROL', 'SBH', 'SNA', 'LUV', 'TJX', 'TSE', 'TYL', 'UVE', 'USNA', 'WDR', 'MMM', 'ABBV', 'ADBE', 'APD', 'ALLE', 'MO', 'AMZN', 'ABC', 'AON', 'AMAT', 'AVY', 'BCR', 'BAX', 'BBBY', 'BBY', 'HRB', 'BA', 'BMY', 'CHRW', 'CELG', 'CHTR', 'CTXS', 'CLX', 'COH', 'CL', 'GLW', 'COST', 'DLPH', 'DAL', 'DNB', 'EW', 'EA', 'EL', 'EXPE', 'EXPD', 'FMC', 'FL', 'GRMN', 'GD', 'HAS', 'HPQ', 'ITW', 'ILMN', 'INTC', 'ICE', 'IBM', 'IPG', 'IFF', 'INTU', 'JNJ', 'JNPR', 'KMB', 'KLAC', 'LB', 'LRCX', 'LEG', 'LLY', 'LMT', 'LOW', 'LYB', 'MMC', 'MAS', 'MA', 'MAT', 'MCD', 'MCK', 'MRK', 'MTD', 'KORS', 'MCHP', 'MU', 'MSFT', 'MON', 'MNST', 'MSI', 'NDAQ', 'NTAP', 'NFLX', 'NOC', 'NVDA', 'OMC', 'PAYX', 'PM', 'PPG', 'PG', 'PSA', 'QRVO', 'RTN', 'REGN', 'RHI', 'ROK', 'CRM', 'STX', 'SEE', 'SHW', 'SPGI', 'SBUX', 'TEL', 'TGNA', 'TDC', 'TXN', 'HSY', 'TSCO', 'TRIP', 'UPS', 'URBN', 'VFC', 'VAR', 'VRSN', 'VRTX', 'WAT', 'WLTW', 'XLNX', 'YUM', 'ZTS', 'DISH', 'INCY', 'MXIM', 'SIRI', 'ABMD', 'AEIS', 'AMD', 'ALGN', 'ATHN', 'BLKB', 'BUFF', 'BRCD', 'BRKR', 'CDNS', 'CACQ', 'CDK', 'CBPO', 'CMPR', 'CRUS', 'CGNX', 'CBRL', 'CREE', 'CRTO', 'EFII', 'ERIE', 'EXEL', 'FNSR', 'FIVE', 'FTNT', 'LOPE', 'HA', 'HDS', 'HCSG', 'HQY', 'IDTI', 'IDCC', 'IONS', 'JACK', 'LANC', 'LSTR', 'LECO', 'LOGI', 'LULU', 'LITE', 'MTSI', 'MASI', 'MTCH', 'MDSO', 'MLNX', 'MELI', 'MSTR', 'MKSI', 'MPWR', 'MORN', 'FIZZ', 'NATI', 'ODP', 'OTEX', 'PZZA', 'PEGA', 'PPC', 'POOL', 'POWI', 'RGLD', 'SAFM', 'SANM', 'SGEN', 'SMTC', 'SLAB', 'STMP', 'SHOO', 'SNPS', 'TTWO', 'ULTI', 'UBNT', 'UTHR', 'OLED', 'VIAV', 'CQH', 'AB', 'AEO', 'ANET', 'APAM', 'ALV', 'BIG', 'EAT', 'BR', 'BC', 'BG', 'BURL', 'BWXT', 'CRI', 'CHH', 'CIEN', 'CNX', 'CLB', 'DAN', 'DRI', 'DLX', 'DLB', 'EV', 'ENR', 'EQM', 'ESNT', 'EVR', 'FICO', 'FII', 'FDC', 'FTV', 'FIG', 'GMED', 'HLF', 'HII', 'HUN', 'KEYS', 'LAZ', 'LCII', 'LEA', 'LII', 'PAYC', 'RYN', 'SHLX', 'SSD', 'AOS', 'DATA', 'TEN', 'TNH', 'TPL', 'THO', 'TTC', 'TUP', 'USG', 'VLP', 'VEEV', 'VMW', 'WBC', 'WST', 'WSM', 'YELP', 'MIK', 'NVR', 'TREX']


"""---------------------------------------
Compare
----------------------------------------"""  
# comp = IndexData.getCompetitors('COP')
# list = []
# for i in comp:
#     list.append(i[0])
#     print(i)  
# print(list)

"""---------------------------------------
CAGR Book/Shareholders Equity
----------------------------------------"""  
# list = ['BRKB', 'UVE', 'AIG', 'CB', 'CINF', 'HIG', 'L', 'PGR', 'TRV', 'XL', 'ANAT', 'AFSI', 'ACGL', 'ESGR', 'NGHC', 'SIGI', 'Y', 'AFG', 'AHL', 'AXS', 'CNA', 'RE', 'FAF', 'KMPR', 'MKL', 'MCY', 'MTG', 'ORI', 'RDN', 'RNR', 'RLI', 'THG', 'VR', 'WRB', 'WTM', 'AMSF', 'AGII', 'EMCI', 'GBLI', 'IPCC', 'JRVR', 'SAFT', 'STFC', 'NAVG',
#        'BLMT', 'SFBC', 'SFST', 'C', 'JPM', 'PNC', 'STI', 'WFC', 'HOMB', 'BAC', 'GWB', 'STL', 'GNBC', 'NCBS', 'RNST', 'STBZ','OZRK', 'BBT', 'RF', 'HBHC', 'IBKC', 'PNFP', 'TRMK', 'BXS', 'FNB', 'FHN', 'CBF', 'CSFL', 'CTBI', 'NCOM', 'PSTB', 'RBCAA' ]
# list = ['BRKB', 'MKL', 'BAC', 'JPM', 'WFC']
# averageBook = []
# for i in list:
#     stats = Ratios.TickerFundamentals(i)
#     stats = stats.getBookValue()
# #     if(stats[5] <= 1.25 and stats[5] >= 0.5):
#     averageBook.append(stats[3])
#     print(i + " : CAGR Book/Share = " + "{0:.2f}".format(stats[0]) + " : P/B = " + "{0:.2f}".format(stats[1]) +
#          " : CAGR Equity = " + "{0:.2f}".format(stats[2]) + " : My P/B = " + "{0:.2f}".format(stats[3])  +
#            " : CAGR Tangible Equity = " + "{0:.2f}".format(stats[4]) + " My Tangible P/B = " + "{0:.2f}".format(stats[5]))
#         
# averageBookValue = sum(averageBook)/len(averageBook)
# print(averageBookValue)

"""-----------------------------------------------------------------------------------
Screens all stocks in list 
-----------------------------------------------------------------------------------"""   
# list = IndexData.getList()
# # list = ['ALGT', 'AHGP', 'ARLP', 'GOOGL', 'AMWD', 'AMGN', 'ANSS', 'AAPL', 'ATRI', 'OZRK', 'BIIB', 'BOFI', 'BWLD', 'CBOE', 'CERN', 'CTSH', 'CPRT', 'CACC', 'DORM', 'EGBN', 'EBIX', 'EXPO', 'FFIV', 'FB', 'FAST', 'FFIN', 'GNTX', 'THRM', 'GILD', 'GBCI', 'HNNA', 'HSIC', 'IDXX', 'ISRG', 'IPGP', 'JBHT', 'JKHY', 'LKFN', 'MANH', 'MKTX', 'EGOV', 'NFBK', 'ODFL', 'ORLY', 'ORIT', 'PRXL', 'PSMT', 'QCOM', 'ROST', 'SEIC', 'SFBS', 'SWKS', 'SYNT', 'TROW', 'TLGT', 'TCBI', 'TXRH', 'CAKE', 'ULTA', 'UTMD', 'WASH', 'WDFC', 'WINA', 'ACN', 'AYI', 'AMP', 'APH', 'AZO', 'CHE', 'CMG', 'CHD', 'CMI', 'DG', 'DPZ', 'DCI', 'FDS', 'GPS', 'GPC', 'HXL', 'HD', 'HRL', 'KNX', 'LCI', 'MMP', 'MMS', 'MCO', 'MSM', 'NEU', 'NKE', 'NUS', 'PII', 'PRLB', 'RHT', 'RMD', 'ROL', 'SBH', 'SNA', 'LUV', 'TJX', 'TMK', 'TYL', 'UVE', 'USNA', 'GWW', 'WDR', 'DIS', 'WAB', 'WLK', 'MMM', 'ABT', 'ABBV', 'ATVI', 'ADBE', 'AAP', 'AFL', 'ALK', 'ALXN', 'MO', 'AMZN', 'AIG', 'ADI', 'AMAT', 'ADSK', 'AVY', 'BCR', 'BAX', 'BBBY', 'BBY', 'HRB', 'BA', 'BMY', 'AVGO', 'CHRW', 'CA', 'CELG', 'CB', 'CINF', 'CTAS', 'CSCO', 'CTXS', 'CLX', 'COH', 'CL', 'COST', 'DLPH', 'DAL', 'DFS', 'DLTR', 'DPS', 'DD', 'DNB', 'EMR', 'EL', 'EXPE', 'EXPD', 'FITB', 'FLIR', 'FL', 'GRMN', 'GD', 'HAS', 'HON', 'HPQ', 'HBAN', 'ITW', 'ILMN', 'INTC', 'IBM', 'IFF', 'INTU', 'JNJ', 'JNPR', 'KEY', 'KMB', 'KLAC', 'LB', 'LRCX', 'LLY', 'LMT', 'LOW', 'LYB', 'MAR', 'MMC', 'MAS', 'MA', 'MAT', 'MCD', 'MCK', 'MJN', 'MRK', 'MTD', 'KORS', 'MCHP', 'MU', 'MSFT', 'MON', 'MNST', 'MSI', 'NTAP', 'NFLX', 'JWN', 'NOC', 'NVDA', 'OMC', 'ORCL', 'PFE', 'PM', 'PPG', 'PFG', 'PGR', 'PSA', 'PHM', 'RTN', 'REGN', 'RAI', 'RHI', 'ROK', 'COL', 'CRM', 'SNI', 'STX', 'SHW', 'SPGI', 'SBUX', 'SYMC', 'TEL', 'TDC', 'TXN', 'HSY', 'TSCO', 'TRIP', 'FOX', 'USB', 'UPS', 'UTX', 'URBN', 'VFC', 'VAR', 'VRSN', 'VRSK', 'VRTX', 'V', 'WMT', 'WAT', 'WDC', 'XLNX', 'YHOO', 'YUM', 'ZTS', 'DISH', 'INCY', 'MXIM', 'SHPG', 'SIRI', 'ABMD', 'ACIW', 'AEIS', 'AMD', 'ALGN', 'ANAT', 'ACGL', 'ARCC', 'ARRS', 'BEAV', 'TECH', 'BLKB', 'BRCD', 'BRKR', 'CDNS', 'CALM', 'CFFN', 'CAVM', 'CBPO', 'CMPR', 'CRUS', 'CGNX', 'COHR', 'CBSH', 'CVLT', 'CBRL', 'CREE', 'CVBF', 'CY', 'DXCM', 'EWBC', 'EFII', 'EXEL', 'FNSR', 'FIVE', 'FTNT', 'LOPE', 'HCSG', 'HOMB', 'HOPE', 'IDTI', 'IDCC', 'ISBC', 'IONS', 'JJSF', 'JACK', 'JAZZ', 'LANC', 'LSTR', 'LGND', 'LECO', 'LOGI', 'LOGM', 'LULU', 'MRVL', 'MASI', 'MDSO', 'MLNX', 'MELI', 'MSTR', 'MPWR', 'MORN', 'FIZZ', 'NATI', 'NTCT', 'NDSN', 'OTEX', 'OPK', 'PZZA', 'PEGA', 'PPC', 'POOL', 'POWI', 'PTC', 'RP', 'RGLD', 'SAFM', 'SANM', 'SGEN', 'SLAB', 'SAVE', 'STMP', 'SHOO', 'SNPS', 'TTWO', 'TFSL', 'PCLN', 'ULTI', 'TRMB', 'UBNT', 'UCBI', 'UTHR', 'OLED', 'WWD', 'ALX', 'AEO', 'NLY', 'AHL', 'AGO', 'ALV', 'BOH', 'BKU', 'BIG', 'BAH', 'EAT', 'BR', 'BC', 'BWXT', 'BXMT', 'CRI', 'CIM', 'CHH', 'CIEN', 'CNX', 'CLB', 'DRI', 'DLX', 'DKS', 'DLB', 'DRQ', 'ELLI', 'EPAM', 'EQM', 'EVR', 'RE', 'FICO', 'FII', 'FIG', 'FSIC', 'GME', 'IT', 'GMED', 'GGG', 'GWRE', 'HLF', 'ITT', 'JBT', 'KKR', 'LVS', 'LAZ', 'LCII', 'LEA', 'LII', 'MFA', 'MTG', 'MSA', 'MSCI', 'NRZ', 'ORI', 'PRA', 'Q', 'RDN', 'RYN', 'RGA', 'RNR', 'RLI', 'AOS', 'STWD', 'SNV', 'DATA', 'TEN', 'TER', 'TNH', 'TPL', 'THO', 'TTC', 'TUP', 'VC', 'VMW', 'GRA', 'WBC', 'WBS', 'WAL', 'WTM', 'WSM', 'YELP', 'NVR', 'TREX']
# badlist = []
# screen = []
# 
# print('start')
# for i in list:
#     try:
#         Analyze.screen(i)
#     except:
#         print('error')
#         badlist.append(i)
# 
# print(badlist)
# print(screen)
# print(len(screen))
# 
# HistoricalPricesData.updateAllHistoricalPrices()
# EarningsData.updateAll()
# print('complete')
Analyze.screenAll()
# print('total complete')

