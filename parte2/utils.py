import numpy as np
from matplotlib import pyplot, transforms

def transform_point(p_org, theta, p):
    t = np.array([
        [np.cos(theta), -np.sin(theta), 0, p_org[0]],
        [np.sin(theta), np.cos(theta), 0, p_org[1]],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
        ])
    print(t)
    return t @ np.concatenate((p, [1]), axis= 0)

def draw_labels(x, y):
    pyplot.text(x[0], y[0], 'B')
    pyplot.text(x[1], y[1], 'I')
    pyplot.text(x[2], y[2], 'W')
    pyplot.text(x[3], y[3], 'T')


def plot_robot(x, y, title=""):
    pyplot.plot(x, y, 'xb')
    pyplot.plot(x, y, '-r')
    pyplot.title(title)
    draw_labels(x, y)

def jacobian(l1, l2, theta):
    s2 = np.sin(theta[1])
    s3 = np.sin(theta[2])
    c2 = np.cos(theta[1])
    c3 = np.cos(theta[2])
    return np.array([
        [(l1*s2*c3) + (l1*c2*s3) + (l2*s3), l2*s3, 0],
        [(-l1*s2*s3) + (l1*c2*c3) + (l2*c3), l2*c3, 0],
        [0, 0, 0]])

def inverse_kinemactics(T, l1, l2):
    theta = np.array([[0.0, 0.0, 0.0],[0.0, 0.0, 0.0]])
    x = T[0][3]
    y = T[1][3]
    c2 = (x*x + y*y - l1*l1 - l2*l2)/(2*l1*l2)
    s2 = np.sqrt(1 - c2*c2)
    theta[0][1] = np.arctan(s2/c2)
    theta[1][1] = -np.arctan(s2/c2)
    k1 = l1 + l2*c2
    k2 = l2*s2
    theta[0][0] = np.arctan(y / x) - np.arctan(k2/k1)
    theta[1][0] = np.arctan(y / x) + np.arctan(k2/k1)
    phi = np.arccos(T[0][0])
    theta[0][2] = phi - theta[0][0] - theta[0][1]
    theta[1][2] = phi - theta[1][0] - theta[1][1]
    return theta

def mount(x, y, theta):
    stheta = np.sin(theta * np.pi / 180)
    ctheta = np.cos(theta * np.pi / 180)

    return np.array([[ctheta, -stheta, 0, x],
                   [stheta, ctheta, 0, y],
                   [0, 0, 1, 0],
                   [0, 0, 0, 1]])

def transform_frame(tab, tac):
    Tab = mount(tab[0], tab[1], tab[2])
    Tac = mount(tac[0], tac[1], tac[2])

    return Tac @ np.linalg.inv(Tab)

def direct_kinemactics(theta, l1, l2, Twt):
    T01 = mount(0, 0, theta[0])
    T12 = mount(l1 * np.cos(theta[1]), l1 * np.sin(theta[1]), theta[1])
    T23 = mount(l2 * np.cos(theta[2]), l2 * np.sin(theta[2]), theta[2])
    T34 = mount(Twt[0], Twt[1], Twt[2])
    T04 = T01 @ T12 @ T23 @ T34
    return (T04, np.array([T04[0, 3], T04[1, 3], np.arccos(T04[0, 0]) * 180 / np.pi]))
