import cv2 as cv
from time import sleep
from model.py import predict

def move():
    print("move")

def direct():
    print("direct")

def classify():
    print("classify")

def capture():
    camera = cv.VideoCapture(0)
    _, X = camera.read()
    X = cv.resize(X, (300, 300))
    camera.release()
    return X

def loop():
    try:
        while True:
            sleep(3)
            predict(capture())
    except KeyboardInterrupt:
        return

def main():
    loop()
main()
