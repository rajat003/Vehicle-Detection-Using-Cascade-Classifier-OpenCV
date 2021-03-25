# OpenCV Python Program To Detect Vehicle In A Video
# Used Python Version 3.6.10

# Project - Group 12
# IDE - PyCharm 2019.03 Community Version

# Videos are taken from youtube, mobile recordings and other sources
# Reference from Lecture notes and online resources OpenCV tutorials

# import libraries of python OpenCV
# some libraries like cv2, python3.6, NumPy, cmake

import cv2
 
# capture frames from a video
cap = cv2.VideoCapture('y_video1.mp4')
 
# Trained XML classifiers describes some features of some object we want to detect
car_cascade = cv2.CascadeClassifier('cars.xml')
 
# loop runs if capturing has been initialized.
# code for loop to read the frames from the video
while True:
    # reads frames from a video
    ret, frames = cap.read()
     
    # convert to gray scale of each frames
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
     
 
# Detection of cars different sizes in the input image/ video frame

    cars = car_cascade.detectMultiScale(gray, 1.1, 1)
     
# To draw a rectangle in each cars
    for (x,y,w,h) in cars:
        cv2.rectangle(frames,(x,y),(x+w,y+h),(0,255,255),2)
 
# Display frames in a window
    cv2.imshow('Detection of Car', frames)

# Press Q on keyboard to  exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break


# De-allocate any associated memory usage
cv2.destroyAllWindows()