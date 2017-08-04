# Author: Tony DiCola
# Modified: Jose Carlos Mayoral
# License: Public Domain
import time
from datetime import datetime
import numpy as np

class ChangeDetection:

    def __init__(self, seconds):
        self.seconds = seconds
        self.cum_sum = np.array([0.0,0.0,0.0])
        self.last_mean = np.array([0,0,0])
        self.last_variance = np.array([1,1,1])
        self.samples = []

    def addData(self,data):
        self.samples.append(data)

    def mean(self,data):
        return np.mean(data, axis=0)

    def variance(self,data):
        return np.var(data, axis=0)

    def changeDetection(self,limit):
        expected_mean = self.last_mean
        expected_variance = self.last_variance
        mean = self.mean(self.samples[:limit])
        variance = self.variance(self.samples[:limit])
        self.CUSUM(self.samples[:limit],mean,variance, expected_mean, expected_variance)
        self.last_mean = mean
        self.last_variance = variance

    def CUSUM(self, data, mean, var, e_mean, e_var):
        array = np.array(data)
        s_z_sum = self.meanChange(array, mean, var, e_mean)
        self.cum_sum = np.sum(s_z_sum, axis=0)

    def meanChange(self,z, m1, v1, m0):
        ### BLANKE
        #s_z = (-np.power(z-m1,2) + np.power(z-m0,2))/(2*v1)
        s_z = ((m1-m0)/v1) * (z-((m0+m1)/2))
        ##ORIGINAL
        #diff = (m0-m1)#/np.power(v1,2)
        #m0m1 = (m0+m1)/2
        #s_z = (z  - m0m1)/np.sqrt(v1)
        return s_z
