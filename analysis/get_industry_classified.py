# coding=gbk
# -*- coding: utf-8 -*-
from __future__ import print_function
import tushare as ts
from openpyxl import load_workbook
import sys, os
import datetime
import time

dir=os.getcwd() + "/"
filepath_list={}
industry_list=[]
file_list= dir + "filelist.txt"
filter_list= dir + "filterlist.txt"
mydatetime=str(time.strftime("-%d-%m-%Y"))

# get file list;
fp=open(file_list)
for lines in fp.readlines():
	lines=lines.replace("\n","")
	tempitem=lines.split(',')
	#print(tempitem),;
	filepath_list[str(tempitem[0])]=str(tempitem[1])
	#print(filepath_list),;
fp.close()
print("file path list:"),;
print(filepath_list),;

#get industry type list
fp=open(filter_list)
for lines in fp.readlines():
	lines=lines.replace("\n","")
	industry_list.append(lines);
	#print(str(lines).decode('utf-8').encode('gbk')),;
fp.close()
print("industry list:"),;
print(industry_list),;

#load xlsx file
industry_file=filepath_list["get_industry_classified"]
wb2 = load_workbook('test.xlsx')
print wb2.get_sheet_names()
