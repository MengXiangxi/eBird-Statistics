import gzip

species1 = 'Parus minor'
species2 = 'Parus major'
species3 = 'Parus cinereus'
species4 = 'Parus bokharensis'
species5 = 'Apus apus'
mat = [[0 for col in range(360)] for row in range(180)]
linenum = 0

with gzip.open('ebd_relAug-2015.txt.gz', 'rb') as rawData,\
    open(species1+'.txt','w') as resultData1,\
    open(species2+'.txt','w') as resultData2,\
    open(species3+'.txt','w') as resultData3,\
    open(species4+'.txt','w') as resultData4,\
    open(species5+'.txt','w') as resultData5,\
    open('density_mat.txt','w') as densemat:
    rawData.readline()
    for entry in rawData:
        latind = int(float(entry.split('\t')[22])) + 89
        longind = int(float(entry.split('\t')[23])) + 179
        mat[latind][longind] += 1
        linenum += 1
        if entry.split('\t')[4] == species1:
            resultData1.write(entry)
        elif entry.split('\t')[4] == species2:
            resultData2.write(entry)
        elif entry.split('\t')[4] == species3:
            resultData3.write(entry)
        elif entry.split('\t')[4] == species4:
            resultData4.write(entry)
        elif entry.split('\t')[4] == species5:
            resultData5.write(entry)
    densemat.writelines('\n'.join([' '.join(c for c in row) for row in mat]))
