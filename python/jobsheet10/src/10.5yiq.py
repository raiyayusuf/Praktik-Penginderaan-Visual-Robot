import cv2
import numpy as np

SKALA_CMYK = 255
MAT_YIQ = np.array([[0.299, 0.587, 0.114],
                    [0.596, -0.274, -0.322],
                    [0.211, -0.523, 0.312]])

MAT_RGB = np.array([[1, 0.956, 0.621],
                    [1, -0.272, -0.647],
                    [1, -1.106, 1.703]])

def rgbKeYiq(r, g, b):
    rgb = np.array([r, g, b]) / 255.0
    yiq = MAT_YIQ.dot(rgb)
    return int(yiq[0] * 255 + .5), int(yiq[1] * 255 + .5), int(yiq[2] * 255 + .5)

def yiqKeRgb(y, i, q):
    yiq = np.array([y, i, q]) / 255.0
    rgb = MAT_RGB.dot(yiq)
    return int(rgb[0] * 255 + .5), int(rgb[1] * 255 + .5), int(rgb[2] * 255 + .5)

y, i, q = rgbKeYiq(171, 20, 250)
print("Y =", y)
print("I =", i)
print("Q =", q)
print()
r, g, b = yiqKeRgb(y, i, q)
print("R =", r)
print("G =", g)
print("B =", b)