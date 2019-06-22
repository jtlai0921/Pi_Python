import fnmatch
import os
import cv2
import numpy as np
from opencv import config
from opencv import face

MEAN_FILE = 'mean.png'
POSITIVE_EIGENFACE_FILE = 'positive_eigenface.png'
NEGATIVE_EIGENFACE_FILE = 'negative_eigenface.png'

def walk_files(directory, match='*'):
    for root, dirs, files in os.walk(directory):
        for filename in fnmatch.filter(files, match):
            yield os.path.join(root, filename)

def prepare_image(filename):
    return face.resize(cv2.imread(filename, cv2.IMREAD_GRAYSCALE))

def normalize(X, low, high, dtype=None):
    X = np.asarray(X)
    minX, maxX = np.min(X), np.max(X)
    X = X - float(minX)
    X = X / float((maxX - minX))
    X = X * (high-low)
    X = X + low
    if dtype is None:
        return np.asarray(X)
    return np.asarray(X, dtype=dtype)

if __name__ == '__main__':
    print("Reading training images...")
    faces = []
    labels = []
    pos_count = 0
    neg_count = 0
    for filename in walk_files(config.POSITIVE_DIR, '*.pgm'):
        faces.append(prepare_image(filename))
        labels.append(config.POSITIVE_LABEL)
        pos_count += 1
    for filename in walk_files(config.NEGATIVE_DIR, '*.pgm'):
        faces.append(prepare_image(filename))
        labels.append(config.NEGATIVE_LABEL)
        neg_count += 1
    print('Read', pos_count, 'positive images and', neg_count, 'negative images.')
    print('Training model...')
    model = cv2.face.createEigenFaceRecognizer()
    model.train(np.asarray(faces), np.asarray(labels))
    model.save(config.TRAINING_FILE)
    print('Training data saved to', config.TRAINING_FILE)
    mean = model.getMean().reshape(faces[0].shape)
    cv2.imwrite(MEAN_FILE, normalize(mean, 0, 255, dtype=np.uint8))
    eigenvectors = model.getEigenVectors()
    pos_eigenvector = eigenvectors[:, 0].reshape(faces[0].shape)
    cv2.imwrite(POSITIVE_EIGENFACE_FILE, normalize(pos_eigenvector, 0, 255, dtype=np.uint8))
    neg_eigenvector = eigenvectors[:, 1].reshape(faces[0].shape)
    cv2.imwrite(NEGATIVE_EIGENFACE_FILE, normalize(neg_eigenvector, 0, 255, dtype=np.uint8))
