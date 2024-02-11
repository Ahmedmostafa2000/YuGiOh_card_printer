import cv2
import os

import numpy as np


oslist = os.listdir("new")
try:
	for i in range(15):
		a4 = np.ones((614*5,421*4,3), np.uint8)*255
		for j in range(5):
			for k in range(4):
				
				image = cv2.imread("new/"+oslist[i*20+j*4+k])
				print()
				a4[j*image.shape[0]:j*image.shape[0]+image.shape[0], k*image.shape[1]:k*image.shape[1]+image.shape[1]] = image
				
				cv2.imwrite(f"poster/{i}.jpg",a4)
					
except:
	print("happend")

for i in os.listdir("poster"):
	image = cv2.imread("poster/"+i)
	image = cv2.resize(image,(118*25,118*44))

	cv2.imwrite(f"resized_poster/{i}",image)
	
