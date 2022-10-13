from distutils import core
from email.mime import image
import matplotlib.pyplot as plt 
import cv2
import numpy as np
from PIL import Image
def im():
    im= Image.open('voiture.png')
    largeur_image=600
    hauteur_image=400
    im.show()
def rotate(im, alpha):
    image = im.rotate(70)
    image = cv2.imread("voiture.jpg")
    image_norm = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    print(type(image))
    cv2.imshow('original Image', image)
    cv2.imshow('Rotated Image', image_norm)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
im()
rotate()