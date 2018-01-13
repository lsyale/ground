from __future__ import print_function
import tushare as ts
import sys, os

dir=os.getcwd() + "/"
functions=[]
functions_list= dir + "function_list.txt"

print("get tushare function list"),;
fp=open(functions_list)
for lines in fp.readlines():
	lines=lines.replace("\n","")
	functions.append(lines)
fp.close()

print("get global ecomy month data"),;
for function in functions:			
	fun="ts."+function
	#name=dir + function + ".xlsx"
	#funs=fun+"("+")"+".to_excel('"+name+"')"	
	name=dir + function + ".csv"
	funs=fun+"("+")"+".to_csv('"+name+"')"	
	if os.path.exists(name):
		os.remove(name)
	try:
		exec(funs)
		print(name),;
	except Exception, e:
		print(e),;
		print("######################Error:###################"),;
		print(funs),;
