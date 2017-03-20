with open('Swift_all.csv','r') as fin,\
     open('Swift01.csv','w') as fout1,\
     open('Swift02.csv','w') as fout2,\
     open('Swift03.csv','w') as fout3,\
     open('Swift04.csv','w') as fout4,\
     open('Swift05.csv','w') as fout5,\
     open('Swift06.csv','w') as fout6,\
     open('Swift07.csv','w') as fout7,\
     open('Swift08.csv','w') as fout8,\
     open('Swift09.csv','w') as fout9,\
     open('Swift10.csv','w') as fout10,\
     open('Swift11.csv','w') as fout11,\
     open('Swift12.csv','w') as fout12:
     fin.readline()
     temp = [['lat,lon,date\n' for col in range(1)] for row in range(12)]
     for i in fin:
         mon = int(i.split(',')[2].split('/')[1])
         temp[mon-1].append(i)
     for i in temp[0]:
         fout1.write(i)
     for i in temp[1]:
         fout2.write(i)
     for i in temp[2]:
         fout3.write(i)
     for i in temp[3]:
         fout4.write(i)
     for i in temp[4]:
         fout5.write(i)
     for i in temp[5]:
         fout6.write(i)
     for i in temp[6]:
         fout7.write(i)
     for i in temp[7]:
         fout8.write(i)
     for i in temp[8]:
         fout9.write(i)
     for i in temp[9]:
         fout10.write(i)
     for i in temp[10]:
         fout11.write(i)
     for i in temp[11]:
         fout12.write(i)
