#!/usr/bin/env python
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

#if __name__ is '__main__':
it = 100 #readings_number
realv=10 #true velocity

measurements = np.array([[10.1,1.0],[10.1,1.0],[10.1,1.0],[10.1,1.0],[10.1,1.0],[10.1,2.0],[10.1,1.0],[10.1,1.0],[15,1.0],[10.1,1.0],]) #measurements
measurements.shape = (10,2)

dt = 1

x = np.array([0,0,10,1.0]).reshape((4,1)) # Initial state
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

I = np.eye(4) # Identity Matrix
plot_list = list()

for m_i,m_j in measurements:
    x = np.dot(A,x) # Prediction State
    P = np.dot(A, np.dot(P,A.T)) + Q # Predicted Covariance
    Z =  np.array([m_i,m_j]).reshape(2,1)
    y = Z - (np.dot(H,x)) # Innovation Function
    S = np.dot(H, np.dot(P,H.T)) + R # Innovation Covariance
    K = np.dot(P, np.dot(H.T,np.linalg.inv(S))) #Kalman Gain
    plot_list.append(x.flatten())
    x = x + np.dot(K,y)
    P = (I-np.dot(K,H))*P

plt.plot(np.arange(0,10),plot_list)
plt.plot(np.arange(0,10),measurements)
plt.show()
