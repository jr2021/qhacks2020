from fastai.vision import *
from time import sleep
import cv2 as opencv
import numpy
import os

learner = load_learner('models/')


def predict(image):
    img = open_image('image.jpg')
    print(learner.predict(img))
    return learner.predict(img) #FIXME

def direct(prediction):
    os.system('arduino-cli compile --fqbn arduino:avr:mega /home/e7poon/jake/qhacks2020/sketches/' + prediction)
    os.system('arduino-cli upload -p /dev/ttyACM0 --fqbn arduino:avr:mega /home/e7poon/jake/qhacks2020/sketches/' + prediction)

def capture():
    camera = opencv.VideoCapture(0)
    _, image = camera.read()
    image = opencv.cvtColor(image, opencv.COLOR_BGR2RGB)
    opencv.imwrite("image.jpg", image)

    plt.imshow(image)
    plt.show()
    print('photo taken')

    return image

def loop():
    try:
        while True:
            sleep(3)
            preds = predict(capture())
            direct('blink')
            sleep(3)
    except KeyboardInterrupt:
        return

def main():
    loop()
main()
