__author__ = 'Ricardo Pasquini'
#Properati Rent Data Downloader
import urllib.request

fechastodownload=[]

for year in range(2017,2018,1):

    for month in range(1,13,1):
        if len(str(month))<2:
            monthstr='0'+str(month)
        else:
            monthstr=str(month)
        fechastodownload.append(str(year)+"-"+monthstr)

fechastodownload.append('2018-01')
fechastodownload.append('2018-02')
print(fechastodownload)

for fecha in fechastodownload:
    urlstring="https://www.properati.com.ar/data/static/data/AR/properati-AR-"+fecha+"-01-properties-rent.csv.gz"
    urlstring2="https://www.properati.com.ar/data/static/data/AR/properati-AR-"+fecha+"-01-properties-rent-six_months.csv.gz"
    print(urlstring)
    #urllib.request.urlretrieve ("https://www.properati.com.ar/data/static/data/AR/properati-AR-2018-02-01-properties-rent-six_months.csv.gz", "properati/201802.gz")
    try: urllib.request.urlretrieve (urlstring, "data/properati/"+fecha+".gz")
    except urllib.error.HTTPError:
        urllib.request.urlretrieve (urlstring2, "data/properati/"+fecha+".gz")


    print(fecha, "download completed")
    #except:
     #   print("nada")


#https://www.properati.com.ar/data/static/data/AR/properati-AR-2016-02-01-properties-rent.csv.gz