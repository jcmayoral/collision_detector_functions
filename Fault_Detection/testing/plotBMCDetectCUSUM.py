import FaultDetection.BMC_CUSUM as bmc

data = []
data.append([2.1,1,1])
data.append([2.2,3,2])
data.append([2.1,1,3])
data.append([2.2,3,4])
data.append([2,1,5])
data.append([2,3,6])
data.append([2,1,7])
data.append([4,9,10])
data.append([2,1,20])
bmc.detect_cusum(data, 4, 1.5, False, True)
