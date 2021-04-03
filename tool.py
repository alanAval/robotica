import numpy as np
import jacobian as jb
import veltrans as vt

j = jb.jacobian(0, 0.65, np.array([0, 16.28, 30]) * np.pi / 180)
print(j)

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
print(vT)