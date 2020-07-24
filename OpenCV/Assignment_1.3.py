import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('tiger.jpg',0)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([]) 
plt.show()
flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
print flags 