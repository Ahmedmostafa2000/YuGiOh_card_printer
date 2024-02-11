import cv2
import numpy as np


a4 = np.ones((614*5,421*4,3), np.uint8)*255
for j in range(5):
	for k in range(4):
		
		image = cv2.resize(cv2.imread("cover.png"),((421,614)))
		
		a4[j*image.shape[0]:j*image.shape[0]+image.shape[0], k*image.shape[1]:k*image.shape[1]+image.shape[1]] = image
		

		cv2.imwrite(f"poster/cover.jpg",a4)
		