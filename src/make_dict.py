# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 14:05:27 2022

@author: fuxin
"""

f_shChar = open('c:/Shanghai/dict/shCharPhone.dict','r',encoding='utf-8')

f_in = open('c:/Shanghai/dict/shh.dic','r',encoding='utf-8')
#模型用的dic文件，还必须是utf8的，还必须是dic结尾的
f_out = open('c:/Shanghai/dict/shh_new.dic','w',encoding='utf-8')

shChar_dict = {}
for line in f_shChar.readlines():
    try:
        word = line.split(" ")[:-1][0].strip()
        phone = line[len(word):].strip()
        shChar_dict[word]=phone
    except:
        continue

for line in f_in.readlines():
    #print(line)
    newline = line
    try:
        word = line.split(" ")[:-1][0].strip()
        newline = word
        for c in word:
            try:
                newline = newline +" "+shChar_dict[c]
            except:
                continue
    except:
        continue        
    f_out.write(newline+'\n')

f_shChar.close()
f_in.close()
f_out.close()