import cv2

img=cv2.imread("download.jpeg")

gaussianBlurImg=cv2.GaussianBlur(img, (21,21),0)
cv2.imwrite ("gaussian Image2.jpg", gaussianBlurImg)