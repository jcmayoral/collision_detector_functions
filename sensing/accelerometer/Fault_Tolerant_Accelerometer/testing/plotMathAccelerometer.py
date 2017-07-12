# Author: Tony DiCola
# Modified: Jose Carlos Mayoral
# License: Public Domain
import time
import matplotlib.pyplot as plt
import FaultDetection
import numpy as np
# Create an ADXL345 instance.
accel = FaultDetection.ChangeDetection(10) # seconds
#accel.plot()
accel.addData([2,1,6])
accel.addData([2,3,6])
accel.addData([2,1,6])
accel.addData([2,3,6])
accel.addData([2,1,6])
accel.addData([2,5,6])
accel.addData([2,1,6])
accel.addData([4,9,10])
accel.addData([2,1,6])
accel.changeDetection()
print ("aaaa")
plt.plot(accel.samples)
plt.show()
