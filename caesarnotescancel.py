import os
import sys
if "CaesarStore" in os.listdir():
    if "caesarstorelast.txt" in os.listdir("CaesarStore"):
        with open("CaesarStore/caesarstorelast.txt","r") as f:
            data = f.readlines()
        try:
            wavfilename = "{}.wav".format(data[-1].replace("\n",""))

            #print(wavfilename)
            if wavfilename in os.listdir("CaesarAudioWAVs"): 
                os.remove("CaesarAudioWAVs/{}".format(wavfilename))
                with open("CaesarStore/caesarstorelast.txt", "w+") as f:                   
                    data.pop(-1)
                    try:
                        f.write(data)
                    except TypeError as tex:
                        pass
        except IndexError as iex:
            pass
                
