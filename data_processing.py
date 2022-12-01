import pandas as pd
import matplotlib.pyplot as plt
import datetime as datetime
data=pd.read_table('Session-Details-Summary-20190306.csv',',')
data.columns=data.columns.str.replace(' ','_')
data.columns=data.columns.str.replace(':','_')
data.columns=data.columns.str.replace('(','')
data.columns=data.columns.str.replace(')','')

#file=open('liberty_park.csv','w')
#file.write(data[data.Station_Name=='PUBLIC USE / LIBERTY PARK'].to_string())
#file.close()

stations=list(set(data.Station_Name))


for i in range(0,len(stations)):
    stationname=stations[i] +'.csv'
    stationname=stationname.replace(' ','')
    stationname = stationname.replace('/','_')

    df=data[data.Station_Name==stations[i]]
    df.to_csv(stationname,index=None,header=True)


stationname = stations[0] + '.csv'
stationname = stationname.replace(' ', '')
stationname = stationname.replace('/', '_')
singlestationdata=pd.read_csv(stationname)


singlestationdata['Start_Date']=pd.to_datetime(singlestationdata['Start_Date'])

#calculating the month energy use
month=[]
for i in range(1,13):
    totalenergy=0
    totalenergy=singlestationdata[(singlestationdata['Start_Date'].dt.month==i) & (singlestationdata['Start_Date'].dt.year<=2019)]

    total=totalenergy['Energy_kWh'].sum()
    month.append(total/6)

print(month)
x=[1,2,3,4,5,6,7,8,9,10,11,12]
plt.plot(x,month)
plt.xlabel('Months')

plt.ylabel('Energy used')
plt.title('%s monthly energy use rate.'% (stations[0]))
plt.show()


#calculating the whole year energy use
years=[]
for i in range(2013,2019):
    totalenergy=0
    totalenergy=singlestationdata[(singlestationdata['Start_Date'].dt.year==i)]

    total=totalenergy['Energy_kWh'].sum()
    years.append(total)
totalenergy=singlestationdata[(singlestationdata['Start_Date'].dt.year==2019)]
total=totalenergy['Energy_kWh'].sum()
years.append(total*6)
print(years)
x=[2013,2014,2015,2016,2017,2018,2019]
plt.plot(x,years)
plt.xlabel('years')

plt.ylabel('Energy used')
plt.title('%s yearly energy use rate.'% (stations[0]))
plt.show()

#calculating the energy use rate by hour

hours=[]
for i in range(0,24):
    totalenergy=0
    totalenergy=singlestationdata[(singlestationdata['Start_Date'].dt.hour==i)&(singlestationdata['Start_Date'].dt.year==2018)]

    total=totalenergy['Energy_kWh'].sum()
    hours.append(total/365)

print(hours)
x=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
plt.plot(x,hours)
plt.xlabel('hours')

plt.ylabel('Energy used')
plt.title('%s hourly energy use rate in 2018.'% (stations[0]))
plt.show()

#show the results for individual trips

#individuals=list(set(data.User_ID))


individuals=data[data.User_ID==str(2829181)]
individuals['Start_Date']=pd.to_datetime(individuals['Start_Date'])
individuals=individuals.sort_values(by='Start_Date',ascending=True)

hours=[]
for i in range(0,24):
    total=0
    totalenergy=individuals[(individuals['Start_Date'].dt.hour==i)&(individuals['Start_Date'].dt.year==2018)]

    total=totalenergy['Energy_kWh'].sum()
    hours.append(total)


x=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
plt.plot(x,hours)
plt.xlabel('hours')

plt.ylabel('Energy used')
plt.title('%s hourly energy use rate in 2018 by %s.'% (stations[0],2829181))
plt.show()

usedstation=list(set(individuals.Station_Name))
frequency=[]
for i in range(0,len(usedstation)):
    frequency.append(len(individuals[individuals['Station_Name']==usedstation[i]]))


plt.plot(usedstation,frequency)
plt.xlabel('Station Name')

plt.ylabel('Frequency')
plt.title('How many time %s user use the stations.'% (2829181))
plt.show()
