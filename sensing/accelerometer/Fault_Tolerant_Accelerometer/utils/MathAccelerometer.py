# Author: Tony DiCola
# Modified: Jose Carlos Mayoral
# License: Public Domain
import time
import matplotlib 
matplotlib.use('Agg')
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
#from datetime import datetime
import driver
import numpy as np

class MathAccelerometer:

    def __init__(self, seconds):
        print("MathAccelerometer Constructor")
        self.accel = driver.FaultAccelerometer()
        self.seconds = seconds
        self.cum_sum = np.array([0,0,0])
        self.fig = plt.figure()

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
        print ('time in seconds ', self.seconds)
        expected_mean = [2,2,2]
        expected_variance = [1,1,1]

        while True:   	   
            samples = []
            timeout = time.time() + self.seconds
            #timeout = datetime.now() + self.seconds / 1000
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
        print ('Gaussian Probability Density Function Mean ' , likelihood)
        s_z = np.array(s_z)
        print ('log-likelihood ratio', s_z)
        self.cum_sum = np.sum([self.cum_sum,s_z],axis=0)
        print ('Cumulative ', self.cum_sum)
        plt.plot(likelihood)
        plt.show()
        plt.savefig('p1.png') 
  
    def meanGaussianSequence(self,z, m1, v1, m0):
        likelihood_ratio = []
        s_z = []

        for i in range(0,3):
            likelihood_ratio.append(-(np.power((z[:,i]- m1[i]),2) + np.power((z[:,i]- m0[i]),2))/(2*v1[i]))
            s_z.append(((m1[i]-m0[i]) /v1[i])* (z[-1,i] - ((m0[i]+m1[i])/2)))

        likelihood = np.exp(likelihood_ratio)
        return likelihood_ratio, s_z
