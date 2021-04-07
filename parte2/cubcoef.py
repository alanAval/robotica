import numpy as np
import utils


def calculatevel(theta, currentpos, tf):
    if currentpos == (len(theta) - 1) or currentpos == 0:
        return 0
    leftinc = (theta[currentpos] - theta[currentpos - 1]) / tf
    rightinc = (theta[currentpos + 1] - theta[currentpos]) / tf
    if leftinc * rightinc > 0:
        return leftinc + rightinc / 2
    else:
        return 0

def cubcoef(th0, thf, thdot0, thdotf, tf):
    a0 = th0
    a1 = thdot0
    a2 = (3 / tf*tf)*(thf - th0) - (2 / thf) * thdot0 - thdotf / tf
    a3 = - (2/np.power(tf, 3)) * (thf - th0) + (thdotf + thdot0) / tf * tf
    return np.array([a0, a1, a2, a3])

def cubcoefs(splines, tf, Twt, l1, l2):
    thdot0 = np.zeros(3)
    theta = np.array([])
    tp = tf / (len(splines) - 1)
    for i in range(len(splines)):
        Tws = utils.transform_frame(Twt, splines[i])
        thetai = np.array([utils.inverse_kinemactics(Tws, l1, l2)[0]])

        if i == 0:
            theta = thetai
        else:
            theta = np.concatenate((theta, thetai), axis=0)
    print(theta)

    coef = np.array([[]])
    for i in range(len(splines) - 1):
        coefi = np.array([])
        thdotfarray = np.array([])
        for j in range(3):
            thdotf = calculatevel(theta[:, j], i, tp)
            coefj = np.array([cubcoef(theta[i][j], theta[i + 1][j], thdot0[j], thdotf, tp)])
            if j == 0:
                coefi = coefj
                thdotfarray = np.array([thdotf])
            else:
                coefi = np.concatenate((coefi, coefj), axis=0)
                thdotfarray = np.concatenate((thdotfarray, np.array([thdotf])), axis=0)
        thdot0 = thdotfarray
        if i == 0:
            coef = np.array([coefi])
        else:
            coef = np.concatenate((coef, np.array([coefi])), axis=0)
    return coef


# coef = cubcoefs(np.array([[0.758, 0.173, 0], [0.6, -0.3, 45], [-0.4, 0.3, 120]]), 1, np.array([0.1, 0.2, 30.0]), 0.5, 0.5)
# print("------------Coeficientes-----------")
# print(coef)