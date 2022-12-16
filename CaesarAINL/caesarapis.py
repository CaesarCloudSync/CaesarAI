import os
import pyttsx3
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(text,whisper_mode=None):
    if whisper_mode == 0:
        engine.say(text)
        engine.runAndWait()

class CaesarAPIs:
    def __init__(self) -> None:
        self.whisper_mode = 0
    def runapis(self,caesarResponse=None,intent=None,userinput=None):
        if intent == "whisper_mode" and "on" in userinput:
            self.whisper_mode = 1
            speak("I will be quiet now sir",0)
        elif intent == "whisper_mode" and "off" in userinput:
            self.whisper_mode = 0
            speak("Can you hear me now sir",0)
        #elif 
        



