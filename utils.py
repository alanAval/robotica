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
    pyplot.text(x[0], y[0], 'B', horizontalAlignment= 'right')
    pyplot.text(x[1], y[1], 'S', horizontalAlignment= 'left')
    pyplot.text(x[2], y[2], 'W')
    pyplot.text(x[3], y[3], 'T')


def plot_robot(x, y, title="", axis=[-1, 1, -1, 1]):
    pyplot.plot(x, y, 'xb')
    pyplot.plot(x, y, '-r')

    pyplot.axis(axis)
    pyplot.title(title)
    draw_labels(x, y)

    pyplot.show()

def jacobian(l1, l2, theta):
    s2 = np.sin(theta[1])
    s3 = np.sin(theta[2])
    c2 = np.cos(theta[1])
    c3 = np.cos(theta[2])
    return np.array([
        [(l1*s2*c3) + (l1*c2*s3) + (l2*s3), l2*s3, 0],
        [(-l1*s2*s3) + (l1*c2*c3) + (l2*c3), l2*c3, 0],
        [0, 0, 0]])