# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 15:39:47 2022

@author: shinefool
"""

ffmpeg -i input.wav -af silenceremove=stop_periods=-1:stop_duration=0.3:stop_threshold=-30dB output.wav