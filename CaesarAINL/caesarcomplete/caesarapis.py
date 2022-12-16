import os
class CaesarAPIs:
    def __init__(self) -> None:
        self.whisper_mode = 0
    def runapis(self,caesarResponse=None,intent=None,userinput=None,voiceengine=None):
        if intent == "whisper_mode" and "on" in userinput:
            self.whisper_mode = 1
            voiceengine.say("I will be quiet now sir")
            voiceengine.runAndWait()
        elif intent == "whisper_mode" and "off" in userinput:
            self.whisper_mode = 0
            voiceengine.say("Can you hear me now sir")
            voiceengine.runAndWait()
        



