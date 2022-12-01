import pandas as pd
from haversine import haversine
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv('Station-table-all-columns-20190320.csv')
charging_info=pd.read_csv('Session-Details-Summary-20190329.csv')
charging_info['Start Date']=pd.to_datetime(charging_info['Start Date'])
unique_stations=data.drop_duplicates(subset=['Address 1'])
charging_info['Port Number'] = charging_info['Port Number'].str.replace(r'\D+', '')

station_list=[]

for i in range(0,1):
    single_station_hourly_charging_pattern = []
    station_list = []

    for j in range(0,len(data)):

        if unique_stations['Address 1'].iloc[i]==data['Address 1'].iloc[j]:

            name=data['Address 1'].iloc[j]

            single_port_hourly_charging_pattern = []
            port_name=data['Station Name'].iloc[j]+" slot"+str(l+1)
            station_list.append(port_name)
            single_station=charging_info[(charging_info['Station Name']==data['Station Name'].iloc[j])&(pd.to_numeric(charging_info['Port Number'])==l+1)]
            print(port_name)
            for m in range(0,24):
                    total=0
                    totalenergy=0
                    totalenergy = single_station[(single_station['Start Date'].dt.hour == m)]

                    total = totalenergy['Energy (kWh)'].sum()
                    single_port_hourly_charging_pattern.append(total)
                # total=0
                # totalenergy = single_station[(single_station['Start Date'].dt.hour == 9)]
                #
                # total = totalenergy['Energy (kWh)'].sum()

            single_station_hourly_charging_pattern.append(single_port_hourly_charging_pattern)

    plt.figure(figsize=(10,8))
    length=len(single_station_hourly_charging_pattern)
    for p in range(0,length):
        plt.subplot(length,1,p+1,)
        plt.step([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23],single_station_hourly_charging_pattern[p])
        plt.ylabel(station_list[p],rotation=70)

    name += 'graph.png'
    plt.savefig(name)
    plt.clf()
    plt.figure(figsize=(10,8))
    ax=sns.heatmap(single_station_hourly_charging_pattern,linewidths=0.5,cmap="Reds")
    ax.set_yticklabels(station_list)
    plt.yticks(rotation=70)
    xmin, xmax = plt.xlim()
    ymin, ymax = plt.ylim()
    name+='.png'
    plt.savefig(name)
    plt.clf()
# data=pd.read_csv('Session-Details-Summary-20190306.csv')
# data.columns=data.columns.str.replace(' ','_')
# data.columns=data.columns.str.replace(':','_')
# data.columns=data.columns.str.replace('(','')
# data.columns=data.columns.str.replace(')','')
# print(data.columns)
#
#
# d=data.drop_duplicates(subset=['Latitude','Longitude'])
#
# k=0
# print(len(d))
# for j in range(0,72):
#   if float(d['Latitude'].iloc[j])>0.0:
#       k = k + 1
#       print("Cluster No ",k)
#
#       print(d['Station_Name'].iloc[j])
#       for i in range(j+1,73):
#
#
#           if haversine((float(d['Latitude'].iloc[j]),float(d['Longitude'].iloc[j])),(float(d['Latitude'].iloc[i]),float(d['Longitude'].iloc[i])),unit='mi')<=0.002:
#               d.iat[i,23]=0.0
#               d.iat[i,24]=0.0
#
#               print(d['Station_Name'].iloc[i])
#
#       d.iat[j, 23] = 0.0
#       d.iat[j, 24] = 0.0
#       print("\n\n\n")



