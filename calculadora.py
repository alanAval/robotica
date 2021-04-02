import numpy as np





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