FROM tensorflow/tensorflow:latest-gpu-jupyter

#VOLUME CaesarAINL CaesarAINL
WORKDIR /CaesarAINL 

ADD CaesarAINL /CaesarAINL 

RUN pip install flask flask_cors tensorflow_hub tensorflow_text scikit-learn tqdm matplotlib gunicorn

EXPOSE 5000 
#80

ENTRYPOINT [ "python" ]
CMD ["app.py"]
