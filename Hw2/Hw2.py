import numpy as np
import cv2
import random

img = cv2.imread('Donger.jpg')
Z = img.reshape((-1,3))

# convert to np.float32
Z = np.float32(Z)

# define criteria, number of clusters(K) and apply kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 4
ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

# Now convert back into uint8, and make original image
center = np.uint8(center)
count = 0
for i in center:
    a = random.randint(0,255)
    b = random.randint(0,255)
    c = random.randint(0,255)
    center[count] = [a,b,c]
    count += 1
    print('[{} {} {}]{}'.format(a,b,c,count))

res = center[label.flatten()]
res2 = res.reshape((img.shape))

cv2.imwrite('Donger1.jpg',res2)
