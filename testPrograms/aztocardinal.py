from __future__ import print_function, division
from PyAstronomy import pyasl
import numpy as np

# Get the cardinal point for 10 azimuth angles
azimuths = np.random.random(10) * 360.
for azimuth in azimuths:
  cp = pyasl.getCardinalPoint(azimuth)
  print("Azimuth: {0:6.2f} deg, Cardinal point: {1:1s}".format(azimuth, cp))
