import numpy as np
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import sys

orbital = str(sys.argv[1])
bohr_radius = 1.5
hz = 2 * 10 ** 10
judgeRate = 1

# n = 1
# l = 0
# m = 0

# print(orbital)

# if orbital == 's0':
#     n = 1; l = 0; m = 0
# elif orbital == 'p0':
#     n = 2; l = 1; m = 0
# elif orbital == 'p1':
#     n = 2; l = 1; m = 1
# elif orbital == 'p-1':
#     n = 2; l = 1; m = -1
# elif orbital == 'd0':
#     n = 3; l = 2; m = 0
# elif orbital == 'd1':
#     n = 3; l = 2; m = 1
# elif orbital == 'd-1':
#     n = 3; l = 2; m = -1
# elif orbital == 'd2':
#     n = 3; l = 2; m = 2
# elif orbital == 'd-2':
    # n = 3; l = 2; m = -2
    
def fR(rad):
    if orbital == 's0':
        return 2 * np.sqrt((hz / bohr_radius) ** 3) * np.exp(-0.5 * hz * rad / bohr_radius)
    elif orbital == 'p-1' or orbital == 'p0' or orbital == 'p1':
        return rad * np.exp(-rad / (2 * bohr_radius)) / (np.sqrt(24 * (bohr_radius ** 5)))
    elif orbital == 'd-2' or orbital == 'd-1' or orbital == 'd0' or orbital == 'd1' or orbital == 'd2':
        return 4 * rad * rad * np.exp(-rad / (3 * bohr_radius)) / (81 * np.sqrt(30 * ((bohr_radius) ** 3)) * (bohr_radius ** 2))

def fY(th, ph):
    if orbital == 's0':
        return np.sqrt(1 / (4 * np.pi))
    elif orbital == 'p-1':
        return np.sqrt(3 / (8 * np.pi)) * np.sin(th) * np.exp(-ph * 1j)
    elif orbital == 'p0':
        return np.sqrt(3 / (4 * np.pi)) * np.cos(th)
    elif orbital == 'p1':
        return np.sqrt(3 / (8 * np.pi)) * np.sin(th) * np.exp(ph * 1j)
    elif orbital == 'd-2':
        return np.sqrt(5 / (32 * np.pi)) * np.sin(th) * np.sin(th) * np.exp(-2 * ph * 1j)
    elif orbital == 'd-1':
        return np.sqrt(5 / (8 * np.pi)) * np.cos(th) * np.sin(th) * np.exp(-ph * 1j)
    elif orbital == 'd0':
        return np.sqrt(5 / (16 * np.pi)) * (3 * (np.cos(th) ** 2) - 1)
    elif orbital == 'd1':
        return np.sqrt(5 / (8 * np.pi)) * np.cos(th) * np.sin(th) * np.exp(ph * 1j)
    elif orbital == 'd2':
        return np.sqrt(5 / (32 * np.pi)) * np.sin(th) * np.sin(th) * np.exp(2 * ph * 1j)
    
# def fR(rad):
#     if n == 1 and l == 0:
#         return 2 * np.exp(-rad / bohr_radius) * np.sqrt(1 / (bohr_radius ** 3))
#     elif n == 2 and l == 1:
#         return (rad / bohr_radius) * np.exp(-rad / (2 * bohr_radius)) * np.sqrt(3 * (2 * bohr_radius) ** 3)
#     elif n == 3 and l == 2:
#         return (((rad / bohr_radius) ** 2) * 4 / 27) * np.exp(-rad / (3 * bohr_radius)) * np.sqrt(10 * (3 * bohr_radius) ** 3)

# def fY(th, ph):
#     if n == 1 and l == 0:
#         if m == 0:
#             return (1 / 2) * np.sqrt(1 / np.pi)
#     elif n == 2 and l == 1:
#         if m == 0:
#             return (1 / 2 * np.cos(th)) * np.sqrt(3 / np.pi)
#         else:
#             return (- 1 / m * 1 / 2 * np.sin(th)) * np.sqrt(3 / (2 * np.pi)) * np.exp(m * 1j * ph)
#     elif n == 3 and l == 2:
#         if m == 0:
#             return (1 / 4 * (3 * (np.cos(th) ** 2) - 1)) * np.sqrt(5 / np.pi)
#         elif m == 1 or m == -1:
#             return (- 1 / m * 1 / 2 * np.sin(th) * np.cos(th)) * np.sqrt(15 / (2 * np.pi)) * np.exp(m * 1j * ph)
#         else:
#             return (1 / 4 * np.sin(th) * np.sin(th)) * np.sqrt(15 / (2 * np.pi)) * np.exp(m * 2j * ph)

def judge(r, th, ph):
    wf = fR(r) * fY(th, ph)
    dP = (wf ** 2)
    return (dP >= judgeRate), (wf >= 0)

r = np.linspace(0, 6, 10)
theta = np.linspace(0, 2 * np.pi, 50)
phi = np.linspace(0, 2 * np.pi, 50)

print(r)
print(theta)
print(phi)

Xp = []
Yp = []
Zp = []

Xm = []
Ym = []
Zm = []

while len(Xp) < 32000:
    judgeRate *= 0.9
    print("Judge Rate: " + str(judgeRate))
    for rad in r:
        for a in theta:
            for b in phi:
                res = judge(rad, a, b)
                if (res[0]):
                    if (res[1]):
                        Xp.append(rad * np.sin(a) * np.cos(b))
                        Yp.append(rad * np.sin(a) * np.sin(b))
                        Zp.append(rad * np.cos(a))
                    else:
                        Xm.append(rad * np.sin(a) * np.cos(b))
                        Ym.append(rad * np.sin(a) * np.sin(b))
                        Zm.append(rad * np.cos(a))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter3D(Xp, Yp, Zp, color = 'red')
ax.scatter3D(Xm, Ym, Zm, color = 'blue')
ax.set_box_aspect([1, 1, 1])

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

def animate(i):
    ax.view_init(elev=10, azim=i*4)
    return fig,

ani = animation.FuncAnimation(fig, animate, frames = 90, interval = 50, blit = True)
ani.save('./export/' + orbital + '.mp4', writer = 'ffmpeg', fps = 20)
