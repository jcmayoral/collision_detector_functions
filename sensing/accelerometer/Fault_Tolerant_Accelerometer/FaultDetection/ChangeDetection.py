# Author: Tony DiCola
# Modified: Jose Carlos Mayoral
# License: Public Domain
import time
from datetime import datetime
import numpy as np

class ChangeDetection:

    def __init__(self, seconds):
        self.seconds = seconds
        self.cum_sum = np.array([0,0,0])
        self.last_mean = np.array([20,20,20])
        self.last_variance = np.array([1,1,1])
        self.samples = []

    def addData(self,data):
        self.samples.append(data)

    def mean(self,data):
        return np.mean(data, axis=0)

    def variance(self,data):
        return np.var(data, axis=0)

    def changeDetection(self):
        expected_mean = self.last_mean
        expected_variance = self.last_variance
        mean = self.mean(self.samples)
        variance = self.variance(self.samples)
        self.CUSUM(self.samples,mean,variance, expected_mean, expected_variance)
        self.last_mean = mean
        self.last_variance = variance

    def CUSUM(self, data, mean, var, e_mean, e_var):
        array = np.array(data)
        s_z_sum = self.meanGaussianSequence(array, mean, var, e_mean)
        self.cum_sum = np.sum(s_z_sum, axis=0)
        #self.cum_sum = np.sum([self.cum_sum,s_z_sum],axis=0)

    def meanGaussianSequence(self,z, m1, v1, m0):
        constants = (m0-m1)/np.power(v1,2)
        m0m1 = (m0+m1)/2
        s_z = constants * (z  - m0m1)
        return s_z
