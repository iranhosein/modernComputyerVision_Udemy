import cv2
import numpy as np
from matplotlib import pyplot as plt

def imshow(title="Image", image=None, size=6):
    w, h = image.shape[0], image.shape[1]
    aspect_ratio = w/h
    plt.figure(figsize=(size * aspect_ratio, size))
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.show()

image = cv2.imread('D:/very test/learnCV/source/modernComputyerVision_Udemy/images/kitten.jpg')
height, width = image.shape[:2]

Tx, Ty = height/4, width/4
T = np.float32([[1, 0, Tx], [0, 1, Ty]])

img_translation = cv2.warpAffine(image, T, (width, height))
cv2.imshow("Translated", img_translation)
cv2.waitKey(0)