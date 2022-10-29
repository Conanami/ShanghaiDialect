# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 11:29:24 2022

@author: shinefool
"""

from pydub import AudioSegment
import os
import shutil
import time
 
AudioSegment.converter = "c:\\ffmpeg\\bin\\ffmpeg.exe" 
now_dir = os.getcwd()   #获取当前文件夹
new_dir = now_dir + '\\test\\'  #wav语音文件所在文件夹
#字从小到大
 
# wav 格式语音文件合成
def voice_unit():
    n=0    
    #list_voice_dir_length = len(list_voice_dir)
    playlist = AudioSegment.empty()
    second_5_silence = AudioSegment.silent(duration=5000)  #产生一个持续时间为5s的无声AudioSegment对象
    #sound = AudioSegment.from_wav(list_voice_dir[n])
    sound1 = AudioSegment.from_file(new_dir+'nnongsil.wav',format="wav") 
    sound2 = AudioSegment.from_file(new_dir+'hao2sil.wav',format="wav")
    sound3 = AudioSegment.from_file(new_dir+'yaasil.wav',format="wav")
    #  wav 
    playlist = sound1+sound2+sound3
        #sound = AudioSegment.from_file(new_dir+list_voice_dir[n],sample_width=2,frame_rate=16000,channels=1)  #raw pcm
    
    playlist.export(new_dir+'playlist.wav',format="wav") #wav
    #playlist.export(new_dir+'playlist.pcm')   #pcm
    print("语音合成完成，合成文件放在：",new_dir,"目录下")      
#对比文件顺序       

 
def main():
    try:
        os.remove(new_dir+'playlist.pcm')
    except:
        print("")
    #testlist()
    voice_unit()
if __name__ == "__main__":
    main()
