# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 11:14:26 2022

@author: fuxin
"""

import moviepy.editor as mp
my_clip = mp.VideoFileClip(r'1.mp4')
#my_clip.audio.write_audiofile(r'7.wav',16000,2)
my_clip.audio.write_audiofile(r'8.wav')