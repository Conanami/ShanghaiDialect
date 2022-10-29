# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 11:29:52 2022

@author: fuxin
"""

import wave
 
wavFile = r"now1.wav"
f = wave.open(wavFile)
# 音频头 参数
params = f.getparams()
Channels = f.getnchannels()
SampleRate = f.getframerate()
bit_type = f.getsampwidth() * 8
frames = f.getnframes()
Duration = frames / float(SampleRate) # 单位为s
 
print("音频头参数：", params)
print("通道数(Channels)：", Channels)
print("采样率(SampleRate)：", SampleRate)
print("比特(SampleWidth)：", bit_type)
print("采样点数(frames)：", frames)
print("总时长(Duration)：", Duration)
f.close()