<<<<<<< HEAD
# TEST
=======
## Task for the publisher and subscriber

#### The above task just for 2 publisher and 2 subscriber in each files to communicate to others. If you want extend it to N publisher and N subscriber, just take this as reference.

## Environment setup

#### Setup the python environment
```
#!/usr/bin/env python 	
```

#### Import the ROS python library
```
import rospy 
```

#### Enable to use string and duration
```
from std_msgs.msg import String, Duration
```

#### Import the message_filters library
```
import message_filters
```

#### Enable to use following functions
```
from message_filters import TimeSynchronizer, Subscriber, Cache
```

## Code explanation (see the remark)

```
def callback(data): 	//(def in python is similiar to C++ function) (callback(data) function names and define variable type)
	rospy.loginfo(' I am listener 1 and I heard %s' % data.data) 	//(print the message and show the message which is from the topic)

def callback_2(data):
	rospy.loginfo(' I am listener 2 and I heard %s' % data.data)

def part():
	pub = rospy.Publisher('chat', String, queue_size=30)		//(define the publisher)(which topic want to publish)(publisher size)(publisher what type of variable)
	pub = rospy.Publisher('chat_2', String, queue_size=30)	

	while not rospy.is_shutdown():		//(similiar to C++ while(1) )

		hello = 'I am talker 1! ' 	//(message content)
		pub.publish(hello)		//(publish the message to topic)
		rospy.loginfo(hello)		//(print it out)

		rospy.sleep(rospy.Duration(1))	//(wait 1 sec so that it can be observe easily)

		rospy.Subscriber('chat_3', String, callback_2)		//(subscribe the what topic, setup variable type, call the callback function after subscribe successfully)
		sub = message_filters.Subscriber('chat_3', String)	//(use message_filter to subscribe the topic)
		cache = message_filters.Cache(sub, 1, allow_headerless=True)		//(setup space to store the message)(get data from sub instruction)(use time stamp provided by ROS real time)
		cache.registerCallback(callback)			//(release the data stored in the space)

		hello2 = 'I am talker 2! ' 
		pub.publish(hello2)
		rospy.loginfo(hello2)

		rospy.sleep(rospy.Duration(1.1))

		rospy.Subscriber('chat_4', String, callback)
		sub2 = message_filters.Subscriber('chat_4', String)
		cache2 = message_filters.Cache(sub2, 1, allow_headerless=True)
		cache2.registerCallback(callback_2)



if __name__ == '__main__':		//(main function)

		rospy.init_node('node', anonymous=True)		//(set node name and which ones can access)
		part()			//(call part function)
		rospy.spin()		//(wait until finish part function)

```

#Result
![Result](/image/2_pub_and_2_su.jpeg "Result")



