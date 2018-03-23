from __future__ import print_function
import rosbag
from geometry_msgs.msg import AccelStamped, Twist
from nav_msgs.msg import Odometry
from sensor_msgs.msg import Image, LaserScan
import rospy
import sys

class MyBagReader():
    def __init__(self,file_name):
        mytypes = [AccelStamped, Twist, Odometry, Odometry, LaserScan, LaserScan, LaserScan, Image, Image]
        self.mytopics = ["/accel", "/cmd_vel", "/odom", "/base/odometry_controller/odom",
            "/scan_front", "/scan_rear", "/scan_unified",
            "/arm_cam3d/rgb/image_raw","/cam3d/rgb/image_raw"]

        self.myPublishers = list()

        for topic_name, msg_type in zip(self.mytopics,mytypes):
            publisher = rospy.Publisher(topic_name, msg_type, queue_size=1)
            self.myPublishers.append([publisher,topic_name])

        self.bag = rosbag.Bag(file_name)

    def read(self):
        start_time = self.bag.get_start_time()
        end_time = self.bag.get_end_time()
        duration_time = end_time - start_time
        r = rospy.Rate(100)

        for topic, msg, t in self.bag.read_messages(topics=self.mytopics):
            print ("ROSBag  Running ", t.to_sec() - start_time, " of " , duration_time, end="\r")
            for p, topic_name in self.myPublishers:
                if topic_name == topic:
                    #print "printing on ", topic_name
                    p.publish(msg)
                    r.sleep()
                    break
        self.bag.close()

rospy.init_node("my_bag_reader")
file_name = '/home/jose/ROS/thesis_ws/my_ws/src/mas_thesis_ws/scripts/test.bag'

if len(sys.argv) > 1:
  file_name=str(sys.argv[1])

bagReader = MyBagReader(file_name)
bagReader.read()
