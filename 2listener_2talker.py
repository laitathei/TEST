#!/usr/bin/env python

import rospy
from std_msgs.msg import String, Duration
import message_filters
from message_filters import TimeSynchronizer, Subscriber, Cache


def callback(data):
	rospy.loginfo(' I am listener 1 and I heard %s' % data.data)

def callback_2(data):
	rospy.loginfo(' I am listener 2 and I heard %s' % data.data)

def part():
	pub = rospy.Publisher('chat', String, queue_size=30)
	pub = rospy.Publisher('chat_2', String, queue_size=30)

	while not rospy.is_shutdown():

		hello = 'I am talker 1! ' 
		pub.publish(hello)
		rospy.loginfo(hello)

		rospy.sleep(rospy.Duration(1))

		rospy.Subscriber('chat_3', String, callback_2)
		sub = message_filters.Subscriber('chat_3', String)
		cache = message_filters.Cache(sub, 1, allow_headerless=True)
		cache.registerCallback(callback)

		hello2 = 'I am talker 2! ' 
		pub.publish(hello2)
		rospy.loginfo(hello2)

		rospy.sleep(rospy.Duration(1.1))

		rospy.Subscriber('chat_4', String, callback)
		sub2 = message_filters.Subscriber('chat_4', String)
		cache2 = message_filters.Cache(sub2, 1, allow_headerless=True)
		cache2.registerCallback(callback_2)



if __name__ == '__main__':

		rospy.init_node('node', anonymous=True)
		part()
		rospy.spin()


