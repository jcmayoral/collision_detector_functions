import rospy
from FaultDetection import ChangeDetection
from geometry_msgs.msg import AccelStamped
from sensor_msgs.msg import Imu
from fusion_msgs.msg import sensorFusionMsg
import numpy as np

# For PCA
from sklearn.decomposition import PCA

#Dynamic Reconfigure
from dynamic_reconfigure.server import Server
from accelerometer_ros.cfg import accelerometerConfig


class CollisionFusionSensor(ChangeDetection):
    def __init__(self, window_size = 10, frame="base_link", sensor_id="accel1",
                       threshold = 60, node = "sensor_node", sensor_type = AccelStamped,
                       topic_name = "accel", sensor_number = 0, config_type = accelerometerConfig):
        self.setup(window_size, frame, threshold, sensor_id)
        ChangeDetection.__init__(self)
        rospy.init_node(node, anonymous=False)
        rospy.Subscriber(topic_name, sensor_type, self.sensorCB)
        sensor_number = rospy.get_param("~sensor_number", 0)
        self.sensor_id = rospy.get_param("~sensor_id", sensor_id)
        self.pub = rospy.Publisher('collisions_'+ str(sensor_number), sensorFusionMsg, queue_size=10)
        self.dyn_reconfigure_srv = Server(config_type, self.dynamic_reconfigureCB)
        rospy.loginfo(sensor_id + " sensor Ready for Fusion")
        rospy.spin()

    def setup(self, window_size, frame, threshold, sensor_id):
        self.i = 0
        self.msg = 0
        self.window_size = window_size
        self.frame = frame
        self.threshold = threshold
        self.sensor_id = sensor_id
        self.weight = 1.0

    def dynamic_reconfigureCB(self,config, level):
        self.threshold = config["threshold"]
        self.window_size = config["window_size"]
        self.weight = config["weight"]

        if config["reset"]:
            self.clear_values()
            config["rest"] = False
        return config

    def updateData(self,msg): # To Override
        self.current_measure = np.zeros(3)

    def doPostProcessing(self):
        pass

    def publishMsg(self,data):
        output_msg = sensorFusionMsg()
        #Filling Message
        output_msg.header.frame_id = self.frame
        output_msg.window_size = self.window_size
        #print ("Accelerations " , x,y,z)

        if any(t > self.threshold for t in data):
            output_msg.msg = sensorFusionMsg.ERROR

        output_msg.header.stamp = rospy.Time.now()
        output_msg.sensor_id.data = self.sensor_id
        output_msg.data = data
        output_msg.weight = self.weight
        self.pub.publish(output_msg)


    def sensorCB(self, msg):

        self.updateData(msg)

        while (self.i< self.window_size):
            self.addData(self.current_measure)
            self.i = self.i+1
            if len(self.samples) is self.window_size:
                self.samples.pop(0)
            return

        self.i=0

        self.changeDetection(len(self.samples))
        cur = np.array(self.cum_sum, dtype = object)
        self.publishMsg(cur) # publishMsg

        self.doPostProcessing()
