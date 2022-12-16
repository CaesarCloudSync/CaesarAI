#import library
import os
import time
import warnings
from caesarapis import CaesarAPIs
import speech_recognition as sr
warnings.filterwarnings("ignore")



#os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
# Initialize recognizer class (for recognizing the speech)


def speak(text,whisper_mode=0):
    if whisper_mode == 0:
        #espeak.synth(text)
        if "output.mp3" in os.listdir():
            os.remove("output.mp3")
        os.system(f'espeak "{text}" --stdout | ffmpeg -i pipe:0 output.mp3')        
        os.system(f'mplayer -volume 300 output.mp3')   
        os.system("pkill mplayer")     
        #raise KeyboardInterrupt
       #os.system(f'mplayer -af volume=30:1 output.mp3')
       
recognizer = sr.Recognizer()
# Reading Microphone as source
# listening the speech and store in audio_text variable
whisper_state = 1
caesarapis = CaesarAPIs()
while True:
    
        try:
            caesarintro ="How can I help you sir?" 
            print(caesarintro)
            #caesartalk(caesarintro,caesarapis.whisper_mode,filename="caesarintro.mp3")
            speak(caesarintro,caesarapis.whisper_mode)
            print("Listening...")

            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source,duration=1)
                audio_text = recognizer.listen(source)

            #print("Billyy")
            #recognizer
            understood = "Understood sir, processing..."
            print(understood)
            #caesartalk(understood,caesarapis.whisper_mode,filename="caesar_understood.mp3")
            speak(understood,caesarapis.whisper_mode)
            # using google speech recognition
            text = recognizer.recognize_google(audio_text)
            print("output:",text)
            print("Caesar processing...")
            # TODO Send to Azure API
            if "hello" in text:
                print("Hola Amari")
                break
                #caesarResponse,intent = ("Hola Amari","greeting") 
                #caesarapis.runapis(caesarResponse,intent,text,speak)

                #print(f"User Input: {text}")
                #print(f"Caesar: {caesarResponse}")
                #caesartalk(caesarResponse,caesarapis.whisper_mode,filename="caesarResponse.mp3")
                #speak(caesarResponse,caesarapis.whisper_mode)
        except Exception as uex:
            continue


            # whisper_mode
         
