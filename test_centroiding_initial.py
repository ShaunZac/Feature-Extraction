#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 19:23:48 2019

@author: shaun
"""
import numpy as np
from centroiding_initial import centroid 
from centroiding_initial import getRegion
from centroiding_initial import rga
def test_centroid():
    """Tests centroid() function in the file, gives true if it passes the test case"""
    region = []
    img = np.ones((10, 10))*50
    for i in range(5):
        for j in range(5):
            region.append([i, j])
    case1 = centroid(region,img) == [2.0, 2.0]
    return case1

def test_getRegion():
    """Tests getRegion() function in the file, gives true if it passes the test case"""
    image = np.array([[20, 10, 5, 0],
             [0, 155, 0, 0],
             [0, 255, 125, 0],
             [0, 155, 0, 0],
             [0, 15, 7, 0]])
    region = []
    getRegion(1, 1, region, image)
    region.sort()
    case1 = region == [[1, 1], [2, 1], [2, 2], [3, 1]]
    
    image = np.array([[0, 0, 0, 0, 0],
                      [0, 70, 155, 255, 0],
                      [0, 255, 255, 0, 0],
                      [0, 175, 255, 95, 0],
                      [0, 0, 0, 0, 0]])
    region = []
    getRegion(2, 2, region, image)
    region.sort()
    case2 = region == [[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [3, 1], [3, 2], [3, 3]]
    
    image = np.array([[0, 0, 0, 0, 0],
                      [0, 70, 155, 255, 0],
                      [0, 255, 255, 0, 0],
                      [0, 175, 255, 95, 0],
                      [0, 0, 0, 0, 0]])
    region = []
    getRegion(3, 3, region, image)
    region.sort()
    case3 = region == [[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [3, 1], [3, 2], [3, 3]]
    
    image = np.ones((480,640), dtype = np.uint8)*255
    image1 = image.copy()
    case4 =  rga(1, 1, image, image1) == None
    return case1 and case2 and case3 and case4
  
    
if(test_centroid() and test_getRegion()):
    print("Code Successful! Hurray!")