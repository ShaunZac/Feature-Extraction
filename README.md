Readme file for img_gen.py
Electrical Subsystem


centroid()
Author: Shaun Zacharia
Date: 16 October 2019
This function gives the centroid of an array.
Input: takes in a 2D array containing all coordinates of the desired region and also takes an image (again a multidimensional array) that contains weights corresponding to each element in the array.
Output: Outputs an array with 2 elements, the x and y coordinate
The function calculates centroid by taking the weighted sum of the x and y coordinates.

getRegion()
Author: Shaun Zacharia
Date: 16 October 2019
This function recursively identifies the region in which a star is contained
Input: takes seed coordinate as (i, j), the region that has already been identified and the image array containing intensity values of the image.
Output: returns an array that contains all the points in which the star region has been identified.
This function uses the region growing algorithm that checks if the seed coordinates given are above the threshold or not. Then it checks for the same in its four nearest neighbours and recursively adds seeds to the array named region. It sets the initial seed intensity value to zero so that there is no redundancy in finding the region. If the elements in the region exceed a fixed number, then the function rejects that region.
References: https://pdfs.semanticscholar.org/4f03/43d34aecf058503eb377dbe147400d53242b.pdf

rga()
Author: Shaun Zacharia
Date: 16 October 2019
This function puts together the centroid and getRegion functions.
Input: two copies of the image and the seed coordinate.
Output: array containing centroids of stars.
