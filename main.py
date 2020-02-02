from fastai.vision import *
from time import sleep
import cv2 as opencv
import numpy
import os

learner = load_learner('models/')

labels = {
    'cardboard':1,
    'paper':1,
    'metal':2,
    'glass':2,
    'plastic':3
}

def predict():
    img = open_image('image.jpg')
    print(learner.predict(img))

    return labels[str(learner.predict(img)[0])]

def direct(prediction):
    os.system('arduino-cli compile --fqbn arduino:avr:mega /home/e7poon/jake/qhacks2020/sketches/' + prediction)
    os.system('arduino-cli upload -p /dev/ttyACM0 --fqbn arduino:avr:mega /home/e7poon/jake/qhacks2020/sketches/' + prediction)

def capture():
    camera = opencv.VideoCapture(0)
    _, image = camera.read()
    image = opencv.cvtColor(image, opencv.COLOR_BGR2RGB)
    opencv.imwrite("image.jpg", image)

    print('photo taken')

    return image

def loop():
    capture()
    prediction = str(predict())
    direct(prediction)

def main():
    loop()

main()
