#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 19:14:52 2019

@author: shaun
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2
from random import randint

image = np.zeros((480,640))
sigma = 1.5

z1=np.sqrt((2 * np.pi * sigma ** 2))
def f(x, y, H, sigma, x_0, y_0):
    return H * (np.exp(-((x - x_0) ** 2 + (y - y_0) ** 2) / (2 *sigma ** 2)) / z1)

def H(M, k_1 = 10 ** 5, k_2 = 1, k_3 = 1):
    return k_1 * np.exp(- k_2 * M + k_3)

f_noise_max = 30
f_noise_min = 0
def r(f_n_max = f_noise_max, f_n_min = f_noise_min):
    return f_n_min + (f_n_max - f_n_min) * np.random.random()

n = 15
w = 50
x = 50 + (image.shape[0] - w-2) * np.random.random(n)
y = 50 + (image.shape[1] - w-2) * np.random.random(n)
b = 6 * np.random.random(n)

cen = []
for i in range(n):
    if 480 - y[i] <0:
        cen.append([960-y[i],x[i]])
    else:
        cen.append([480-y[i],x[i]])   
print("\n")
cen.sort()

image2 = np.zeros(image.shape)
for i in np.arange(n):
    m1=int(round(480-y[i]-w/2))
    n1=int(round(x[i]-w/2))
    amp=randint(1,n/5)
    #for j in np.arange(image2.shape[0]):
    for j in range(w):
        #for k in np.arange(image2.shape[1]):
         for k in range(w):
            z=f(m1+j, n1+k, (255*5/n)*amp*z1, sigma, 480-y[i], x[i])
            #print(z/H(b[i]))
            if( m1+j > 479 or n1+k > 639):
                break
            image2[m1+j][n1+k] = image2[m1+j][n1+k] + z

image = image2.copy()
for j in np.arange(image.shape[0]):
    for k in np.arange(image.shape[1]):
        image[j][k] = image[j][k] + r()
        
cv2.imwrite('gen6.jpg', image)