import cv2
import os

for i in os.listdir("poster"):
	image = cv2.imread("poster/"+i)
	image = cv2.resize(image,(118*25,118*44))

	cv2.imwrite(f"resized/{i}",image)