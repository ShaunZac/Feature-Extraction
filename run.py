#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 00:10:43 2019

@author: shaun
"""
import img_gen
import centroiding_initial
import numpy as np
for i in range(10):
#    img_gen
    centroiding_initial
    from img_gen import cen
    from centroiding_initial import centroids

    diff = cen - centroids
    sqrt = []
    for i in diff:
        sqrt.append((i[0]**2+i[1]**2)**0.5)
    print("Mean  error: " + str(np.mean(sqrt)) + " Max error: " + str(max(sqrt)))