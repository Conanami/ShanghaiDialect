# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 14:46:13 2022

@author: fuxin
"""
#import sys
#import importlib

#importlib.reload(sys)
#sys.setdefaultencoding("utf-8")
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

def getPage(htmlsoup):
    a=htmlsoup.find('div',id=('pager'))
    curpage = int(a.find('font').string)
    for line in a:
        if(line.find('共')):
            tmptotal = str(line).strip()
            if(tmptotal!=''):
                totalpage = int(tmptotal[tmptotal.find('/')+1:-1])
    return curpage,totalpage


def getList(url,title,csvfile):
    if(os.path.exists(csvfile)):
        f = codecs.open(csvfile,'a','gbk')
    else:
        f = codecs.open(csvfile,'w','gbk')
    writer = csv.writer(f)
    page = urllib.request.urlopen(quote(url,safe='/:?='))   
    contents = page.read()   
#获得了整个网页的内容也就是源代码  
    soup = BeautifulSoup(contents,"html.parser")
    curpage , totalpage = getPage(soup)
    for i in range(1,totalpage+1):
        pageurl = url+"/"+str(i)
        page = urllib.request.urlopen(quote(pageurl,safe='/:?='))
        contents = page.read()   
        #获得了整个网页的内容也就是源代码  
        soup = BeautifulSoup(contents,"html.parser")
        a = soup.find('div',class_=('mbox-c'))
        b = a.find_all('li')
        for line in b:
            #print(line)
            putong = line.find('a').attrs['href'][1:]
            shHua = line.find('a').string
            mp3 = line.find('img').attrs['audio']
            mp3url = 'https://audio.dict.cn/mp3.php?q='+mp3
            save_url='c:/Shanghai/mp3'
            file_name = mp3+'.mp3'
            file_path = os.path.join(save_url, file_name)
            row = ''
            if not (os.path.exists(file_path)):
                mp3Download.DownloadFile(mp3url, save_url,file_name)
                row = (title,putong,shHua,mp3)
                print(row)
            if (row!=''):
                writer.writerow(row)
    f.close()
    
