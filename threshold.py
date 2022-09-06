import cv2
img = cv2.imread("download.jpeg")
grayImg=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("img",img)
threshImg = cv2.threshold(grayImg,150,255,cv2.THRESH_BINARY)[1]
cv2.imwrite("thresholdImg.jpg",threshImg)