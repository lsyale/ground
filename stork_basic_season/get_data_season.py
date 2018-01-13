# coding=utf-8
from __future__ import print_function
import tushare as ts
import sys, os
import datetime
import time

dir=os.getcwd() + "/"
functions=[]
functions_list= dir + "function_list.txt"
mydatetime=str(time.strftime("-%d-%m-%Y"))
get_stock_basics=dir + "get_stock_basics" + mydatetime + ".xlsx"
print(get_stock_basics),;
print("get tushare function list"),;
#sys.exit(0) 
fp=open(functions_list)
for lines in fp.readlines():
	lines=lines.replace("\n","")
	functions.append(lines)
fp.close()

print("get stock basics"),;
ts.get_stock_basics().to_excel(get_stock_basics)

sys.exit(0) 
#function=sys.argv[0][sys.argv[0].rfind(os.sep)+1:]
#function=function.split('.')[0]
#function="get_report_data"
#fun="ts."+function

print("get stock season data"),;
for year in range(2012,2018):
	for month in range(1,5):
		for function in functions:			
			#print(year,month)
			fun="ts."+function
			name=dir + function +"-"+str(year)+"-"+str(month)+".xlsx"
			funs=fun+"("+str(year)+","+str(month)+")"+".to_excel('"+name+"')"
			if os.path.exists(name):
				continue
			else:
				exec(funs)
				print(name),;
				print(funs),;
#		ts.get_report_data(year,month).to_excel(name)
