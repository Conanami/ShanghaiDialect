# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 14:28:08 2022

@author: fuxin
"""

from pydub import AudioSegment

from pydub.utils import make_chunks

myaudio = AudioSegment.from_file("7.wav" , "wav")

chunk_length_ms =60000 # 分块的毫秒数

chunks = make_chunks(myaudio, chunk_length_ms) #将文件切割成1秒每块

#保存切割的音频到文件

for i, chunk in enumerate(chunks):
    chunk_name = "chunk{0}.wav".format(i)
    print("exporting", chunk_name)
    chunk.export(chunk_name, format="wav")