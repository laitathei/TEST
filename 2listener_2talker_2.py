#!/usr/bin/env python

import rospy
from std_msgs.msg import String, Duration
import message_filters
from message_filters import TimeSynchronizer, Subscriber, Cache


def callback_3(data):
	rospy.loginfo(' I am listener 3 and I heard %s' % data.data)

def callback_4(data):
	rospy.loginfo(' I am listener 4 and I heard %s' % data.data)

def part():
	pub = rospy.Publisher('chat_3', String, queue_size=30)
	pub = rospy.Publisher('chat_4', String, queue_size=30)

	while not rospy.is_shutdown():

		hello = 'I am talker 3! ' 
		pub.publish(hello)
		rospy.loginfo(hello)

		rospy.sleep(rospy.Duration(1))

		rospy.Subscriber('chat', String, callback_4)
		sub = message_filters.Subscriber('chat', String)
		cache = message_filters.Cache(sub, 1, allow_headerless=True)
		cache.registerCallback(callback_3)

		hello2 = 'I am talker 4! ' 
		pub.publish(hello2)
		rospy.loginfo(hello2)

		rospy.sleep(rospy.Duration(1.1))

		rospy.Subscriber('chat_2', String, callback_3)
		sub2 = message_filters.Subscriber('chat_2', String)
		cache2 = message_filters.Cache(sub2, 1, allow_headerless=True)
		cache2.registerCallback(callback_4)


if __name__ == '__main__':

		rospy.init_node('node_2', anonymous=True)
		part()
		rospy.spin()

