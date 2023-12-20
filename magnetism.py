import cv2
import numpy as np
import math

image = cv2.imread("image.png")

h, w, notrelated = image.shape
current = 5

blacks = []
slopes = []

def checkblack(x, y):
    pixel = image[i, j]
    if sum(pixel) == 0:
        blacks.append((i, j))

for i in range(h):
    for j in range(w):
        checkblack(i, j)
        
for i in blacks:
    distances = [((x[0] - i[0])**2 + (x[1] - i[1])**2)**0.5 for x in blacks]
    nexti = blacks[distances.index((sorted(distances)[1]))]
    if nexti[0] - i[0] != 0:
        slope = (nexti[1] - i[1])/(nexti[0] - i[0])
        slopes.append(math.atan(slope))
    else:
        slopes.append(math.pi/2)


        
a = len(blacks)
print(a, len(slopes))
print(slopes)
for i in range(h):
    for j in range(w):
        value = 0
        for bn in range(a):
            x = blacks[bn]
            rsquared = ((x[0] - i)**2 + (x[1] - j)**2)
            if (x[0] - j) != 0:
                rsloped = math.atan((x[1] - i)/(x[0] - j))
            else:
                rsloped = math.pi/2
            
            cross = math.sin(slopes[bn] - rsloped)
            value += (current * cross)/rsquared
        print(value)
        
cv2.imshow("mat", image)
cv2.waitKey(0)
        
