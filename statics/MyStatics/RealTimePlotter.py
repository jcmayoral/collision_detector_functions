import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

class RealTimePlotter:
    def __init__(self, max_samples = 1000, pace = 200):
        self.max_samples = max_samples
        self.f = plt.figure()
        self.ax = plt.axes()
        self.ax.set_title('Results')
        self.ax.legend("True")
        self.pace_ = pace
        plt.gca().set_color_cycle(['red', 'green', 'blue'])
        print ("RealTimePlotter Constructor Initialized")


    def update(self,seq,x,y):
        if seq % self.pace_ is 0:
            plotObject = self.ax.plot(x,y)
            plt.legend(iter(plotObject), ('x', 'y', 'z'))
            plt.draw()

        if len(x) >= self.max_samples:
            x.pop(0)
            y.pop(0)
            self.ax.cla()
