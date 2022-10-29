# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 15:23:04 2022

@author: fuxin
"""

import speech_recognition as sr
audio_file = 'demo_audio.wav'
r=sr.Recognizer()
with sr.AudioFile(audio_file) as source:
    audio = r.record(source)
    
print('文本内容:',r.recognize_sphinx(audio,language='zh-CN'))