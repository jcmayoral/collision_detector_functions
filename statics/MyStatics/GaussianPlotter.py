import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
import math

class GaussPlot:
    def __init__(self):
        self.f = plt.figure()
        self.ax = plt.axes()
        self.ax.set_title('Gaussian Bell')
        self.ax.legend("True")
        plt.gca().set_color_cycle(['red', 'green', 'blue'])
        plt.show()
        print ("GaussiPlotter Constructor Initialized")

    def call(self,data,mu,variance):
        sigma = np.sqrt(variance)
        plotObject = self.ax.plot(data,mlab.normpdf(data, mu, sigma))
