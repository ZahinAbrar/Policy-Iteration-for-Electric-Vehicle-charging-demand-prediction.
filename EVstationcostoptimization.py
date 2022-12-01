import EV_valueiteration as EVV
import data
from datetime import datetime
import matplotlib.pyplot as plt
import pytz
# profit=[]
# shortprofit=[]
# for solarcapacity in range(20,21,5):
#     # shortprofit=[]
#     utc = datetime.today()
#     timezone = pytz.timezone('US/Mountain')
#     nowTime = timezone.localize(utc).replace(hour=6,minute=0, second=0, microsecond=0)
#
#     data.calculatesupplyanddemand(nowTime=nowTime,MaxSolar=0,MaxTime=96)
profitlist=[]
batterylist=[]
for batterycapacity in range(25,26,5):
    batterylist.append(batterycapacity)
    final=EVV.optimizer(sampletime=15,batterypanalty=0.01,numberOfhours=2*24,gamma=1,maxsolar=0,maxload=0,batterymaxenergy=batterycapacity,energysample=10)
    profitlist.append(final)
    print(batterycapacity)
    print(final)
        # shortprofit.append(final)
        # print(solarcapacity,batterycapacity)
        # print(final)
    # profit.append(shortprofit)

# file=open('finalValue.txt')
# file.write(profit)

# plt.plot(batterylist,profitlist)
# plt.xlabel('Battery Capacity in KW')
# plt.ylabel('Profit in dollar')
# plt.title('Total profit by varying battery capacity')
# plt.savefig('Total profit by varying battery capacity.png')