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
      self.cum_sum = 0

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
      expected_mean = [2,2,]
      expected_variance = [1,1,1]
      
      while True:   	   
         samples = []
         timeout = time.time() + self.seconds / self.accel.get_data_rate()
	 while time.time() < timeout:
	    #print ('remaining ' , timeout - time.time())
	     samples.append(self.accel.read())
         mean = self.mean(samples)
         variance = self.variance(samples)
         self.CUSUM(samples,mean,variance, expected_mean, expected_variance)
         #print('Mean Values X={0}, Y={1}, Z={2}'.format(mean[0], mean[1], mean[2]))
         #print('Variance Values X={0}, Y={1}, Z={2}'.format(variance[0], variance[1], variance[2]))

   def CUSUM(self, data, mean, var, e_mean, e_var):
      array = np.array(data)
      likelihood,s_z = self.meanGaussianSequence(array, mean, var, e_mean)
      print ('Gaussian Probability Density Function ' , likelihood)
      print ('log-likelihood ratio', s_z)

   def meanGaussianSequence(self,z, m1, v1, m0):
      likelihood = []
      s_z = []
      for i in range(0,3):
         likelihood.append((np.power(-z[-1,i]- m1[i],2) + np.power(-z[-1,i]- m0[i],2))/(2*v1[i]))
         s_z.append(((m1[i]-m0[i]) /v1[i])* (z[-1,i] - ((m0[i]+m1[i])/2)))

      likelihood = np.exp(likelihood)
      
      return likelihood, s_z
