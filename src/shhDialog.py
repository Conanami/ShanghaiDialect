# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 11:06:57 2022

@author: fuxin
"""
from urllib.parse import quote
import urllib.request
import re 
from bs4 import BeautifulSoup
from distutils.filelist import findall
import mp3Download

#url = "https://shh.dict.cn/list/礼貌用语"
import csv
import codecs
import os
import shhList

def getDialogList(url):
    rtlist = []
    listurl = url+"/1"
    page = urllib.request.urlopen(quote(listurl,safe='/:?='))   
    contents = page.read()   
#获得了整个网页的内容也就是源代码  
    soup = BeautifulSoup(contents,"html.parser")
    curPage, totalPage = shhList.getPage(soup)
    print(curPage,totalPage)
    for i in range(1,totalPage+1):
        pageurl = url+"/"+str(i)
        page = urllib.request.urlopen(quote(pageurl,safe='/:?='))
        contents = page.read()   
        #获得了整个网页的内容也就是源代码  
        soup = BeautifulSoup(contents,"html.parser")
        a = soup.find_all('h4')
        for b in a:
            c = b.find_all('a')
            for d in c:
               rtlist.append(d.string)
    return rtlist

def getDialog(url,title,csvfile):
    if(os.path.exists(csvfile)):
        f = codecs.open(csvfile,'a','gbk')
    else:
        f = codecs.open(csvfile,'w','gbk')
    writer = csv.writer(f)
    tmpurl = url+"/"+title
    #print(tmpurl)
    page = urllib.request.urlopen(quote(tmpurl,safe='/:?='))   
    contents = page.read()   
#获得了整个网页的内容也就是源代码  
    soup = BeautifulSoup(contents,"html.parser")
    a = soup.find('div',class_=('mbox-c'))
    b = a.find_all('li')
    for line in b:
        #print(line)
        shHua = line.find('em')
        putong = line.find('span')
        if(shHua!=None):
            shHua = shHua.get_text()
            putong = putong.get_text()
            mp3 = line.find('img').attrs['audio']
            mp3url = 'https://audio.dict.cn/mp3.php?q='+mp3
            save_url='c:/Shanghai/dialog_mp3'
            file_name = mp3+'.mp3'
            file_path = os.path.join(save_url, file_name)
            row = ''
            if not (os.path.exists(file_path)):
                mp3Download.DownloadFile(mp3url, save_url,file_name)
                row = (title,putong,shHua,mp3)
                print(row)
            if (row!=''):
                writer.writerow(row)
            print(shHua,putong,file_name)
    f.close()
    

#url = 'https://shh.dict.cn/dialog'
#print(getDialogList(url))
#getDialog(url)