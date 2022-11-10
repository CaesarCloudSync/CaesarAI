from flask import Flask,request
from flask_cors import cross_origin
from caesarinfer import CaesarNL
import tensorflow as tf
#app = Flask(__name__)


#@app.route("/",methods=["GET"])
#@cross_origin()
#def caesarhome():
#    return "Caeser: How can I help you sir?"

#@app.route("/caesarapi",methods=["POST","GET"])
#@cross_origin()
#def caesarapi():
#    if request.method == "GET":
#        return "Caeser: Hello sir, this is the CaesarAIAPI"
#    elif request.method == "POST":
#       user_input_json = request.get_json()
#        caesarResponse,intents = CaesarNL.run([user_input_json["caesarapi"]])
#       return {"caesarmessage":{"caesarResponse":caesarResponse,"intent":intents}}

if __name__ == "__main__":
    print(tf.__version__)
    
    #app.run(debug=True,host="0.0.0.0",port=5000) # 
