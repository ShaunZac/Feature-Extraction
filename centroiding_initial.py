#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 14:41:23 2019

@author: shaun
"""

def centroid(region, img):
    """ Takes input in terms of coordinates of region
    and returns its centroid"""
    x_centre = 0
    y_centre = 0
    elements = 0
    for i in region:
        x_centre += i[0]*img[i[0], i[1]]
        y_centre += i[1]*img[i[0], i[1]]
        elements += 1*img[i[0], i[1]]
    return [x_centre/elements, y_centre/elements]

def getRegion(j, i, region, img):
    """Recursively adds all pixels above threshold to the array named region
    Takes starting point coordinates as input"""
    #checks if current seed is edge one or not
    edge = j==img.shape[0] or i==img.shape[1] or j==-1*img.shape[0] or i==-1*img.shape[1]
    if(len(region) > 150 or edge):
        return
    if(img[j, i] <= thresh):
        return region
    else:
        img[j, i] = 0 #setting it to 0 so it is not counted again
        region.append([j, i])
        if edge:
            return region
        else:
            getRegion(j, i-1, region, img)
            getRegion(j, i+1, region, img)
            getRegion(j+1, i, region, img)
            getRegion(j-1, i, region, img)        

def rga(j, i, img, img1):
    """This implements the region growing algorithm"""
    region = []
    getRegion(j, i, region, img) #once whole region is identified, it is assigned
    if(len(region) > 149):
        return
    return centroid(region, img1)


import cv2
import numpy as np
import matplotlib.pyplot as plt
import time 
import math

n = 3 #Every nth pixel is checked
centroids = []
# Reading the images as arrays
img = np.array(cv2.imread("Image 1.jpg", 0))
img1 = img.copy()
thresh = 45 #arbitrarily set threshold value for intensity value

start = time.time()
xlen = img.shape[1] #length of image in x
ylen = img.shape[0] #length of image in y
for i in range(xlen//n):
    for j in range(ylen//n):
        if img[n*j,n*i] > thresh: #checking for seeds in every nth pixel
            centroids.append(rga(n*j, n*i, img, img1))

end = time.time()
centroids = np.array(centroids) #converting into numpy array so it can be plotted 
#print("Total time taken = " +str((end-start)*1000)+" ms")
#print("Number of stars = " +str(centroids.shape[0]))
centroids = np.array(sorted(centroids, key = lambda x:x[0])) #sorting by first element

#This part is solely done to get a pictorial representation of the data obtained
plt.rcParams['axes.facecolor'] = 'black'
#plt.xlim(0,640)
#plt.ylim(0,480)
#plt.axis('off');
x = []
y = []
for i in centroids:
    x.append(i[1])
    y.append((-1)*i[0]+480)
#plt.plot(x, y, 'w.', )

#Done for making image of centroids
image = np.zeros(img.shape, dtype = np.uint8)
for m in centroids:
    image[math.floor(m[0]), math.floor(m[1])] = 255
cv2.imwrite('gen4_result.jpg', image)
cv2.waitKey(0)
cv2.destroyAllWindows()