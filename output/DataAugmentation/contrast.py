
import cv2
import numpy as np

img = cv2.imread('filterImg5.jpg')
Y = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)[:,:,0]

# compute min and max of Y
min = np.min(Y)
max = np.max(Y)

# compute contrast
contrast = (max-min)/(max+min)
print(contrast)