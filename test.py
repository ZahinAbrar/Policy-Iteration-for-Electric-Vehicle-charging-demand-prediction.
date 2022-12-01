import pandas as pd
from datetime import datetime,timedelta
import pytz
import math
import matplotlib.pyplot as plt

data_frame = pd.read_csv('Session-Details-Summary-20190329.csv')

data_frame['Start Date'] = pd.to_datetime(data_frame['Start Date'])


start_date = pd.to_datetime('12-14-2018')

single_station = data_frame[data_frame['Address 1'] == '55 East 300 South']
single_day=single_station[(
                    single_station['Start Date'].dt.year == start_date.year) & (
                                                 single_station['Start Date'].dt.month == start_date.month) & (
                                                 single_station['Start Date'].dt.day == start_date.day)]



# utc = datetime.today()
# timezone = pytz.timezone('US/Mountain')
# nowTime = timezone.localize(utc).replace(year=2018,month=12,day=13, hour=0,minute=0, second=0, microsecond=0)
# demand=[]
#
# for i in range(0,96):
#     time_slot_energy=single_station[(
#                     single_station['Start Date'].dt.hour == nowTime.hour)]
#     demand.append(time_slot_energy['Energy (kWh)'].sum())
#     demand[i]=demand[i]*10/4
#     nowTime = nowTime + timedelta(minutes=15)
#
# print(demand)
# High=max(demand)
# low=min(demand)
# price=[]
# index=[]
# for i in range(0,96):
#     index.append(i)
#     price.append(math.exp((demand[i] - low) / (High - low)) * 0.07)
#     # income = (demand[i] * price / 10) * -1
#
#
# f, axarr = plt.subplots(2, sharex=True, figsize=(15, 15))
#
# f.subplots_adjust(hspace=0.22)
#
# axarr[0].bar(index, demand, 1.0,
#                         alpha=0.8,
#                         color='salmon',
#                         linewidth=0,
#                         antialiased=True)
# axarr[0].set_ylabel('Energy unit',fontsize=16)
# axarr[0].set_title( 'Demand in Energy Unit',fontsize=16)
#
# axarr[1].bar(index, price, 1.0,
#                         alpha=0.8,
#                         color='skyblue',
#                         linewidth=0,
#                         antialiased=True)
# axarr[1].set_ylabel('Price / KW',fontsize=16)
# axarr[1].set_xlabel('Time',fontsize=16)
# axarr[1].set_title( 'Price based on demand',fontsize=16)
#
# plt.show()

#
def calculateDemand(MaxTime=96):
    start_date = pd.to_datetime('12-11-2018')

    single_station = data_frame[data_frame['Address 1'] == '55 East 300 South']
    single_day = single_station[(
                                    single_station['Start Date'].dt.year == start_date.year) & (
                                    single_station['Start Date'].dt.month == start_date.month) & (
                                    single_station['Start Date'].dt.day == start_date.day)]

    utc = datetime.today()
    timezone = pytz.timezone('US/Mountain')
    nowTime = timezone.localize(utc).replace(year=2018, month=12, day=13, hour=0, minute=0, second=0, microsecond=0)
    demand = []

    for i in range(0, MaxTime):
        time_slot_energy = single_station[(single_station['Start Date'].dt.hour == nowTime.hour)&(single_station['Start Date'].dt.day == nowTime.day)&(single_station['Start Date'].dt.month == nowTime.month)]
        demand.append(time_slot_energy['Energy (kWh)'].sum())

        nowTime = nowTime + timedelta(minutes=15)

    return demand