import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np
import math

class GaussPlot:
    def __init__(self):
        print ("GaussiPlotter Constructor Initialized")

    def call(self,data,mu,variance):
        sigma = np.sqrt(variance)
        #plotObject = self.ax.plot(data,mlab.normpdf(data, mu, sigma))
        #initialize a normal distribution with frozen in mean=-1, std. dev.= 1
        print ("sigma", sigma)
        self.rv = []
        for i in range(len(sigma)):
            self.rv.append(norm(loc = mu[i], scale = sigma[i]))
        self.x = np.arange(-10, 10, .1)
        #plot the pdfs of these normal distributions
        #plt.plot(x, rv.pdf(x), x, rv1.pdf(x), x, rv2.pdf(x))
