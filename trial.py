import urllib.request
import cv2
import numpy as np
# Replace the URL with your own IPwebcam shot.jpg IP:port
url='http://192.168.137.78:8080/shot.jpg'

imgResp = urllib.request.urlopen(url)

imgNp = np.array(bytearray(imgResp.read()),dtype=np.uint8)

# Decode the array to OpenCV usable format
img = cv2.imdecode(imgNp,-1)


# put the image on screen
cv2.imshow('IPWebcam',img)
cv2.waitKey(10)
# Program closes if q is pressed
print('Original Dimensions : ',img.shape)
 
width = 100
height = 100
dim = (width, height)
 
# resize image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
 
print('Resized Dimensions : ',resized.shape)
 
cv2.imshow("Resized image", resized)
cv2.waitKey(0)

#hello