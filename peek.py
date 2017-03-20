import gzip

with gzip.open('ebd_sampling_relAug-2015.txt.gz', 'rb') as rawData:
    with open('peek.txt','w') as resultData1:
        for i in range(1,100):
            resultData1.write(rawData.readline())
