import numpy as np
import matplotlib.pyplot as plt
import cv2

image = np.zeros((480,640))

def f(x, y, H, sigma, x_0, y_0):
    return H * np.exp(-((x - x_0) ** 2 + (y - y_0) ** 2) / (2 * sigma ** 2)) / (2 * np.pi * sigma ** 2)

def H(M, k_1 = 10 ** 5, k_2 = 1, k_3 = 1):
    return k_1 * np.exp(- k_2 * M + k_3)

f_noise_max = 30
f_noise_min = 0
def r(f_n_max = f_noise_max, f_n_min = f_noise_min):
    return f_n_min + (f_n_max - f_n_min) * np.random.random()

# Selecting the stars
n = 10
x = 10 + (image.shape[0] - 10) * np.random.random(n)
y = 10 + (image.shape[1] - 10) * np.random.random(n)
b = 6 * np.random.random(n)

cen = np.array([x,y])
cen = cen.T
cen = np.array(sorted(cen, key = lambda x:x[0]))

#plt.plot(y, 480 - x, 'o')
#plt.xlim(0,640)
#plt.ylim(0,480);
#plt.axis('off');
#plt.savefig('coordinates.jpg', quality = 95, format = 'jpg')

image2 = np.zeros(image.shape)
sigma = 1.5
for i in np.arange(n):
    for j in np.arange(image2.shape[0]):
        for k in np.arange(image2.shape[1]):
            image2[j][k] = image2[j][k] + f(j, k, H(b[i]), sigma, x[i], y[i])


image = image2.copy()
for j in np.arange(image.shape[0]):
    for k in np.arange(image.shape[1]):
        image[j][k] = image[j][k] + r()


cv2.imwrite('Image 1.jpg', image)