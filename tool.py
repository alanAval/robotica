import numpy as np
l1 = 0.65
l2 = 0.22

def jacobian(theta):
    s2 = np.sin(theta[1])
    c2 = np.cos(theta[1])
    return np.array([
        [(l1*s2), 0],
        [l1*c2 + l2, l2]])



theta1 = 0
theta2 = 16.28
theta3 = 30

j = jacobian(np.array([theta1, theta2, theta3]) * np.pi / 180)

print(j)