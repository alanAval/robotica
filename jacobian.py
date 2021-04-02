import numpy as np
l1 = 0.5
l2 = 0.5

def jacobian(theta):
    s2 = np.sin(theta[1])
    s3 = np.sin(theta[2])
    c2 = np.cos(theta[1])
    c3 = np.cos(theta[2])
    return np.array([
        [(l1*s2*c3) + (l1*c2*s3) + (l2*s3), l2*s3, 0],
        [(-l1*s2*s3) + (l1*c2*c3) + (l2*c3), l2*c3, 0],
        [0, 0, 0]])



theta1 = 20
theta2 = -10
theta3 = 12

j = jacobian(np.array([theta1, theta2, theta3]) * np.pi / 180)
print(j)

















