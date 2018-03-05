# Author: Tony DiCola
# Modified: Jose Carlos Mayoral
# License: Public Domain
import time
from datetime import datetime
from MyStatics.GaussianPlotter import GaussPlot
import numpy as np

class ChangeDetection:

    def __init__(self, length = 3, factor = 1):
        self.cum_sum = np.zeros(length) * factor
        #self.cum_sum = np.array([0.0,0.0,0.0])
        self.last_mean = np.ones(length) * factor
        #self.last_mean = np.array([0,0,0])
        self.last_variance = np.ones(length) * factor
        #self.last_variance = np.array([1,1,1])
        self.samples = []
        self.s_z =[]

    def clear_values(self):
        self.cum_sum.fill(0)
        #self.cum_sum = np.array([0.0,0.0,0.0])
        self.last_mean.fill(1)
        #self.last_mean = np.array([0,0,0])
        self.last_variance.fill(1)
        #self.last_variance = np.array([1,1,1])
        self.samples = []
        self.s_z = []

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

    def CUSUM(self, data, m1, v1, m0, v0):
        array = np.array(data)
        #MEAN
        #s_z_sum = self.meanChange(array, mean, var, e_mean)
        #variance
        self.varianceChange(array, m1, v1, v0)
        self.cum_sum = np.sum(self.s_z, axis=0)

    def meanChange(self,z, m1, v1, m0):
        ### BLANKE
        #s_z = (-np.power(z-m1,2) + np.power(z-m0,2))/(2*v1)
        self.s_z = ((m1-m0)/v1) * (z-((m0+m1)/2))
        ##ORIGINAL
        #diff = (m0-m1)#/np.power(v1,2)
        #m0m1 = (m0+m1)/2
        #s_z = (z  - m0m1)/np.sqrt(v1)

    def varianceChange(self,z, m1, v1, v0):
        ### BLANKE
        #s_z = (-np.power(z-m1,2) + np.power(z-m0,2))/(2*v1)
        std_0 = np.sqrt(v0)
        std_1 = np.sqrt(v1)
        diff = ((1/v0) - (1/v1))
        self.s_z = np.log(std_0/std_1) + ((np.power(z-m1,2)/2) * diff)
