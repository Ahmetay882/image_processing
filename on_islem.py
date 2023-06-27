import cv2
import matplotlib.pyplot as plt

# Görüntü Boyutlandırma
def boyutlandirma(img, x, y):
    return cv2.resize(img, (x,y))