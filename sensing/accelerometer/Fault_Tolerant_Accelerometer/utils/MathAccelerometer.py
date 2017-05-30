# Author: Tony DiCola
# Modified: Jose Carlos Mayoral
# License: Public Domain
import time
import driver

class MathAccelerometer:
   def __init__(self):
      print("MathAccelerometer Constructor")
      self.accel = driver.FaultAccelerometer()
   def plot(self):
      print('Printing X, Y, Z axis values, press Ctrl-C to quit...')
      while True:
         # Read the X, Y, Z axis acceleration values and print them.
         x, y, z = self.accel.read()
         print('X={0}, Y={1}, Z={2}'.format(x, y, z))
         # Wait half a second and repeat.
         time.sleep(0.5)
