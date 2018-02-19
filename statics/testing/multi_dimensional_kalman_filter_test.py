#!/usr/bin/env python
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from MyKalmanFilter.SimpleKalmanFilter import SimpleKalmanFilter

measurements = np.array([[10.1,1.0],[10.1,1.0],[10.1,1.0],[10.1,1.0],[10.1,1.0],[10.1,2.0],[10.1,1.0],[10.1,1.0],[15,1.0],[10.1,1.0],]) #measurements
measurements.shape = (10,2)

dt = 1
x = np.array([0,0,10,0]).reshape((4,1)) # Initial state
P = np.eye(4) * 10 # Initial Uncertanty
A = np.eye(4) # Transition Matrix
A[0,2] = dt
A[1,3] = dt

H = np.array(([0,0,1,0],[0,0,0,1])) # Measurement Function
R = np.array(([10,0],[0,10])) # measurement noise covariance
Q = np.array(([1/4*np.power(dt,4), 1/4*np.power(dt,4),1/2*np.power(dt,3), 1/2*np.power(dt,3)],
	      [1/4*np.power(dt,4), 1/4*np.power(dt,4),1/2*np.power(dt,3), 1/2*np.power(dt,3)],
	      [1/2*np.power(dt,3), 1/2*np.power(dt,3), np.power(dt,2), np.power(dt,2)],
	      [1/2*np.power(dt,3), 1/2*np.power(dt,3), np.power(dt,2), np.power(dt,2)])) # Process Noise Covariance

kalman_filter_ = SimpleKalmanFilter(x, A, H, R, Q, dt=1, size =4)

plot_list = list()

for m_i,m_j in measurements:
    Z =  np.array([m_i,m_j]).reshape(2,1)
    kalman_filter_.runFilter(Z)
    plot_list.append(kalman_filter_.getInnovationFunction().flatten())

print plot_list
plt.plot(np.arange(0,10),plot_list)
plt.show()
