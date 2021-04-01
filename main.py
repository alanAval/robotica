import numpy as np

def extract_rba(brela):
    rab = brela[0:3, 0:3]
    return rab.transpose()

def extract_pborg(brela):
    return brela[0:3, 3]

def cross(p):
    return np.array([[0, -p[0], p[1]], [p[0], 0, -p[0]], [-p[1], p[0], 0]])

def mount(brela):
    rba = extract_rba(brela)
    pborg = extract_pborg(brela)
    pborg_cross = cross(pborg)
    x = -1 * (rba @ pborg_cross)
    zero = np.zeros((3,3))
    top_part = np.concatenate((rba, x), axis=1)
    bottom_part = np.concatenate((zero, rba), axis=1)
    return np.concatenate((top_part, bottom_part), axis=0)


def veltrans(brela, vrela):
    x = mount(brela)
    return x @ vrela

brela = np.array([[0.866, -0.5, 0, 10], [0.5, 0.866, 0, 5], [0, 0, 1, 0], [0, 0, 0, 1]])
vrela = np.array([10, 5, 0, 0, 0, 5])

print(brela)
print(vrela)
print(veltrans(brela, vrela.transpose()))