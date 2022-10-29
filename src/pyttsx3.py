# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 11:06:58 2022

@author: fuxin
"""

import pyttsx3 as pyttsx

engine = pyttsx.init()
engine.say("你好，pyttsx")
engine.runAndWait()