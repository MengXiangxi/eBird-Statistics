import gzip

with gzip.open('D:/eBird/ebd_relAug-2015.txt.gz', 'rb') as rawData:
    with open('D:/eBird/peek.txt','w') as resultData1:
        for i in range(1,100):
            data = rawData.readline()
            print(data)
            resultData1.write(data)
