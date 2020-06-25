#!/usr/bin/env python
#
#  Copyright 2020 [David Robert Wong]
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#  ********************
#  v0.1.0: drwnz (david.wong@tier4.jp)
#
#  ros_pointcloud_grabber.py
#
#  Created on: June 25th 2020
#

import rospy
from sensor_msgs.msg import PointCloud2
import sensor_msgs.point_cloud2 as point_cloud2
import numpy as np

pointcloud_topics = ["/filtered_points", "/points_raw/compare_map/filtered", "/points_raw/compare_map/outlier/filtered"]

topic_1 = []
topic_2 = []
topic_3 = []


def callback_1(data):
    cloud_points = list(point_cloud2.read_points(data, skip_nans=True, field_names = ("x", "y", "z", "intensity")))
    topic_1.append(cloud_points)

def callback_2(data):
    cloud_points = list(point_cloud2.read_points(data, skip_nans=True, field_names = ("x", "y", "z", "intensity")))
    topic_2.append(cloud_points)

def callback_3(data):
    cloud_points = list(point_cloud2.read_points(data, skip_nans=True, field_names = ("x", "y", "z", "intensity")))
    topic_3.append(cloud_points)

def write_out():
    np.save(pointcloud_topics[0].replace("/", "_"), np.array(topic_1))
    np.save(pointcloud_topics[1].replace("/", "_"), np.array(topic_2))
    np.save(pointcloud_topics[2].replace("/", "_"), np.array(topic_3))

    print topic_2

def listener():
    rospy.init_node('pointcloud_grabber', anonymous=True)
    rospy.Subscriber(pointcloud_topics[0], PointCloud2, callback_1)
    rospy.Subscriber(pointcloud_topics[1], PointCloud2, callback_2)
    rospy.Subscriber(pointcloud_topics[2], PointCloud2, callback_3)
    rospy.spin()

if __name__ == '__main__':
    listener()
    rospy.on_shutdown(write_out)
