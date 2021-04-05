import numpy as np
import utils

theta1 = 20
theta2 = -10
theta3 = 12

j = utils.jacobian(0.5, 0.5, np.array([theta1, theta2, theta3]) * np.pi / 180)
print(j)

















