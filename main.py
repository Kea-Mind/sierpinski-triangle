import numpy as np
import random
import cv2
import math

def random_point_on_triangle(A, B, C):
    """
    http://www.cs.princeton.edu/~funk/tog02.pdf
    https://stackoverflow.com/a/47425047/8455692
    Given three vertices A, B, C, 
    sample point uniformly in the triangle
    """
    r1 = random.random()
    r2 = random.random()
    s1 = math.sqrt(r1)
    y = A[0] * (1.0 - s1) + B[0] * (1.0 - r2) * s1 + C[0] * r2 * s1
    x = A[1] * (1.0 - s1) + B[1] * (1.0 - r2) * s1 + C[1] * r2 * s1
    return np.round( (y, x)).astype(int)

H, W = 1000, 1000
A, B, C = (100, 500), (900, 100), (900, 900)
canvas = np.ones( (H, W) )
canvas[tuple(zip(A, B, C)) ] = 0
point = random_point_on_triangle(A, B, C)
canvas[point[0], point[1]] = 0
i = 0
while True:
    corner = (A, B, C)[np.random.randint(3)]
    point = (int((point[0] + corner[0]) / 2) , int((point[1] + corner[1]) / 2) )
    canvas[point[0], point[1]] = 0
    i += 1
    if i % 100 == 0:
        cv2.imshow('Canvas', canvas) # Render canvas
        cv2.waitKey(5) # Wait for render
cv2.destroyAllWindows()