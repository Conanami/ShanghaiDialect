# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 15:01:26 2022

@author: fuxin
"""

import os

from pydub import AudioSegment
import os
import shutil
import time
import csv

import jieba
import re,string

def jiebaCut(instr):
    jieba.load_userdict("C:\\Shanghai\\dict\\fuxin.dict")
    punc = '~`!#$%^&*()_+-=|\';":/.,?><~·！@#￥%……&*（）——+-=“：’；、。，？》《{}'
    tmpstr = re.sub(r"[%s]+" %punc, "",instr)
    seg_list = jieba.cut(tmpstr)
    newlist = " ".join(seg_list)
    return newlist

def all_path(dirname,filterlist):

    result = []#所有的文件

    for maindir, subdir, file_name_list in os.walk(dirname):

        for filename in file_name_list:
            apath = os.path.join(maindir, filename)#合并成一个完整路径
            ext = os.path.splitext(apath)[1]  # 获取文件后缀 [0]获取的是除了文件名以外的内容

            if ext in filterlist:
                result.append(apath)

    return result

def loadWaves(path,filterlist=[".wav"]):
    result = {}
    filenames=all_path(path,filterlist)
    for filename in filenames:
        filename=str(filename)
        temp=filename.split('.')
        temp2 = temp[0].split("\\")
        #print(temp2[-1][:-4])
        result[temp2[-1][:-4]]=filename
    #print(result)
    return result

def loadDict(dictpath):
    f_in = open(dictpath,'r',encoding='utf-8')
    shChar_dict = {}
    for line in f_in.readlines():
        try:
            word = line.split(" ")[:-1][0].strip()
            phone = line[len(word):].strip()
            shChar_dict[word]=phone.replace(' ','')
        except:
            continue
    return shChar_dict

def makeWaveByWord(myText,wavdict,shhdict,outputfile):
    playlist = AudioSegment.empty()
    new_dir = "C:\\Shanghai\\dict\\test_output\\"
    #playlist.export(new_dir+'playlist.wav',format="wav")
    biaodian=[',','。','？','，','?','！','…','-','“','”','《','》','、','.',':','：','x','!','；',' ']
    
    readStr = myText
    for i in range(len(readStr)):
        print(i,len(readStr),readStr[i])
        if readStr[i] in biaodian:
            sound = AudioSegment.silent(duration=100)
        else:
            wavekey = shhdict[readStr[i]]
            if i==len(readStr)-1:
                #结尾字，浊变清
                if readStr[i-1] not in biaodian:
                    if wavekey[0]==wavekey[1]:
                        wavekey=wavekey[1:]+"2"
                    if wavekey[-1]!='2': #结尾字，一声变二声
                        wavekey = wavekey
                wavfile = wavdict[wavekey]
                sound = AudioSegment.from_file(wavfile,format="wav")   
                sound =sound [:int(len(sound)*0.8)] 
            else:
                if readStr[i+1] in biaodian:
                    #结尾字，浊变清
                    if i>0 and readStr[i-1] not in biaodian:
                        if wavekey[0]==wavekey[1]:
                            wavekey=wavekey[1:]+"2"
                        if wavekey[-1]!='2': #结尾字，一声变二声
                            wavekey = wavekey 
                    wavfile = wavdict[wavekey]
                    sound = AudioSegment.from_file(wavfile,format="wav")
                    sound = sound[:int(len(sound)*0.6)] 
                else:
                    wavfile = wavdict[wavekey]
                    sound = AudioSegment.from_file(wavfile,format="wav")
                    sound = sound[:int(len(sound)*0.8)]
        playlist = playlist + sound
    
    playlist.export(new_dir+outputfile,format="wav")
    print("语音合成完成，合成文件放在：",new_dir,"目录下")      


def getSentence(csvpath):
    result = []
    with open(csvpath,encoding='utf-8') as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            result.append(row)
    return result



def main():
    wavpath = "C:\Shanghai\dict\TTS\short_wav"
    wavDict = loadWaves(wavpath)
    dictPath = "C:\Shanghai\dict\shCharSorted.dict"
    shhDict = loadDict(dictPath)
    myText = "你直播才是搞橙子，肯定更加欢喜看你"
    afterCut = jiebaCut(myText)
    print(afterCut)
    makeWaveByWord(afterCut,wavDict,shhDict,'test005.wav')
    
    
    
    
if __name__ == "__main__":
    main()