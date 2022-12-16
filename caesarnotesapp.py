from caesarnotes import CaesarNotes
from flask import Flask,request
from flask_cors import cross_origin
import os

app = Flask(__name__)

@app.route("/",methods=["GET"])
@cross_origin()
def caesarhome():
    return "Caeser: How can I help you sir?"

@app.route("/caesarapi",methods=["POST","GET"])
@cross_origin()
def caesarapi():
    if request.method == "GET":
        return "Caeser: Hello sir, this is the CaesarAIAPI"
    elif request.method == "POST":
        user_input_json = request.get_json()
        #<filename> <duration_seconds> <subject> <translate>
        try:
            user_input_json["filename"]
            user_input_json["duration_seconds"]
            user_input_json["subject"]
            user_input_json["translate"]
        except KeyError as kex:
            return {"message":"runcaesar <filename> <duration_seconds> <subject> <translate>"}
        print("Caesar Processing...")
        noteargfilename,record_time,subject,translate = "caesarnotesapp",130,"ainotes","translate"
        try:
            CaesarNotes.run_app_record(noteargfilename,record_time,subject,translate)
            #return {"caesarmessage":{"caesarResponse":caesarResponse,"intent":intents}}
        except KeyboardInterrupt as kex:
            with open(f"CaesarNotes/{subject}/{noteargfilename}.txt") as f:
                data =f.read()
            pass
            

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000)) # 80
    app.run(debug=True,host="0.0.0.0",port=port) # 