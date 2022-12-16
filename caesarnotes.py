import pyaudio
import wave
import sys
import os
import speech_recognition as sr
import requests
class CaesarNotes:
    @staticmethod
    def record(noteargfilename,record_time,subject,translate=None): 
        frames = []
        try:
            if "CaesarAudioWAVs" not in os.listdir():
                os.mkdir("CaesarAudioWAVs")
            subject = subject.capitalize()
            if  subject not in os.listdir("CaesarAudioWAVs"):
                os.mkdir(f"CaesarAudioWAVs/{subject}")
            filename = "CaesarAudioWAVs/{}/{}.wav".format(subject,noteargfilename) #"resonance_and_damping.wav"
            # set the chunk size of 1024 samples
            chunk = 1024
            # sample format
            FORMAT = pyaudio.paInt16
            # mono, change to 2 if you want stereo
            channels = 1
            # 44100 samples per second
            sample_rate = 44100
            record_seconds = record_time #5#900 seconds
            # initialize PyAudio object
            p = pyaudio.PyAudio()
            # open stream object as input & output
            stream = p.open(format=FORMAT,
                            channels=channels,
                            rate=sample_rate,
                            input=True,
                            output=True,
                            frames_per_buffer=chunk)

            print("Recording...")
            for i in range(int(sample_rate / chunk * record_seconds)):
                data = stream.read(chunk)
                # if you want to hear your voice while recording
                # stream.write(data)
                frames.append(data)
            print("Finished recording.")
            # stop and close stream
            stream.stop_stream()
            stream.close()
            # terminate pyaudio object
            p.terminate()
            # save audio file
            # open the file in 'write bytes' mode
            wf = wave.open(filename, "wb")
            # set the channels
            wf.setnchannels(channels)
            # set the sample format
            wf.setsampwidth(p.get_sample_size(FORMAT))
            # set the sample rate
            wf.setframerate(sample_rate)
            # write the frames as bytes
            wf.writeframes(b"".join(frames))
            # close the file
            wf.close()
        except KeyboardInterrupt as kex:
            #print(frames)
            stream.stop_stream()
            stream.close()
            # terminate pyaudio object
            p.terminate()
            # save audio file
            # open the file in 'write bytes' mode
            wf = wave.open(filename, "wb")
            # set the channels
            wf.setnchannels(channels)
            # set the sample format
            wf.setsampwidth(p.get_sample_size(FORMAT))
            # set the sample rate
            wf.setframerate(sample_rate)
            # write the frames as bytes
            wf.writeframes(b"".join(frames))
            # close the file
            wf.close()
            if translate == "translate":
                print("Translating...")
                r = sr.Recognizer()
                if "CaesarNotes" not in os.listdir():
                    os.mkdir("CaesarNotes")
                if subject not in os.listdir("CaesarNotes"):
                    os.mkdir(f"CaesarNotes/{subject}")
                txtfilename = "CaesarNotes/{}/{}.txt".format(subject,filename.replace(".wav","").replace("CaesarAudioWAVs/","").replace(f"{subject}",""))
                with sr.AudioFile(filename) as source:
                    # listen for the data (load audio to memory)
                    audio_data = r.record(source)
                    # recognize (convert from speech to text)
                    text = r.recognize_google(audio_data)
                    #print(text)
                    with open(txtfilename,"w+") as f:
                        f.write(text)
                    with open(txtfilename,"r") as f:
                        text = f.read()
                        textlist  = text.split("period")
                        #print(textlist)
                    sentences = ""
                    with open(txtfilename,"w+") as f:
                        for t in textlist:
                            sentence = f"{t.rstrip().lstrip()}.\n".capitalize()
                            print(sentence)
                            sentences += sentence
                            f.write(sentence)
                    sendrevisionbank = input("Send to RevisionBank: (y) or (n)").lower()
                    if sendrevisionbank == "y":
                        cardname = f'{txtfilename.split("/")[0]}/{txtfilename.split("/")[1].replace(".txt","").capitalize()}'
                        json = {"revisioncardscheduler":{"sendtoemail":"amari.lawal05@gmail.com","revisionscheduleinterval":60,"revisioncards":[{"subject":f"A-Level {cardname}","revisioncardtitle":cardname,"revisioncard":sentences}]}}
                        loginjson = {"email":"amari.lawal05@gmail.com","password":"kya63amari"}
                        try:
                            print("Logging in...")
                            access_token = requests.post("https://revisionbank.onrender.com/loginapi",json=loginjson).json()["access_token"]
                            headers = {"Authorization": f"Bearer {access_token}"}
                            print("Logged in.")
                        except Exception as ex:
                            print("Login Failed.{}:{}".format(type(ex),ex))

                        try:
                            print("Storing CaesarAI text...")
                            response = requests.post("https://revisionbank.onrender.com/storerevisioncards",json=json,headers=headers).json()
                            print("CaesarAI Stored.")
                        except Exception as ex:
                            print("CaesarAI Text not stored.".format(type(ex),ex))



                    elif sendrevisionbank == "n":
                        pass
                    else:
                        pass
                    
            elif translate == None:
                pass
            else:
                pass
    @staticmethod
    def run():
        # the file name output you want to record into
        if len(sys.argv) == 2:
            if sys.argv[1] == "help":
                print("CaesarAI Notes Help: runcaesar <filename> <duration_seconds> <subject> <translate>")
            
        if len(sys.argv) <= 1:
            print("Type in your text file name as an argument.")
        elif len(sys.argv) == 4:
            noteargfilename = sys.argv[1]
            # TODO Type in minutes
            record_time = int(sys.argv[2])* 60 #3600 # 60 record_time - seconds
            if sys.argv[3].lower() == "physics":
                subject = "physics"
                translate = None
                CaesarNotes.record(noteargfilename,record_time,subject,translate)
            elif sys.argv[3].lower() == "computer_science":
                subject = "computer_science"
                translate = None
                CaesarNotes.record(noteargfilename,record_time,subject,translate)
            elif sys.argv[3].lower() == "maths":
                subject = "maths"
                translate = None
                CaesarNotes.record(noteargfilename,record_time,subject,translate)
            elif sys.argv[3].lower() == "ainotes":
                subject = "ainotes"
                translate = None
                CaesarNotes.record(noteargfilename,record_time,subject,translate)
            else:
                print(f"'{sys.argv[3].capitalize()}' is not a correct directory name.")
            
            
        elif len(sys.argv) > 5:
            print("Not right amount of arguments. 4 arguments")
        elif len(sys.argv) == 5:
            noteargfilename = sys.argv[1]
            # TODO Type in minutes
            record_time = int(sys.argv[2])* 60 #3600 # 60 record_time - seconds
            subject = sys.argv[3]
            translate = sys.argv[4]
            CaesarNotes.record(noteargfilename,record_time,subject,translate)

if __name__ == "__main__":
    CaesarNotes.run()