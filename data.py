import pytz
from datetime import datetime, timedelta
import random
import pandas as pd
import test

timeZone = pytz.timezone('US/Mountain')
def calculatesupplyanddemand(nowTime=0,MaxTime=96,sampleTime=15,MaxSolar=60,MaxLoad=40):
    demand=test.calculateDemand(MaxTime=MaxTime)
    offPrice = 0.065
    peakPrice = 0.132
    midPrice = 0.094
    winterCost = [offPrice, peakPrice, midPrice, peakPrice, offPrice]
    winterZone = ['off', 'peak', 'mid', 'peak', 'off']
    summerCost = [offPrice, midPrice, peakPrice, midPrice, offPrice]
    summerZone = ['off', 'mid', 'peak', 'mid', 'off']

    zonelist=[]
    pricelist=[]

    solar=[]
    d=[]
    for i in range(0,MaxTime):
        if nowTime.hour <= 7:
            hourSection = 0
        elif nowTime.hour <= 11:
            hourSection = 1
        elif nowTime.hour <= 17:
            hourSection = 2
        elif nowTime.hour <= 19:
            hourSection = 3
        else:
            hourSection = 4

        if nowTime.strftime("%a") in ['Saturday', 'Sunday']:
            zone = 'off'
            price = offPrice
        else:
            if (nowTime >= datetime(2018, 11, 1, 0, 0, 0, 0, timeZone) and
                    nowTime <= datetime(2019, 4, 30, 0, 0, 0, 0, timeZone)):
                # winter
                price = winterCost[hourSection]
                zone = winterZone[hourSection]
            else:
                price = summerCost[hourSection]
                zone = summerZone[hourSection]

        zonelist.append(zone)
        pricelist.append(price)

        if nowTime.hour>=6 and nowTime.hour<18:
            solar.append(random.randint(0,MaxSolar))
        else:
            solar.append(0)


        d.append([solar[i],demand[i],pricelist[i],zonelist[i]])
        nowTime=nowTime+timedelta(minutes=sampleTime)



    dataframe = pd.DataFrame(
    {'Solar': solar,
     'Demand': demand,
     'Price': pricelist,
     'Zone': zonelist
    })
    dataframe.to_csv('predict.csv',sep=',')



# nowTime = timeZone.localize(datetime.today()).replace(minute=0, second=0, microsecond=0)

