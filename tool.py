import numpy as np
import veltrans as vt
import utils

j = utils.jacobian(0, 0.65, np.array([0, 16.28, 30]) * np.pi / 180)
print("Jaboian: " + str(j))

vl = j @ (np.array([20, -10, 12]) * np.pi / 180)
print(vl)

omega = np.array([0, 0, 20 - 10 + 12])

vw = np.concatenate((vl, omega))

print(vw)

t = np.array([[np.sqrt(3)/2, -1/2, 0, ((2 - np.sqrt(3))/20)], 
               [1/2, np.sqrt(3)/2, 0, ((-1 -2*np.sqrt(3))/20)],
               [0, 0, 1, 0],
               [0, 0, 0, 1]])

print(t)


vT = vt.veltrans(t, vw)
print("Vt = " + str(vT))

b = np.array([0, 0, 0])
bs = np.array([0, 0, 0])
sw = np.array([0.45, 0.47, 16.28 * np.pi / 180])
st = np.array([0.6, -0.3, 45 * np.pi / 180])

x = np.array([b[0], bs[0], sw[0], st[0]])
y = np.array([b[1], bs[1], sw[1], st[1]])

utils.plot_robot(x, y, "Robô")