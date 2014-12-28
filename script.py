import re
import csv
input_file = open("amp-unorganised-location.csv",'rU')
data = []
dist=""
city=""
for row in input_file:
    data.append(row.strip().split(','))
#print data
data[0].append("City")


for i in range(1,len(data)):
    if(len(data[i])==4):
        #print data[i]
        ampid=data[i][0]
        proj_title=data[i][1]
        status = data[i][2]
        while(i<17 and len(data[i+1])==1):
            district=data[i+1][0]
            data[i+1]=[]
            data[i+1].append(ampid)
            data[i+1].append(proj_title)
            data[i+1].append(status)
            data[i+1].append(district)
    if(data[i][3]==''):
        distr=['','']
    else:
        distr=data[i][3].split("(")
    rem = '-")'
    city = distr[1]
    dist = distr[0]
    city = re.sub('[-")]','',city)
    dist=re.sub('[-")]','',dist)
    data[i][3]=dist
    data[i].append(city)
with open("output.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(data)
