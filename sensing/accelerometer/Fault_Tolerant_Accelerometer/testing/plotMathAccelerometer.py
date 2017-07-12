# Author: Tony DiCola
# Modified: Jose Carlos Mayoral
# License: Public Domain
import time
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import utils
import numpy as np
# Create an ADXL345 instance.
accel = utils.MathAccelerometer(10000) # seconds
#accel.plot()
x = accel.changeDetection()
plt.plot(x, np.arange(0,len(x)))
plt.savefig('jose.png')
print (x)
