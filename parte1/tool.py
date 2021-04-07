import numpy as np
import veltrans as vt
import utils
from matplotlib import pyplot, transforms

l1 = l2 = 0.5

def solve_tool(theta, option):
    print("Começo dos resultados para opção: " + str(option) + "-----------------")
    j = utils.jacobian(l1, l2, theta[option,])
    print("Jacobiano: \n" + str(j))

    vl = j @ (np.array([20, -10, 12]) * np.pi / 180)

    omega = np.array([0, 0, 20 - 10 + 12])

    vw = np.concatenate((vl, omega))

    print("Velocidade W,W: \n" + str(vw))

    t = np.array([[np.sqrt(3)/2, -1/2, 0, ((2 - np.sqrt(3))/20)], 
                [1/2, np.sqrt(3)/2, 0, ((-1 -2*np.sqrt(3))/20)],
                [0, 0, 1, 0],
                [0, 0, 0, 1]])

    vT = vt.veltrans(t, vw)
    print("Velocidade T,T: \n" + str(vT))
    print("Fim dos resultados para opção: " + str(option) + "-----------------")
    #Modo 1
    b = np.array([0, 0])
    bIy = l1 * np.sin(theta[option,0])
    bIx = l1 * np.cos(theta[option,0])
    bI = np.array([bIx, bIy])
    bw = np.array([0.45, -0.47])
    bt = np.array([0.6, -0.3])

    x = np.array([b[0], bI[0], bw[0], bt[0]])
    y = np.array([b[1], bI[1], bw[1], bt[1]])

    pyplot.subplot(121 + option)
    utils.plot_robot(x, y, "Robô disposição " + str(option + 1))


bw = np.array([0.45, 0.47, 16.28 * np.pi / 180])

Tbw = np.array([[0.96, 0.25, 0, 0.45],
                [-0.25, 0.96, 0, -0.47],
                [0, 0, 1, 0],
                [0, 0, 0, 0]])

theta = utils.inverse_kinemactics(Tbw, l1, l2)

print(theta * 180 / np.pi)

pyplot.figure(figsize=(10, 5))

solve_tool(theta, 0)
solve_tool(theta, 1)

pyplot.show()