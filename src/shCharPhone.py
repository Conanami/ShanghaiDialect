# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 11:27:37 2022

@author: fuxin
"""

shChar = open('c:/Shanghai/dict/shChar.dict','r',encoding='utf-8')
chChar = open('c:/Shanghai/dict/chChar.dict','r',encoding='utf-8')
ch_dict = {};
f_shChar = open('c:/Shanghai/dict/shCharPhone.dict','w',encoding='utf-8')

shCharlist = shChar.readlines()
chCharlist = chChar.readlines()

for line in chCharlist:
    word = line.split(" ")[:-1][0].strip()
    phone = line[len(word):].strip()
    ch_dict[word]=phone
#print(ch_dict)
for line in shCharlist:
    try:
        phone = ch_dict[line.strip()]
        newline = line.strip()+" "+phone+"\n"
        f_shChar.write(newline)
    except:
        f_shChar.write(line)

shChar.close()
chChar.close()
f_shChar.close()
    