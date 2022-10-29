# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 14:46:38 2022

@author: fuxin
"""

from scipy.io import wavfile
import wave
import numpy as np
import matplotlib.pyplot as plt
from pydub import AudioSegment
import os
 #定义转化格式函数
def trans_mp3_to_wav(filepath,file_name,outpath):
    print(filepath)
    song = AudioSegment.from_mp3(filepath)
    song.export(outpath+"/"+file_name+".wav", format="wav",parameters=('-ar','16000'))
    

def wholeDir_mp3_to_wav(inpath,outpath=None):
    
    filter=[".mp3"] #设置过滤后的文件类型 当然可以设置多个类型
    for file_name in os.listdir(inpath):
        if not os.path.exists('c:/Shanghai/mp3/'+file_name):
            ext = os.path.splitext(file_name)[1]
            old_name = os.path.splitext(file_name)[0]
            if ext in filter:
                tmppath = inpath+'/'+file_name
                #print(old_name)
                trans_mp3_to_wav(tmppath, old_name,outpath)
            
            #result.append(apath)
            
    


#source_file_path = 's0t2z8S.mp3'
#trans_mp3_to_wav(source_file_path)
print(wholeDir_mp3_to_wav('c:/Shanghai/dialog_mp3','c:/Shanghai/wav'))