import rosbag
import rospy
from geometry_msgs.msg import AccelStamped, Twist
from nav_msgs.msg import Odometry
from sensor_msgs.msg import Image, LaserScan
import sys

class MyBagRecorder():
    def __init__(self,file_name):
        self.busy = False
        self.bag = rosbag.Bag(file_name +'.bag', 'w')
        rospy.Subscriber("/accel", AccelStamped, self.mainCB, "/accel")
        rospy.Subscriber("/cmd_vel", Twist, self.mainCB, "/cmd_vel")
        rospy.Subscriber("/base/twist_mux/command_navigation", Twist, self.mainCB, "/base/twist_mux/command_navigation")
        rospy.Subscriber("/odom", Odometry, self.mainCB, "/odom")
        rospy.Subscriber("/base/odometry_controller/odometry", Odometry, self.mainCB, "/base/odometry_controller/odometry")
        rospy.Subscriber("/scan_front", LaserScan, self.mainCB, "/scan_front")
        rospy.Subscriber("/scan_rear", LaserScan, self.mainCB, "/scan_rear")
        rospy.Subscriber("/scan_unified", LaserScan, self.mainCB, "/scan_unified")
        rospy.Subscriber("/arm_cam3d/rgb/image_raw", Image, self.mainCB, "/arm_cam3d/rgb/image_raw")
        rospy.Subscriber("/cam3d/rgb/image_raw", Image, self.mainCB, "/cam3d/rgb/image_raw")
        rospy.loginfo("Initializing")

    def writeToBag(self,topic, msgs):
        while (self.busy is True):
            pass
        self.busy = True
        self.bag.write(topic, msgs)
        self.busy = False

    def mainCB(self,msg, topic_name):
        self.writeToBag(topic_name, msg)

    def close(self):
        rospy.loginfo("Closing Bag File")
        self.bag.close()

rospy.init_node("my_bag_recorder")

file_name = 'test'

if len(sys.argv) > 1:
  file_name=str(sys.argv[1])

bagRecord = MyBagRecorder(file_name)

while not rospy.is_shutdown():
    rospy.spin()

bagRecord.close()
