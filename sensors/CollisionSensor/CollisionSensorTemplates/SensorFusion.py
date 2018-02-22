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
    def __init__(self, number_elements = 3, window_size = 10, frame="base_link", sensor_id="accel1",
                       threshold = 60, node = "sensor_node", sensor_type = AccelStamped,
                       topic_name = "accel", sensor_number = 0, config_type = accelerometerConfig):
        self.setup(window_size, frame, threshold, sensor_id)
        ChangeDetection.__init__(self, number_elements)
        rospy.init_node(node, anonymous=False)
        self.sensor_number = rospy.get_param("~sensor_number", 0)
        self.sensor_id = rospy.get_param("~sensor_id", sensor_id)
        self.subscriber_ = rospy.Subscriber(topic_name, sensor_type, self.sensorCB)

        self.pub = rospy.Publisher('collisions_'+ str(sensor_number), sensorFusionMsg, queue_size=10)
        self.dyn_reconfigure_srv = Server(config_type, self.dynamic_reconfigureCB)
        rospy.loginfo(sensor_id + " sensor Ready for Fusion")
        rospy.spin()

    def setup(self, window_size, frame, threshold, sensor_id):
        self.i = 0
        self.msg = 0
        self.is_over_lapping_required = False
        self.window_size = window_size
        self.frame = frame
        self.threshold = threshold
        self.sensor_id = sensor_id
        self.weight = 1.0
        self.is_disable = False

    def reset_publisher(self):
        self.pub = rospy.Publisher('collisions_'+ str(self.sensor_number), sensorFusionMsg, queue_size=10)

    def dynamic_reconfigureCB(self,config, level):
        self.threshold = config["threshold"]
        self.window_size = config["window_size"]
        self.weight = config["weight"]
        self.is_disable = config["is_disable"]
        self.sensor_number = config["detector_id"]
        self.reset_publisher()

        if config["reset"]:
            self.clear_values()
            config["reset"] = False
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

        #self.addData(self.current_measure)

        if self.is_over_lapping_required:

            self.addData(self.current_measure)

            if len(self.samples) > self.window_size:
                self.samples.pop(0)

        else:

            if ( self.i < self.window_size) and len(self.samples) < self.window_size:
                self.addData(self.current_measure)
                self.i = self.i+1
            else:
                self.samples.pop(0)
                return

        self.i =0

        self.changeDetection(len(self.samples))
        cur = np.array(self.cum_sum, dtype = object)

        if not self.is_disable:
            self.publishMsg(cur) # publishMsg

        self.doPostProcessing()
