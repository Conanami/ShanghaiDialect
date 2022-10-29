# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 11:11:01 2022

@author: fuxin
"""

import csv
import re
from num2hanzi import to_chinese,to_series

def Sentence2Chinese(instr):
    rtstr = instr
    numlist = re.findall(r'\d+', rtstr)
    cnt =0
    for num in numlist:
        index = rtstr.find(num,cnt)
        numstr = (rtstr[index:index+len(num)+1])
        cnt = index+1
    #最后是年，句号，分开读
    #这里加入转换判断
    #如果数字后面是年，则转换为数字
    #如果是电话号码，则转换为单一数字
    #如果是别的，则转换为中文数字
        if numstr[-1]=="年" or numstr[-1]=="。" :
            newstr = to_series(int(numstr[:-1]))
            newstr = newstr+numstr[-1]
            rtstr = rtstr.replace(numstr,newstr,1)
        else:
            newstr = to_chinese(int(numstr[:-1]))
            newstr = newstr+numstr[-1]
            #print(newstr,numstr[-1])
            rtstr = rtstr.replace(numstr,newstr,1)
    return rtstr

def Csv_To_Chinese(oldfile,newfile):
    import codecs
    f = csv.reader(open(oldfile,'r'))
    f1 = codecs.open(newfile,'w','utf-8')
    writer = csv.writer(f1)
    for i in f:
        if(i[2].strip()==''):
            tmpstr = i[1]
        else:
            tmpstr = i[2]
            
        if(re.search(r'\d', tmpstr)):
            out = Sentence2Chinese(tmpstr)
        else:
            out = tmpstr
        row = i[0],i[1],out,i[3]   
        writer.writerow(row)
    f1.close()

if __name__ == '__main__':
    Csv_To_Chinese('all.csv','all_chinese.csv')