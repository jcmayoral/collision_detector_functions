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
accel.addData([2.1,1,1])
accel.addData([2.2,3,2])
accel.addData([3.1,1,3])
accel.addData([4.2,3,4])
accel.addData([3,1,5])
accel.addData([1,3,6])
accel.addData([2,1,7])
accel.addData([4,9,10])
accel.addData([2,1,20])

plot_data = []
print(len(accel.samples))
for x in range(1,len(accel.samples)+1):
    accel.changeDetection(x)
    print (accel.samples[:x])
    plot_data.append(accel.cum_sum)

x = np.arange(len(plot_data))
plt.figure()
plt.plot(plot_data)
plt.legend()
plt.figure()
plt.plot(accel.samples)
plt.show()
