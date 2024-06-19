import numpy as np
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import sys

# orbital = str(sys.argv[1])
bohr_radius = 1.5
hz = 2 * 10^10
judgeRate = 1

n = 1
l = 0
m = 0

# print(orbital)

def fR(rad):
    if n == 1 and l == 0:
        return 2 * np.exp(-rad / bohr_radius) * np.sqrt(1 / (bohr_radius ** 3))
    elif n == 2 and l == 1:
        return (rad / bohr_radius) * np.exp(-rad / (2 * bohr_radius)) * np.sqrt(3 * (2 * bohr_radius)^3)
    elif n == 3 and l == 2:
        return (((rad / bohr_radius)^2) * 4 / 27) * np.exp(-rad / (3 * bohr_radius)) * np.sqrt(10 * (3 * bohr_radius)^3)

def fY(th, ph):
    if n == 1 and l == 0:
        if m == 0:
            return (1 / 2) * np.sqrt(1 / np.pi)
    elif n == 2 and l == 1:
        if m == 0:
            return (1 / 2 * np.cos(th)) * np.sqrt(3 / np.pi)
        else:
            return (- 1 / m * 1 / 2 * np.sin(th)) * np.sqrt(3 / (2 * np.pi)) * np.exp(m * 1j * ph)
    elif n == 3 and l == 2:
        if m == 0:
            return (1 / 4 * (3 * (np.cos(th)^2) - 1)) * np.sqrt(5 / np.pi)
        elif m == 1 or m == -1:
            return (- 1 / m * 1 / 2 * np.sin(th) * np.cos(th)) * np.sqrt(15 / (2 * np.pi)) * np.exp(m * 1j * ph)
        else:
            return (1 / 4 * np.sin(th) * np.sin(th)) * np.sqrt(15 / (2 * np.pi)) * np.exp(m * 2j * ph)

x = np.linspace(0, 6, 100)
y = [fR(t) for t in x]

plt.plot(x, y)
plt.show()
