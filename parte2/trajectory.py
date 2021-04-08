import numpy as np
import utils
import cubcoef 
from matplotlib import pyplot, transforms

#questão 2

def position_trajectory(coefs, freq, total_time, part_time):
    theta = np.empty((0, 3), float)
    for section in range(int(total_time / part_time)):
        for j in range(int(freq * part_time) + 1):
            coef = coefs[section]
            t = j / freq
            thetaJ = coef[:, 0] + coef[:, 1]*t + coef[:,2]*t*t + coef[:, 3]*t*t*t
            theta = np.vstack((theta, thetaJ))
        pass
    return theta

def velocity_trajectory(coefs, freq, total_time, part_time):
    theta = np.empty((0, 3), float)
    for section in range(int(total_time / part_time)):
        for j in range(int(freq * part_time) + 1):
            coef = coefs[section]
            t = j / freq
            thetaJ = coef[:, 1] + 2*coef[:,2]*t + 3*coef[:, 3]*t*t
            theta = np.vstack((theta, thetaJ))

    return theta

def acceleration_trajectory(coefs, freq, total_time, part_time):
    theta = np.empty((0, 3), float)
    for section in range(int(total_time / part_time)):
        for j in range(int(freq * part_time) + 1):
            coef = coefs[section]
            t = j / freq
            thetaJ = 2*coef[:,2] + 6*coef[:, 3]*t
            theta = np.vstack((theta, thetaJ))

    return theta

#questão 2


t = 9.0
tp = 3.0
freq = 40

Twt = np.array([0.1, 0.2, 30.0])
coefs = cubcoef.cubcoefs(np.array([[0.758, 0.173, 0], [0.6, -0.3, 45], [-0.4, 0.3, 120], [0.758, 0.173, 0]]), t, Twt, 0.5, 0.5)
print("------------Coeficientes-----------")
print(coefs)
position = position_trajectory(coefs, freq, t, tp)
velocity = velocity_trajectory(coefs, freq, t, tp)
acceleartion = acceleration_trajectory(coefs, freq, t, tp)

timeValues = np.linspace(0, t, num=freq*9 + 3)

pyplot.figure(num=1, figsize=(20, 10))

for i in range(3):
    pyplot.subplot(331 + i)
    pyplot.title('Posição da junta ' + str(i+ 1) + ' em rad')
    pyplot.plot(timeValues, position[:,i], '-')
    pyplot.subplot(334 + i)
    pyplot.title('Velocidade da junta ' + str(i+ 1) + ' em rad/s')
    pyplot.plot(timeValues, velocity[:,i], '-')
    pyplot.subplot(337 + i)
    pyplot.title('Aceleração da junta ' + str(i+ 1) + ' em rad/s^2')
    pyplot.plot(timeValues, acceleartion[:,i], '-')

pyplot.figure(num=2, figsize=(20, 10))

pos = np.empty((0, 3), float)

for i in position:
    pos = np.vstack((pos, utils.direct_kinemactics(i, 0.5, 0.5, Twt)[1]))

x = pos[:, 0]
y = pos[:, 1]

pyplot.title('Posições cartesianas')
pyplot.plot(x, y, '-')

print(pos)

pyplot.show()