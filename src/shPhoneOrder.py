# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 13:46:07 2022

@author: fuxin
"""



#对shCharPhone.dict进行排序
f_shChar = open('c:/Shanghai/dict/shCharPhone.dict','r',encoding='utf-8')

f_out = open('c:/Shanghai/dict/shCharSorted.dict','w',encoding='utf-8')

tmpline = f_shChar.readlines()
tmpdict = {}
for line in tmpline:
    try:
        word = line.split(" ")[:-1][0].strip()
        phone = line[len(word):].strip()
        tmpdict[word]=phone
    except:
        print("不能分解",line)
f_shChar.close()

#print(tmpdict)
a = sorted(tmpdict.items(), key=lambda x: x[1], reverse=False)
print(a)
for line in a:
    tmpstr = line[0]+" "+line[1]+'\n'
    f_out.write(tmpstr)
f_out.close()
