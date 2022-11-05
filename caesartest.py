from audioop import reverse
import datetime
import speech_recognition as sr
import sys
import os
import json
# importing libraries 
import speech_recognition as sr 
import os 
from pydub import AudioSegment
import shutil
from pydub.silence import split_on_silence

filename = r"D:\Notion Speech Recognition\audio-chunks1\chunk1.wav"
# initialize the recognizer
r = sr.Recognizer()
# open the file
with sr.AudioFile(filename) as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source=source,duration=5)
    # recognize (convert from speech to text)
    text = r.recognize_google(audio_data)
    print(text)