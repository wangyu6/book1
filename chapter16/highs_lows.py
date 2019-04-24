import csv 
from datetime import datetime
from matplotlib import pyplot as plt
#从文件中获取日期、最高、最低气温
filename = 'death_valley_2014.csv'
with open( filename ) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	# print(header_row)

	# for index, colum_header in enumerate(header_row):
	# 	print(index, colum_header)
	dates, highs, lows = [],[],[]
	for row in reader:
		try:
			current_date = datetime.strptime(row[0],"%Y-%m-%d")
			# dates.append(current_date)
			
			high = int(row[1])
			# highs.append(high)

			low = int(row[3])
			# lows.append(low)
		except ValueError:
			print(current_date,'missng data')
		else:
			dates.append(current_date)
			highs.append(high)
			lows.append(low)
	# print(high)
fig = plt.figure(dpi = 128,figsize=(10,6))
plt.plot(dates, highs,c = 'red')
plt.plot(dates,lows,c='blue')
plt.fill_between(dates,highs,lows,facecolor = 'blue',alpha =0.1)

#设置图形格式
plt.title("daily high tempture- 2014", fontsize=20)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()
plt.ylabel("tempture(F)",fontsize = 16)
plt.tick_params(axis='both',which='major',labelsize=16)

plt.show()