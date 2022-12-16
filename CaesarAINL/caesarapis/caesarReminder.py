import os
import json
import time
import requests
from datetime import datetime, timedelta
class CaesarReminder:
    @staticmethod
    def reminder():
        if "CaesarReminders" in os.listdir():
            if "caesarreminders.json" in os.listdir("CaesarReminders"):
                with open("CaesarReminders/caesarreminders.json","r") as f:
                    reminders = json.load(f)
                message = ""    
                for reminder in reminders["reminders"]:
                    message += "{}".format(reminder['subject'])
                    message += "<br>"
                    message += "{}".format(reminder['message'])
                    message += "<br>"
                    message += "Reminder: {}\n".format(datetime.fromisoformat(reminder['timestep']).strftime('%m/%d/%Y, %H:%M:%S'))
                    message += "<br>"
                    message += "<br>"
                sendjson = {"raspsendemail":{"email":reminders["email"],"message":message,"subject":"Caesar Reminders"}}
                response = requests.post("https://revisionbank-email.onrender.com/raspsendemail",json=sendjson)
                print(response.text)


            elif "caesarreminders.json" not in os.listdir("CaesarReminders"):
                sendjson = {"raspsendemail":{"email":"amari.lawal@gmail.com","message":"No Reminders Scheduled","subject":"Caesar Reminders"}}
                response = requests.post("https://revisionbank-email.onrender.com/raspsendemail",json=sendjson)
                print(response.text)
                


            # send email saying reminder
        elif "CaesarReminders" not in os.listdir():
            sendjson = {"raspsendemail":{"email":"amari.lawal@gmail.com","message":"No Reminders Scheduled","subject":"Caesar Reminders"}}
            response = requests.post("https://revisionbank-email.onrender.com/raspsendemail",json=sendjson)
            print(response.text)
            # Send email saying No reminders




if __name__ == "__main__":
    constant = 60 *60 
    duration = 48 * constant # hours
    
    #print(datetime.now().isoformat())
    while True:
        CaesarReminder.reminder()
        time.sleep(duration)
    #pass