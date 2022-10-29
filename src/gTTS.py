# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 16:18:04 2022

@author: fuxin
"""
import tempfile 
from gtts import gTTS
from pygame import mixer
mixer.init()

def speak(sentence):
    with tempfile.NamedTemporaryFile(delete=True) as fp:
        tts = gTTS(text =sentence,lang='zh-CN')
        tts.save("{}.mp3".format(fp.name))
        mixer.music.load("{}.mp3".format(fp.name))
        mixer.music.play()

speak('努力做个对社会有用的人')