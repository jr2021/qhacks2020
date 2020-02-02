from keras.models import load_model
from model import predict
from time import sleep
import cv2 as opencv
import numpy
import os

model = load_model('models/model.h5')
labels = {0:'cardboard', 1:'glass', 2:'metal', 3:'paper', 4:'plastic', 5:'trash'}

def direct(prediction):
    os.system('arduino-cli compile --fqbn arduino:avr:mega ' + prediction)
    os.system('arduino-cli upload -p /dev/ttyACM0 --fqbn arduino:avr:mega ' + prediction)
    sleep(3)

def predict(image):
    return model.predict(numpy.expand_dims(image,axis=0))

def capture():
    camera = opencv.VideoCapture(0)
    _, image = camera.read()
    image = opencv.resize(image, (300, 300))
    camera.release()
    return image

def loop():
    try:
        while True:
            sleep(3)
            image = capture()
            prediction = predict(image)
            direct(prediction)
    except KeyboardInterrupt:
        return

def main():
    loop()
main()
