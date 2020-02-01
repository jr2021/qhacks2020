import numpy as np
from keras.models import load_model


model = load_model('models/model.h5')
labels = {
    0:'cardboard',
    1:'glass',
    2:'metal',
    3:'paper',
    4:'plastic',
    5:'trash'
}

def predict(image):
    """
    :param image: matrix representing a 300x300x3 image
    :return: output prediction for input sample
    """
    return model.predict(np.expand_dims(image, axis=0))
