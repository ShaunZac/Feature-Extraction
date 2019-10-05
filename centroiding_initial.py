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

def getregion(j, i, region, img):
    """Recursively adds all pixels above threshold to the array named region"""
    edge = j == img.shape[0] or i == img.shape[1] or j == -1*img.shape[0] or i == -1*img.shape[1]
    if(len(region) > 60 or edge):
        return
    if(img[j, i] <= thresh):
        return region
    else:
        img[j, i] = 0 #setting it to 0 so it is not counted again
        region.append([j, i])
        if edge:
            return region
        else:
            getregion(j, i-1, region, img)
            getregion(j, i+1, region, img)
            getregion(j+1, i, region, img)
            getregion(j-1, i, region, img)        

def rga(j, i, img, img1):
    """This implements the region growing algorithm"""
    region = []
    getregion(j, i, region, img) #once whole region is identified, it is assigned
    return centroid(region, img1)


import cv2
import numpy as np
import matplotlib.pyplot as plt
import time 


n = 3 #Every nth pixel is checked
centroids = []
# Reading the images as arrays
img = np.array(cv2.imread("image1.png", 0))
img1 = img.copy()
thresh = 10

start = time.time()
xlen = img.shape[1] #length of image in x
ylen = img.shape[0] #length of image in y
for i in range(xlen//n):
    for j in range(ylen//n):
        if img[n*j,n*i] > thresh: #checking for seeds in every nth pixel
            centroids.append(rga(n*j, n*i, img, img1))

end = time.time()
centroids = np.array(centroids) #converting into numpy array so it can be plotted 
print("Total time taken = " +str((end-start)*1000)+" ms")
print("Number of stars = " +str(centroids.shape[0]))

#This part is solely done to get a pictorial representation of the data obtained
plt.rcParams['axes.facecolor'] = 'black'
x = []
y = []
for i in centroids:
    x.append(i[1])
    y.append((-1)*i[0])
plt.plot(x, y, 'w.', )

#image = np.zeros(img.shape, dtype = np.uint8)
#for m in centroids:
#    image[m[0], m[1]] = 255
#cv2.imshow('img', img1)
#cv2.waitKey(0)
#cv2.destroyAllWindows()