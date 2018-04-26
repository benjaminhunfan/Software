#!/usr/bin/env python

import rospy #importar ros para python
from std_msgs.msg import String, Int32 # importar mensajes de ROS tipo String y tipo Int32
from geometry_msgs.msg import Twist # importar mensajes de ROS tipo geometry / Twist


class Test1(object):
	def __init__(self, args):
		super(Test1, self).__init__()
		self.args = args
		self.publisher = rospy.Publisher( "/chat", String, queue_size=10)


	#def publicar(self):
	def publicar(self):
		while(true):
		
			
			self.publisher.publish(msg)
			rospy.sleep(1)
		
	#def callback(self,msg):

msg = String()
msg.data = "hola"
def main():
	rospy.init_node('test') #creacion y registro del nodo!

	obj = Test1('args') # Crea un objeto del tipo Template, cuya definicion se encuentra arriba

	#objeto.publicar() #llama al metodo publicar del objeto obj de tipo Template

	#rospy.spin() #funcion de ROS que evita que el programa termine -  se debe usar en  Subscribers


if __name__ =='__main__':
	main()
