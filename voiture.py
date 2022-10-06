from email.mime import image
import matplotlib.pyplot as plt 
from PIL import Image
def im():
    im= Image.open('voiture.png')
    im.show()