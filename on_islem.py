import cv2 as cv
import matplotlib.pyplot as plt

# görüntü boyutlandırma

def boyutlandirma(img,x,y):
    return cv.resize(img,(x,y))