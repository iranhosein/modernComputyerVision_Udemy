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

image = np.zeros((512, 512, 3), np.uint8)

# Define 4 points
pts = np.array([[10, 50], [400, 50], [90, 200], [50, 500]], np.int32)

# Reshape 4 points
pts = pts.reshape((-1, 1, 2))

cv2.polylines(image, [pts], True, (0, 0, 255), 3)
imshow("Image", image)





