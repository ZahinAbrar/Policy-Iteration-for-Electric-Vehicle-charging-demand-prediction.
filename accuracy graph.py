import matplotlib.pyplot as plt
import seaborn as sns
#
# x=[10,20,30,40,50,60,70,80]
# y=[25,54.74,55.89,69.68,65.23,67.09,52.44,64.22]
#
# plt.plot(x,y)
# plt.xlabel('Epochs')
# plt.ylabel('Accuracey')
# plt.title('RNN Model for accuracy prediction for a sample station')
# plt.savefig('RNN.png')
# plt.clf()
#
# x=[500,1000,1500,2000,2500,3000,3500,4000,4500,5000,5500]
# y=[249/696,293/696,336/696,364/696,385/696,417/696,422/696,420/696,389/696,464/696,419/696,444/696]
#
# plt.plot(x,y)
# plt.xlabel('Epochs')
# plt.ylabel('Accuracey')
# plt.title('NN Model for accuracy prediction for a sample station')
# plt.savefig('NN.png')

draw=[[5,4,2,0,20],[5,4,2,60,4],[1,6,60,7,3],[2,40,9,7,7],[30,4,9,8,3]]
plt.figure(figsize=(6, 10))
ax = sns.heatmap(draw, cmap="Reds")
ax.set_yticklabels([ 4, 3, 2, 1, 0])
ax.set_xticklabels([ 0,1,2,3,4])
plt.yticks(rotation=70)
xmin, xmax = plt.xlim()
ymin, ymax = plt.ylim()
plt.title('1407')
plt.xlabel('Actual Kw')
plt.ylabel('Predicted Kw')

plt.savefig('stations.png')
plt.clf()