import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline
from skimage.io import imread, imshow

image1 = imread('1.jpg')
imshow(image1);

image2 = imread('1.jpg', as_gray=True)
imshow(image2)

print(image1.shape)
print(image2.shape)

print(image1.size)
print(image2.size)

pixel_feat1 = np.reshape(image2, (50 * 50))
pixel_feat1

pixel_feat2 = np.reshape(image1, (50 * 50 * 3))
pixel_feat2