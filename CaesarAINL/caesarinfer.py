import sys
import json
import spacy
import pickle
import random
import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_text as text
from sklearn.preprocessing import LabelBinarizer

    
# TODO AIM - Implement Chatbot Gossip to Caesar
# 1. Add data to datasets train | valid | test 
#     a. then clean labels
# 2. Augment data to provide more potential possibilites
# 3. Use BERT to match input with the response
# Command Labels - AddToPlaylist | GetWeather -> API -> user
# Conversation Labes - Greeting | Goodbye  -> BERTNN: input:"hello" => response:"hi there, I am caesar" -> user

# TODO AIM - Single names of songs artists like "play a boogie" and it will play a boogie's music.
# 1. Idea one - NER detect the named entities
# 2. Create new Neural Network that detects that. * Have to determine the relationship between the entites 


greetings = ["Greeting","smalltalk_greetings_hello"]
courtesy_greeting = ["CourtesyGreeting"]

class CaesarNL:
  @staticmethod
  def run(userinput):
    #if len(sys.argv) == 2:
    #userinput = [sys.argv[1].lower()]
    stored_name = "Amari"
    classifier_model = tf.keras.models.load_model('caesarmodel/caesarnl.h5',custom_objects={'KerasLayer':hub.KerasLayer})

    # Show the model architecture
    results = tf.nn.softmax(classifier_model(tf.constant(userinput)))
    with open("caesarmodel/labelbinarizer.pkl","rb") as f:
        binarizer = pickle.load(f)


    intents=binarizer.inverse_transform(results.numpy())
    with open("intentdata/responses.json","r") as f:
      responses = json.load(f)["responses"]

    if intents[0] in greetings:
      greetresponse = random.choice(responses["Greeting"]).replace("<HUMAN>",stored_name)
      #print(greetresponse)
      return greetresponse,intents[0]
    else:
      response = f"response to be implemented for text:{userinput}, predicted intent:{intents[0]}"
      #print(response)
      return response,intents[0]
    #elif len(sys.argv) < 2:
    #response = "What is it, sir?"
    #print(response)
    #return response
      

if __name__ == "__main__":
  userinput = ["Hello"]
  response,intents = CaesarNL.run(userinput)
  print(response,intents)



