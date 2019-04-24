# from __future__ import (absolute_import, division, print_function, unicode_literals)
# try:
#     #py2.x版本
#     from urllib2 import urlopen
# except ImportError as e:
#     #py 3.x版本
#     from urllib.request import urlopen
import json
import pygal
import	math
from itertools import groupby



def drawline(x_data, y_data, title, y_legend):
	xy_map = []
	for x, y in groupby(sorted(zip(x_data, y_data)), key= lambda _:_[0]):
		y_list = [ v for _ ,v in y]
		xy_map.append([x,sum(y_list) / len(y_list)])
	x_unique, y_mean = [*zip(*xy_map)]
	line_chart = pygal.Line()
	line_chart.title = title
	line_chart.x_labels = x_unique
	line_chart.add(y_legend, y_mean)

	line_chart.render_to_file(title + '.svg')
	return line_chart
# json_url = "https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json"
# response  = urlopen(json_url)

# #读取数据
# req = response.read()
# #将数据写入文件
# with open('btc_close_2017_urllib.json','wb') as f:
#     f.write(req)

# #加载json数据格式
# file_urllib = json.loads(req)
# print(file_urllib)

#将数据加载到一个1列表中
filename = "btc_close_2017_urllib.json"
with open(filename) as f:
    btc_data = json.load(f)
#打印每一天的信息
# for btc_dict in btc_data:
# 	date = btc_dict['date']
# 	month = int(btc_dict['month'])

# 	week = int(btc_dict['week'])
# 	weekday = btc_dict['weekday']
# 	close = int(float(btc_dict['close']))

# 	print("{} is month  {}  week{}".format(date,month,week))

#创建五个列表分别存储日期，和收盘价
dates = []
months = []
weeks = []
weekdays = []
close = []
# # 每一天的信息
for btc_dict in btc_data:
	dates.append(btc_dict['date'])
	months.append(int(btc_dict['month']))
	weeks.append(int(btc_dict['week']))
	weekdays.append(btc_dict['weekday']) 
	close.append(int(float(btc_dict['close']))) 

# line_chart = pygal.Line(x_label_rotation = 20 , show_minor_x_labels = False)
# line_chart.title = "收盘价 对数变换"
# line_chart.x_labels = dates
# N =20 #x轴坐标每隔二十天显示一次
# line_chart.x_labels_major = dates[::N]
# close_log = [math.log10(_) for _ in close]
# line_chart.add('收盘价',close_log)
# line_chart.render_to_file('收盘价对数折线图.svg')
idx_week = dates.index('2017-12-11')
wd = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
weekdays_int = [wd.index(w) + 1 for w in weekdays[1:idx_week]]

line_chart_weekday = drawline(weekdays_int, close[1:idx_week], '收盘价周日均值','周日均值')
line_chart_weekday.x_labels = ['周一 ','周二','周三','周四','周五','周六','周日']
# line_chart_weekday.render_to_file(title + '.svg')
line_chart_weekday.render_to_file('收盘价星期均值.svg')


with open('收盘价dashboard.html','w',encoding = 'utf-8') as html_file:
	html_file.write('<html><head><title>收盘价dashboard</title><meta charset="utf-8"</head></body>\n')
	for svg in ['收盘价折线图.svg','收盘价对数折线图.svg','收盘价日月均值.svg']:
		html_file.write('	<object type = "image/svg+xml" data = "{0}"\
			height = 400></object>\n'.format(svg))
		
	html_file.write('</body></html>')
