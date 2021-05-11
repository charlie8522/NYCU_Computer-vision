import numpy as np
import cv2
from skimage import io

img = io.imread('license.jpg', pilmode='L')
threshold = 127
b = 1.0 * (img > threshold)
io.imsave('binarized.jpg', b)


b = np.uint8(b)
nb_components, labels, stats, centroids = cv2.connectedComponentsWithStats(b, connectivity=4)
#print(nb_components,stats)

count = 0
for i in range(len(stats)):
    if stats[i][4] > 1000 and stats[i][4]<10000:
        count += 1
print('Number count:{}'.format(count))
