import numpy as np
import utils
import cubcoef 
from matplotlib import pyplot, transforms

def transform_angle_single(angle):
    if angle > 180:
        angle = angle - 360
    return angle

def transform_angle(angle):
    for i in range(len(angle)):
        angle[i] = transform_angle_single(angle[i])

def position_trajectory(coefs, freq, total_time, part_time):
    theta = np.empty((0, 3), float)
    for section in range(int(total_time / part_time)):
        for j in range(int(freq * part_time)):
            coef = coefs[section]
            t = j / freq * part_time
            thetaJ = coef[:, 0] + coef[:, 1]*t + coef[:,2]*t*t + coef[:, 3]*t*t*t
            theta = np.vstack((theta, thetaJ))

    return theta

def velocity_trajectory(coefs, freq, total_time, part_time):
    theta = np.empty((0, 3), float)
    for section in range(int(total_time / part_time)):
        for j in range(int(freq * part_time)):
            coef = coefs[section]
            t = j / freq * part_time
            thetaJ = coef[:, 1] + 2*coef[:,2]*t + 3*coef[:, 3]*t*t
            theta = np.vstack((theta, thetaJ))

    return theta

def acceleration_trajectory(coefs, freq, total_time, part_time):
    theta = np.empty((0, 3), float)
    for section in range(int(total_time / part_time)):
        for j in range(int(freq * part_time)):
            coef = coefs[section]
            t = j / freq * part_time
            thetaJ = 2*coef[:,2] + 6*coef[:, 3]*t
            theta = np.vstack((theta, thetaJ))

    return theta



coefs = cubcoef.cubcoefs(np.array([[0.758, 0.173, 0], [0.6, -0.3, 45], [-0.4, 0.3, 120], [0.758, 0.173, 0]]), 3, np.array([0.1, 0.2, 30.0]), 0.5, 0.5)
print("------------Coeficientes-----------")
print(coefs)
position = position_trajectory(coefs, 40, 3, 1)
velocity = velocity_trajectory(coefs, 40, 3, 1)
acceleartion = acceleration_trajectory(coefs, 40, 3, 1)

timeValues = np.linspace(0, 3, num=40*3)

pyplot.figure(figsize=(10, 5))

print(position)

pyplot.subplot(331)
pyplot.plot(timeValues, position[:,0], '-')
pyplot.subplot(332)
pyplot.plot(timeValues, position[:,1], '-')
pyplot.subplot(333)
pyplot.plot(timeValues, position[:,2], '-')

pyplot.subplot(334)
pyplot.plot(timeValues, velocity[:,0], '-')
pyplot.subplot(335)
pyplot.plot(timeValues, velocity[:,1], '-')
pyplot.subplot(336)
pyplot.plot(timeValues, velocity[:,2], '-')

pyplot.subplot(337)
pyplot.plot(timeValues, acceleartion[:,0], '-')
pyplot.subplot(338)
pyplot.plot(timeValues, acceleartion[:,1], '-')
pyplot.subplot(339)
pyplot.plot(timeValues, acceleartion[:,2], '-')

pyplot.show()
