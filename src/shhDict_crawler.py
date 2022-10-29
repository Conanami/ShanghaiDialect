# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 13:25:07 2022

@author: fuxin
"""
import urllib.request
import re 
from bs4 import BeautifulSoup
from distutils.filelist import findall
import shhList
import shhDialog

def GetAll():
    url = 'https://shh.dict.cn/'
    page = urllib.request.urlopen(url)   
    contents = page.read()   
    #获得了整个网页的内容也就是源代码  
    soup = BeautifulSoup(contents,"html.parser")
    print("海词上海话" + "\n" +" 上海话      普通话      类别     mp3 ")
     
    #a=soup.find_all('div',class_=('obox-c fydl fc80'))
    a=soup.find_all('li')
    for li in a:
        tmpurl = li.find('a').attrs['href']
        if(tmpurl.find('list')>=0):
            oneUrl = url+tmpurl[1:]
            title = tmpurl[6:]
            print(oneUrl)
            shhList.getList(oneUrl,title,'0304.csv')

def GetAllDialog():
    url = 'https://shh.dict.cn/dialog'
    dialogList = shhDialog.getDialogList(url)
    csvfile = 'dialog01.csv'    
    for dialog in dialogList:
        print(dialog,"Running...")
        shhDialog.getDialog(url, dialog, csvfile)
#print(a)
GetAll()