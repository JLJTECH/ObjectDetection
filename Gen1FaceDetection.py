#!/usr/bin/env python3

import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Read the input image
img = cv2.imread('1.jpg')

# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# Draw rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 1)
    
    #Add Label
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img,'Face',(x,y-10), font, 1, (200,255,155), 1, cv2.LINE_AA)

# Display the output
cv2.imshow('img', img)
cv2.waitKey()
