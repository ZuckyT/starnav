import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["figure.figsize"]=[7.00, 3.50]
plt.rcParams["figure.autolayout"]=True
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
r=0.5
u, v = np.mgrid[0:5, 0:np.pi:20j]
x = np.cos(u) * np.sin(v)
y = np.sin(u) * np.sin(v)
z = np.cos(v)
ax.plot_surface(x, y, z, cmap=plt.cm.YlGnBu_r)
plt.show()
