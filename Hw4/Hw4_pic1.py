import numpy as np
import cv2

img = cv2.imread('pic1.jpg')
img = cv2.resize(img, (512, 512), interpolation=cv2.INTER_AREA)
constant = cv2.copyMakeBorder(img,0,0,400,400,cv2.BORDER_CONSTANT,value=(255,255,255))

blur_img = cv2.GaussianBlur(constant, (0, 0), 25)
usm = cv2.addWeighted(constant, 1.5, blur_img, -0.5, 0)

gray = cv2.cvtColor(usm, cv2.COLOR_RGB2GRAY)
res,gray2 =cv2.threshold(gray,120, 255, cv2.THRESH_TOZERO) 
edges = cv2.Canny(gray2,600,100)
lines = cv2.HoughLines(edges, 1, np.pi/120, 120, min_theta=np.pi/36, max_theta=np.pi-np.pi/36)

flag1 = 0
flag2 = 0
list1 = []
list2 = []
for line in lines:
    if flag1 == 2:break
    rho,theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))
    #cv2.line(constant,(x1,y1),(x2,y2),(0,255,0),1)
    list1.append([x1,y1])
    list1.append([x2,y2])
    flag1 += 1

for line in lines:
    if flag2 == 3:break
    rho,theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))
    if (y2-y1)/(x2-x1)<0 :
        #cv2.line(constant,(x1,y1),(x2,y2),(0,255,0),1) 
        list2.append([x1,y1])
        list2.append([x2,y2])
        flag2 += 1

x1 = list1[0][0]
y1 = list1[0][1]
x2 = list1[1][0]
y2 = list1[1][1]
x3 = list1[2][0]
y3 = list1[2][1]
x4 = list1[3][0]
y4 = list1[3][1]

X1 = list2[2][0]
Y1 = list2[2][1]
X2 = list2[3][0]
Y2 = list2[3][1]
X3 = list2[4][0]
Y3 = list2[4][1]
X4 = list2[5][0]
Y4 = list2[5][1]

x0 = ((x3-x4) * (x2*y1 - x1*y2) - (x1-x2) * (x4*y3 - x3*y4)) / ((x3-x4) * (y1-y2) - (x1-x2) * (y3-y4))
y0 = ((y3-y4) * (y2*x1 - y1*x2) - (y1-y2) * (y4*x3 - y3*x4)) / ((y3-y4) * (x1-x2) - (y1-y2) * (x3-x4))
X0 = ((X3-X4) * (X2*Y1 - X1*Y2) - (X1-X2) * (X4*Y3 - X3*Y4)) / ((X3-X4) * (Y1-Y2) - (X1-X2) * (Y3-Y4))
Y0 = ((Y3-Y4) * (Y2*X1 - Y1*X2) - (Y1-Y2) * (Y4*X3 - Y3*X4)) / ((Y3-Y4) * (X1-X2) - (Y1-Y2) * (X3-X4))
cv2.line(constant,(int(x0),int(y0)),(int(X0),int(Y0)),(0,127,0),1)
#print((int(x0),int(y0)),(int(X0),int(Y0)))

length = 180*(15517/15530)/(143/156)
print("%.1f" %length)
#cv2.imshow('1'edges)
#cv2.imshow('2',img)
#cv2.imshow('3',constant)

#cv2.waitKey(0)
#cv2.destroyWindow()

