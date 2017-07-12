# Author: Tony DiCola
# Modified: Jose Carlos Mayoral
# License: Public Domain
import time
import matplotlib
matplotlib.use('Agg')
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np

class ChangeDetection:

    def __init__(self, seconds):
        #print("MathAccelerometer Constructor")
        self.seconds = seconds
        self.cum_sum = np.array([0,0,0])
        self.samples = []
        #self.fig = plt.figure()

    def addData(self,data):
        self.z_i = data
        self.samples.append(self.z_i)
        #self.changeDetection()

    def mean(self,data):
        return np.mean(data, axis=0)

    def variance(self,data):
        return np.var(data, axis=0)

    def changeDetection(self):
        #print ('time in seconds ', self.seconds)
        expected_mean = np.array([2,2,250])
        expected_variance = np.array([1,1,1])       
        mean = self.mean(self.samples)
        variance = self.variance(self.samples)
        self.CUSUM(self.samples,mean,variance, expected_mean, expected_variance)

    def CUSUM(self, data, mean, var, e_mean, e_var):
        array = np.array(data)
        s_z = self.meanGaussianSequence(array, mean, var, e_mean)

        if not np.isinf(s_z).any():
            self.cum_sum = np.sum([self.cum_sum,s_z],axis=0)

    def meanGaussianSequence(self,z, m1, v1, m0):
        constants = (m0-m1)/np.power(v1,2)
        m0m1 = (m0+m1)/2
        s_z = constants * (z  - m0m1)
        return s_z
