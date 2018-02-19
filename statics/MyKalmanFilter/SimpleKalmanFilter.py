#!/usr/bin/env python
from __future__ import division
import numpy as np

class SimpleKalmanFilter:
	def __init__(self, initial_state, transition_matrix, obs_model, noise_cov, process_noise, dt=1, size =4):
		self.__x = initial_state.reshape((size,1))
		self.__P = np.eye(size)
		self.__A = transition_matrix
		self.__H = obs_model
		self.__R = noise_cov
		self.__Q = process_noise
		self.__I = np.eye(size)
		self.__dt = dt

	def setTransitionMatrix(self, transition_matrix):
		self.__A = transition_matrix

	def setPredictedCovariance(self, predicted_cov):
		self.__P = predicted_cov

	def setObservationModel(self, obs_model):
		self.__H = obs_model

	def setNoiseCovariance(self,noise_cov):
		self.__R = noise_cov

	def setProcessNoise(self,process_noise):
		self.__Q = process_noise

	def getInnovationFunction(self):
		return self.__y

	def runFilter(self, Z):
		self.__x = np.dot(self.__A,self.__x) # Prediction State
		self.__P = np.dot(self.__A, np.dot(self.__P,self.__A.T)) + self.__Q # Predicted Covariance
		#Z =  np.array([m_i,m_j]).reshape(2,1)
		self.__y = Z - (np.dot(self.__H, self.__x)) # Innovation Function
		self.__S = np.dot(self.__H, np.dot(self.__P,self.__H.T)) + self.__R # Innovation Covariance
		self.__K = np.dot(self.__P, np.dot(self.__H.T,np.linalg.inv(self.__S))) #Kalman Gain
		self.__x = self.__x + np.dot(self.__K,self.__y)
		self.__P = np.dot((self.__I-np.dot(self.__K,self.__H)),self.__P)
