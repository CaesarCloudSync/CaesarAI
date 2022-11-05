#import library
import warnings
from gtts import gTTS
import os
from playsound import playsound
import time
warnings.filterwarnings("ignore")
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import speech_recognition as sr
# Initialize recognizer class (for recognizing the speech)
recognizer = sr.Recognizer()
def caesartalk(caesarspeech,filename="example.mp3"):
    audio = gTTS(caesarspeech, lang="en", slow=False)
    audio.save(filename)
    playsound(filename)
    time.sleep(1)
    if filename in os.listdir():
        os.remove(filename)
# Reading Microphone as source
# listening the speech and store in audio_text variable
with sr.Microphone() as source:
    caesarintro ="How can I help you sir?" 
    print(caesarintro)
    caesartalk(caesarintro,filename="caesarintro.mp3")
    audio_text = recognizer.listen(source)
    print("Understood sir, processing.")
    try:
        # using google speech recognition
        text = recognizer.recognize_google(audio_text)
        print("Caesar processing...")
        from caesarinfer import CaesarNL
        caesarResponse = CaesarNL.run([text])
        print(f"User Input: {text}")
        print(f"Caesar: {caesarResponse}")
        caesartalk(caesarResponse,filename="caesarResponse.mp3")

    except Exception as ex:
        print(type(ex),ex)
        print("Sorry, I did not get that")
         