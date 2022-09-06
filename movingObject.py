import cv2  # imported opencv
import time  # time library
import imutils  # resizing library

# initialize the camera time.sleep (1) #1 second delay
cam = cv2.VideoCapture(0)


# while(cam.isOpened()): # Capture frame-by-frame
#         ret, frame = cam.read()
#         if ret:
#             assert not isinstance(frame,type(None)), 'frame not found'
# success, cv_img = cam.read()

firstFrame = None  # initializing there are no object.

area = 500  # threshold

while True:  # infinite loop
    _, img = cam.read()  # read the frame from the camera, it returns two values a flag and image so we don't need f;ag so just written _
    text = "Normal"  # initialize the text as Normal
    img = imutils.resize(img, width=500)  # resize the image
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # convert color to Gray:

    gaussianImg = cv2.GaussianBlur(grayImg, (21, 21), 0)  # smoothening

    if firstFrame is None:
        firstFrame = gaussianImg  # we are saving the first preprocessed 1
        continue

    imgDiff = cv2.absdiff(firstFrame, gaussianImg)  # subtracting current frar
    threshImg = cv2.threshold(imgDiff, 25, 255, cv2.THRESH_BINARY)[1]  # thre:
    threshImg = cv2.dilate(threshImg, None, iterations=2)  # remove holes
    # covering up the whole moving object a
    cnts = cv2.findContours(
        threshImg.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    cnts = imutils.grab_contours(cnts)

    for c in cnts:
        if cv2.contourArea(c) < area:
            continue
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(img, (x, y), (x+w, y + h), (0, 255, 0), 2)
        text = "Moving Object detected"

    print(text)

    cv2.putText(img, text, (10, 20),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.imshow("cameraFeed", img)
    key = cv2.waitKey(1) & 0xFF #record the pressed key
    if key == ord("x"):
        break

cam.release()

cv2.destroyAllWindows()
