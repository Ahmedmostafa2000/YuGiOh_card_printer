import cv2
import os

for i in os.listdir("toberesized"):
	image = cv2.imread("toberesized/"+i)
	image = cv2.resize(image,(421,614))

	cv2.imwrite(f"resized/{i}",image)