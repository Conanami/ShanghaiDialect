# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 17:06:15 2022

@author: fuxin
"""
#两个字典都做成单个字，然后比较一下
chf = open('c:/shanghai/dict/ch.dict','r',encoding='utf-8')
shf = open('c:/shanghai/dict/shh.dic','r')
chChar = open('c:/Shanghai/dict/chChar.dict','w',encoding='utf-8')
shChar = open('c:/Shanghai/dict/shChar.dict','w',encoding='utf-8')
illegal = ['\t','\n',' ','\r']
chWordList = chf.readlines()
shWordList = shf.readlines()
allWord = []
allShWord = []
for chWord in chWordList:
    tmpword = chWord.split(" ")[:-1][0].strip()
    allWord.append(tmpword)
    if len(tmpword)==1:
        chChar.write(chWord)
cnt = 0
cnt1 = 0 
for shWord in shWordList:
    for shc in shWord:
        if not shc in allShWord and shc not in illegal :
            allShWord.append(shc)
            shChar.write(shc+'\n')
    
    tmpword = shWord.split(" ")[:-1][0].strip()
    
    if tmpword in allWord:
        #print(tmpword)
        cnt1 = cnt1+1
    else:
        no = False
        for c in tmpword:
            if not c in allWord:
                no = True
                print(tmpword)
                break
        if no==False:
            #print(tmpword)
            cnt1 = cnt1+1
                
    cnt = cnt +1
    
shChar.close()
chChar.close()
chf.close()
shf.close()

print(cnt1,cnt)