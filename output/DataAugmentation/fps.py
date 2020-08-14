#!/usr/bin/env python

import cv2

outvid1 = cv2.VideoWriter('E:/LincodeLabs/FIlter_classifier/fastAi_results/Inhaler/fps_60_top.mp4',cv2.VideoWriter_fourcc('M','J','P','G'), 60, (640,480))
cap = cv2.VideoCapture(1,cv2.CAP_DSHOW)
#cap.set(cv2.CAP_PROP_FOURCC)
#cv2.VideoWriter_fourcc('M','J','P','G'))
#capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FPS, 60)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640) 
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
fps = int(cap.get(5))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))    
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) 

print('height:',h ,' width:',w)
print("fps:", fps)
print("Framerate = %0.2f FPS" % (fps))
current_gain = cap.get(cv2.CAP_PROP_GAIN)
print("Gain = %0.2f" % (current_gain))
print("Aperture = ", cap.get(cv2.CAP_PROP_APERTURE))
print("Auto Exposure = ", cap.get(cv2.CAP_PROP_AUTO_EXPOSURE))
print("Exposure = ", cap.get(cv2.CAP_PROP_EXPOSURE))
print("Brightness = ", cap.get(cv2.CAP_PROP_BRIGHTNESS))
print("Buffer Size = ", cap.get(cv2.CAP_PROP_BUFFERSIZE))
print("Gamma = ", cap.get(cv2.CAP_PROP_GAMMA))
print("Hue = ", cap.get(cv2.CAP_PROP_HUE))
print("ISO Speed = ", cap.get(cv2.CAP_PROP_ISO_SPEED))
print("Saturation = ", cap.get(cv2.CAP_PROP_SATURATION))
print("Sharpness = ", cap.get(cv2.CAP_PROP_SHARPNESS))
print("White Balance Blue U = ", cap.get(cv2.CAP_PROP_WHITE_BALANCE_BLUE_U))
print("White Balance Red V = ", cap.get(cv2.CAP_PROP_WHITE_BALANCE_RED_V))
while(cap.isOpened()):
    test_video_framerate = cap.get(cv2.CAP_PROP_FPS)
    # print(test_video_framerate)
    ret,frame = cap.read()
    if not ret:
        break
    cv2.imshow('frame', frame)
    outvid1.write(frame)

    k = cv2.waitKey(1)
    if k == 27:
        break