#import library
import warnings
#from gtts import gTTS
import os
#from playsound import playsound
from caesarapis import CaesarAPIs
import time
import pyttsx3
warnings.filterwarnings("ignore")
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import speech_recognition as sr
from caesarinfer import CaesarNL
# Initialize recognizer class (for recognizing the speech)
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def speak(text,whisper_mode=None):
    if whisper_mode == 0:
        engine.say(text)
        engine.runAndWait()
recognizer = sr.Recognizer()

#def caesartalk(caesarspeech,whisper_mode,filename="example.mp3"):
#    if whisper_mode == 0:
#        audio = gTTS(caesarspeech, lang="en", slow=False)
#       audio.save(filename)
#        playsound(filename)
#        time.sleep(1)
#        if filename in os.listdir():
#            os.remove(filename)
# Reading Microphone as source
# listening the speech and store in audio_text variable
whisper_state = 1
caesarapis = CaesarAPIs()
while True:
    with sr.Microphone() as source:
        
        caesarintro ="How can I help you sir?" 
        print(caesarintro)
        #caesartalk(caesarintro,caesarapis.whisper_mode,filename="caesarintro.mp3")
        speak(caesarintro,caesarapis.whisper_mode)
        #recognizer
        recognizer.adjust_for_ambient_noise(source,duration=1)
        audio_text = recognizer.listen(source)
        understood = "Understood sir, processing..."
        print(understood)
        #caesartalk(understood,caesarapis.whisper_mode,filename="caesar_understood.mp3")
        speak(understood,caesarapis.whisper_mode)
        try:
            # using google speech recognition
            text = recognizer.recognize_google(audio_text)
            print(text)
            print("Caesar processing...")
            caesarResponse,intent = CaesarNL.run([text])
            caesarapis.runapis(caesarResponse,intent,text)
            
            print(f"User Input: {text}")
            print(f"Caesar: {caesarResponse}")
            #caesartalk(caesarResponse,caesarapis.whisper_mode,filename="caesarResponse.mp3")
            speak(caesarResponse,caesarapis.whisper_mode)

        except Exception as ex:
            print(type(ex),ex)
            print("Sorry, I did not get that")

            # whisper_mode
         