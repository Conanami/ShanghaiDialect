# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 11:12:01 2022

@author: fuxin
"""

from win32com.client import Dispatch

speaker = Dispatch("SAPI.SpVoice")
speaker.Speak("努力做一个对社会有用的人")
del speaker