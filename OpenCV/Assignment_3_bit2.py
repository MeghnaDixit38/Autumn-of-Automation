#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 17:20:17 2020

@author: meghnadixit38
"""


import cv2

def sketch(image):
    
    img_gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    
    img_blur=cv2.GaussianBlur(img_gray,(3,3),0)
   
    edges=cv2.Canny(img_blur,10,80)
    
    ret,mask=cv2.threshold(edges,50,255,cv2.THRESH_BINARY_INV)
    return mask


cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    cv2.imshow('Live_Sketch',sketch(frame))
    
    if cv2.waitKey(1)==13:
        break

cap.release()

cv2.destroyAllWindows()