import numpy as np
import veltrans as vt

m1 = np.array([[np.sqrt(2)/2, np.sqrt(2)/2, 0, 0.6], 
               [-(np.sqrt(2)/2), np.sqrt(2)/2, 0, -0.3],
               [0, 0, 1, 0],
               [0, 0, 0, 1]])

m2 = np.array([[np.sqrt(3)/2, -1/2, 0, ((2 - np.sqrt(3))/20)], 
               [1/2, np.sqrt(3)/2, 0, ((-1 -2*np.sqrt(3))/20)],
               [0, 0, 1, 0],
               [0, 0, 0, 1]])


print(m1 @ m2)


print(np.arccos(0.96) * 180 / np.pi)

print(16.26 * np.pi / 180)


print(np.sqrt(0.45*0.45 + 0.47*0.47))

print(np.sqrt(0.1*0.1 + 0.2*0.2))

print('test 2')

def jacbian(l1, l2, s2, c2):
    return np.array([[l1*s2, 0, 0], [l1*c2 + l2, l2, 0], [0 , 0, 0]])


j = jacbian(0.65, 0.22, 0.28033165657793746, 0.9599032046619437)

print(j @ np.array([20, -10, 12]))




l1 = 0
l2 = 0.65

def jacobian(s2, s3, c2, c3):
    return np.array([
        [(l1*s2*c3) + (l1*c2*s3) + (l2*s3), l2*s3, 0],
        [(-l1*s2*s3) + (l1*c2*c3) + (l2*c3), l2*c3, 0],
        [0, 0, 0]])

j = jacobian(0, 0.28033165657793746, 1, 0.9599032046619437)
vl = j @ np.array([20, -10, 12])
print(vl)