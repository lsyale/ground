from __future__ import print_function
import tushare as ts
import sys, os
import datetime
import time

dir=os.getcwd() + "/"
functions=[]
functions_list= dir + "function_list.txt"
mydatetime=str(time.strftime("-%d-%m-%Y"))
tempdata_dir= dir + "../tempdata/"

print("get tushare function list"),;
fp=open(functions_list)
for lines in fp.readlines():
	lines=lines.replace("\n","")
	functions.append(lines)
fp.close()

print("get global ecomy month data"),;
for function in functions:			
	fun="ts."+function
	name=tempdata_dir + function + mydatetime +".xlsx"
	funs=fun+"("+")"+".to_excel('"+ name +"')"	
	if os.path.exists(name):
		#os.remove(name)
		continue
	try:
		exec(funs)
		print(name),;
	except Exception, e:
		print(e),;
		print("######################Error:###################"),;
		print(funs),;
