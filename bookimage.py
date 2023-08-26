import cv2
import numpy as np
from matplotlib import pyplot as plt
from skimage.filters import threshold_local

def imshow(title="image", image=None, size=6):
    w, h = image.shape[0], image.shape[1]
    aspect_ratio = w/h
    plt.figure(figsize=(size * aspect_ratio, size))
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.show()

image = cv2.imread('D:/very test/learnCV/source/modernComputyerVision_Udemy/images/scan.jpg')
# imshow("orginal", image)

V = cv2.split(cv2.cvtColor(image, cv2.COLOR_BGR2HSV))[2]
T = threshold_local(V, 25, offset=15, method="gaussian")

thresh = (V>T).astype("uint8") * 255
imshow("threshold_local", thresh)
