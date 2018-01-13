from __future__ import print_function
import tushare as ts
import sys, os
#ts.get_report_data(year,month).to_excel(name)

function=sys.argv[0][sys.argv[0].rfind(os.sep)+1:]
function=function.split('.')[0]
dir="/home/ls/Documents/stork/stork_basic/"
#function="get_report_data"
fun="ts."+function
#year="2017"
#month="1"
#name=dir + function +"_"+year+"_"+month".xlsx"
#funs=funs+"("+year+","+month+")"+".to_excel('"+name+"')"
#print(funs)
#exec(funs)
for year in range(2006,2018):
	for month in range(1,5):
		#print(year,month)
		name=dir + function +"-"+str(year)+"-"+str(month)+".xlsx"
		funs=fun+"("+str(year)+","+str(month)+")"+".to_excel('"+name+"')"
		print(name),;
		print(funs),;
#		exec(funs)
#		ts.get_report_data(year,month).to_excel(name)
