import pandas as pd
import math
import matplotlib.pyplot as plt
import seaborn as sns

data_frame=pd.read_csv('Session-Details-Summary-20190329.csv')

data_frame['Start Date']=pd.to_datetime(data_frame['Start Date'])
data=pd.read_csv('Station-table-all-columns-20190320.csv')
unique_stations=data.drop_duplicates(subset=['Address 1'])

start_date = pd.to_datetime('26-03-2019')

lebely=[]
for i in range(30):
    dat = start_date - pd.to_timedelta(i, 'd')
    date=str(dat.year)+"-"+str(dat.month)+"-"+str(dat.day)
    lebely.append(date)

for i in range(0,1):
    print(i)

    total = [[0 for x in range(30)] for y in range(24)]

    name=unique_stations['Address 1'].iloc[i]
    for j in range(0, len(data)):
        if unique_stations['Address 1'].iloc[i]==data['Address 1'].iloc[j]:


            single_station = data_frame[data_frame['Station Name']==data['Station Name'].iloc[j]]







        #
        #
        #     #length=len(single_station)-2
        #
        #     #day_count = (single_station['Start Date'].iloc[0] - single_station['Start Date'].iloc[length]).days + 1
        #     #print(length,day_count)
        #
        #     #print(single_station['Start Date'].iloc[0] + pd.to_timedelta(l, 'd'))
        #
        #
        #
            for m in range(0,24):
                 for da in range(0,30):
                      dat=start_date - pd.to_timedelta(da, 'd')

                      totalenergy=0
                      totalenergy = single_station[(single_station['Start Date'].dt.hour == m)&(single_station['Start Date'].dt.year == dat.year)&(single_station['Start Date'].dt.month == dat.month)&(single_station['Start Date'].dt.day == dat.day)]

                      total[m][da] += totalenergy['Energy (kWh)'].sum()
                      #print(total[m][da])


    plt.figure(figsize=(8, 6))
    ax = sns.heatmap(total, cmap="Purples")
    ax.set_yticklabels([23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0])
    ax.set_xticklabels(lebely)
    plt.yticks(rotation=70)
    xmin, xmax = plt.xlim()
    ymin, ymax = plt.ylim()
    plt.title(name)
    plt.xlabel('Day of Years')
    plt.ylabel('Hours')
    name += ' year.png'
    plt.show()
    # plt.savefig(name)
    plt.clf()




