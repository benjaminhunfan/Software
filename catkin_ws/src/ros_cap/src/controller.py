#!/usr/bin/env python

import rospy #importar ros para python
from std_msgs.msg import String, Int32 # importar mensajes de ROS tipo String y tipo Int32
from geometry_msgs.msg import Twist # importar mensajes de ROS tipo geometry / Twist
from sensor_msgs.msg import Joy
from duckietown_msgs.msg import Twist2DStamped

class Controller(object):
	def __init__(self, args):
		super(Controller, self).__init__()
		self.args = args
		self.subscriber = rospy.Subscriber("/duckiebot/joy", Joy, self.callback)
		self.publisher = rospy.Publisher("/duckiebot/wheels_driver_node/car_cmd", Twist2DStamped, queue_size=10)

	#def publicar(self):
	#def callback(self,msg):
	def callback(self,msg):
		x = msg.axes[1]*0.8
		z = msg.axes[3]*10
		f = msg.buttons[5]
		twist= Twist2DStamped()
		twist.v = x
		twist.omega = z
		if f == 1:
			twist.v = 0

		self.publisher.publish(twist)



def main():
	rospy.init_node('test') #creacion y registro del nodo!

	obj = Controller('args') # Crea un objeto del tipo Template, cuya definicion se encuentra arriba

	#objeto.publicar() #llama al metodo publicar del objeto obj de tipo Template

	#rospy.spin() #funcion de ROS que evita que el programa termine -  se debe usar en  Subscribers
	rospy.spin()


if __name__ =='__main__':
	main()
