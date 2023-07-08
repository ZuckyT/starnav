import numpy as np
import matplotlib.pyplot as plt

ax = plt.subplot(111, projection = 'polar')
radius=90

ax.plot(260, 70.26, 'g.')
#plt.polar(100, 70.26, 'g.')
#plt.polar(130, 70.26, 'g.')
#plt.polar(0.785398, 45, 'r.')
#plt.polar(0.872851, 45, 'b.')
ax.plot(1.5708, 45, 'y.')
ax.set_rmax(90)
ax.set_facecolor('#000000')
plt.show()
