# Author: Tony DiCola
# Modified: Jose Carlos Mayoral
# License: Public Domain
import time
import driver
import numpy as np

class MathAccelerometer:

   def __init__(self, seconds):
      print("MathAccelerometer Constructor")
      self.accel = driver.FaultAccelerometer()
      self.seconds = seconds

   def mean(self,data):
      return np.mean(data, axis=0)

   def variance(self,data):
      return np.var(data, axis=0)

   def plot(self):
      while True:
 	 samples = []
         for i in range(0,500):
             samples.append(self.accel.read())
         mean = self.mean(samples)
         variance = self.variance(samples)
         print('Mean Values X={0}, Y={1}, Z={2}'.format(mean[0], mean[1], mean[2]))
         print('Variance Values X={0}, Y={1}, Z={2}'.format(variance[0], variance[1], variance[2]))

   def changeDetection(self):
      print ('time in seconds ', self.accel.get_data_rate())
      
      while True:   	   
         samples = []
         timeout = time.time() + self.seconds / self.accel.get_data_rate()
	 while time.time() < timeout:
	    #print ('remaining ' , timeout - time.time())
	     samples.append(self.accel.read())
         mean = self.mean(samples)
         variance = self.variance(samples)
         print('Mean Values X={0}, Y={1}, Z={2}'.format(mean[0], mean[1], mean[2]))
         print('Variance Values X={0}, Y={1}, Z={2}'.format(variance[0], variance[1], variance[2]))

