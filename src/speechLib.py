# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 11:18:21 2022

@author: fuxin
"""

from comtypes.client import CreateObject
from comtypes.gen import SpeechLib

engine = CreateObject("SAPI.SpVoice")
stream = CreateObject("SAPI.SpFileStream")
in_file = "demo.txt"
out_file = "demo_audio.wav"

stream.open(out_file,SpeechLib.SSFMCreateForWrite)
engine.AudioOutputStream = stream

f=open(in_file,'r',encoding = 'utf-8')
theText = f.read()
f.close()
engine.Speak(theText)
stream.close()
