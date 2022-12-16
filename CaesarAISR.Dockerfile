FROM alpine/alpine:latest

#VOLUME CaesarAINL CaesarAINL
WORKDIR /CaesarAISR

ADD CaesarAISR /CaesarAISR

RUN pip install -r requirements_caesarnotes.txt
#RUN pip install flask flask_cors tensorflow_hub tensorflow_text scikit-learn tqdm matplotlib gunicorn
