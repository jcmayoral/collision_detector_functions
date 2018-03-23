#!/usr/bin/env python
from __future__ import division
import matplotlib.pyplot as plt
import numpy as np

def update(mean1,var1,mean2,var2):
   new_mean = (var2*mean1 + var1*mean2)/(var1+var2)
   new_var = 1/(1/var1 + 1/var2)
   return [new_mean, new_var]

def predict(mean1,var1,mean2,var2):
   new_mean = mean1 + mean2
   new_var = var1 + var2
   return [new_mean, new_var]


#if __name__ is '__main__':
sigma_mess = 4
sigma_move = 2

measurements = np.array([5,6,7,9,10])
motion = np.array([1,1,2,1,1])

#Initial values
mu = 0
sig = 1000
x = 0
predict_mean = np.array([0,0])
predict_var = np.array([0,0])
update_mean = np.array([0,0])
update_var = np.array([0,0])

for i,j in zip(measurements,motion):
    mu,sig = predict (mu,sig,j,sigma_move)
    predict_mean = np.append(predict_mean, [x,mu])
    predict_var = np.append(predict_var, [x,sig])
    print ("predict " , mu , sig) 
    mu,sig = update (mu,sig,i,sigma_mess)
    update_mean = np.append(predict_mean, [x,mu])
    update_var = np.append(predict_var, [x,sig])
    print ("update " , mu , sig) 
    x = x + 1


plt.figure()
plt.plot(predict_mean, label='Predict Mean')
plt.plot(update_mean, label='Update Mean')
plt.legend()

plt.figure()
plt.plot(predict_var, label='Predict Sigma')
plt.plot(update_var, label='Update Sigma')
plt.legend()
plt.show()
