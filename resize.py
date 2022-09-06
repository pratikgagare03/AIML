import cv2
import imutils
img = cv2.imread("download.jpeg")
resizeImg = imutils.resize(img, width=10)
cv2.imwrite("resizedImage.jpeg",resizeImg)