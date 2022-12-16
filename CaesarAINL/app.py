from flask import Flask,request
from flask_cors import cross_origin
import os
from caesarinfer import CaesarNL
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
        
        print("Caesar Processing...")
        caesarResponse,intents = CaesarNL.run([user_input_json["caesarapi"]])
        print("Caesar Processed.")
        print(caesarResponse,"intent:",intents)

        return {"caesarmessage":{"caesarResponse":caesarResponse,"intent":intents}}

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000)) # 80
    app.run(debug=True,host="0.0.0.0",port=port) # 