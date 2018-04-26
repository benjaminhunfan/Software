#!/usr/bin/env python

import rospy #importar ros para python
from std_msgs.msg import String, Int32 # importar mensajes de ROS tipo String y tipo Int32
import numpy as np
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class Controller(object):
	def __init__(self, args):
		super(Controller, self).__init__()
		self.args = args
		self.subscriber = rospy.Subscriber("/usb_cam/image_raw", Image, self.callback)
		self.publisher = rospy.Publisher("/duckiebot/Image_procesada", Image, queue_size=10)
		self.bridge= CvBridge()


	def callback(self,msg):
		try:
			cv_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")
		except CvBridgeError as e:
			print (e)

		lower_yellow = np.array([30, 86, 172])
		upper_yellow = np.array([61, 255, 255])

		mask = cv2.inRange(cv_image, lower_yellow, upper_yellow)
		kernel = np.ones((5,5),np.uint8)

		mask = cv2.erode(mask, kernel, iterations= 1)
		mask = cv2.dilate(mask, kernel, iterations= 8)

		image, contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
		areas = [cv2.contourArea(c) for c in contours]

		#print 'number of contours', len(contours)
		if len(contours)>0:
			for c in contours:
				#max_index = np.argmax(areas)
				#cnt = contours[max_index]
				cnt = c
				x,y,w,h= cv2.boundingRect(cnt)

				cv2.rectangle(cv_image, (x,y), (x+w,y+h), (0,255,0),2)

		image_out = cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV)
		image_out= cv2.bitwise_and(cv_image, cv_image, mask= mask)
		imagen_procesada= self.bridge.cv2_to_imgmsg(cv_image, "bgr8")
		self.publisher.publish(imagen_procesada)




def main():
	rospy.init_node('test') #creacion y registro del nodo!

	obj = Controller('args') # Crea un objeto del tipo Template, cuya definicion se encuentra arriba

	#objeto.publicar() #llama al metodo publicar del objeto obj de tipo Template

	rospy.spin() #funcion de ROS que evita que el programa termine -  se debe usar en  Subscribers


if __name__ =='__main__':
	main()
