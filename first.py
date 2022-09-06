import cv2
img=cv2.imread("sample2.png")
cv2.imwrite("sample1.png",img)
cv2.imshow("AI Masterclass",img)
cv2.waitKey(0)
cv2.destroyAllWindows()