import matplotlib.pyplot as plt

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,edgecolor='none',s = 40)
#设置图表标题并给坐标轴加上指定标签
plt.title('square numbers',fontsize=24)
plt.xlabel('values',fontsize=14)
plt.ylabel('square of values',fontsize=14)

#设置刻度标记的大小
plt.axis([0,1100,0,1100000])
plt.tick_params(axis = 'both',which='major',labelsize=1)

plt.savefig('square',bbox_inches = 'tight')
plt.show()