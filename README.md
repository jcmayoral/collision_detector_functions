# Python Libraries

This package contains python libraries useful for the master thesis proposal of Jose Mayoral Banos

## sensors

This folder stands for sensors drivers.

1. Adafruit_Python_ADXL345: Python driver for accelerometer model ADXL345 and arduino.
1. CollisionSensorTemplates: Provides the interfacing for Collision Detection Observers.

## statics

Provides a library with custom functionalities used for ploting Stochastic Measures.

###MyStatics
1. RealTimePlotter. A simple matplotlib interface to plot data on real time provided by a publisher.
1. GaussianPlotter. A simple matplotlib interface to plot gaussian distribution over a window of measures.

###MyKalmanFilter
A minimal Kalman Filter implementation interface

## Fault_Detection

Provides change detection functionalities.

1. BMC_CUSUM a modification of the BMC libraries for ChangeDetection.
1. ChangeDetection a CUSUM based algorithm for detecting changes



Directory Map
.
├── Fault_Detection
│   ├── FaultDetection
│   ├── testing
├── sensors
│   ├── accelerometer
│   │   └── Adafruit_Python_ADXL345
│   │       ├── Adafruit_ADXL345
│   │       └── examples
│   └── CollisionSensor
│       ├── CollisionSensorTemplates
└── statics
    ├── MyKalmanFilter
    ├── MyStatics
    └── testing

