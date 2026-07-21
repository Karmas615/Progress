#essential functions in opencv
import cv2 as cv

img = cv.imread('CV/Photos/download.webp')

cv.imshow('Image', img)

#Turns the image into gray scale
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray_img)

#Blur makes the image blurry and smooth, it is used to remove noise from the image. It is also used to reduce the details in the image.
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT) #increasing kernal size will increase the blur effect
cv.imshow('Blur', blur)

#Edge Cascade makes the image edges more prominent, it is used to detect the edges in the image. It is also used to reduce the details in the image.
canny = cv.Canny(blur, 125, 175)
cv.imshow("Canny",canny)

#Dilating the image makes the edges more prominent, it is used to increase the thickness of the edges. It is also used to reduce the details in the image.
dilated = cv.dilate(canny, (7,7), iterations=1) #increasing kernal size and iterations will increase the thickness of the edges
cv.imshow("Dilated", dilated)

#Eroding makes the edges less prominent, it is used to decrease the thickness of the edges. It is also used to reduce the details in the image.
eroded = cv.erode(dilated, (3,3), iterations=1) #increasing kernal size and iterations will decrease the thickness of the edges
cv.imshow("Eroded", eroded)

#Resize resizes the image to a specific size, it is used to change the size of the image. It is also used to reduce the details in the image.
resize = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)  #interpolation=cv.INTER_CUBIC is used to increase the size of the image, it is also used to reduce the details in the image.
cv.imshow('Resize', resize)

#cropping crops the image to a specific size, it is used to remove the unwanted parts of the image. It is also used to reduce the details in the image.
cropped = img[50:100, 100:500] #first is height, second is width
cv.imshow('Cropped', cropped)


cv.waitKey(0) 

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#color spaces

img = cv.imread('CV/Photos/download.webp')

cv.imshow('Image', img)

#gray scale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

#BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('L*a*b', lab)

#BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

#HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV to BGR', hsv_bgr)
cv.waitKey(0)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Template matching is a technique used to find a specific object in an image. It is used to find the location of the object in the image. It is also used to reduce the details in the image.
import numpy as np

img = cv.imread('CV/Photos/soccer_practice.jpg', 0)
template = cv.imread('CV/Photos/ball.PNG', 0)
h, w = template.shape

methods = [cv.TM_CCOEFF_NORMED, 
            cv.TM_CCORR_NORMED, cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]

for method in methods:
    img2 = img.copy()
    
    result = cv.matchTemplate(img2, template, method)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
    if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc
    
    bottom_right = (location[0] + w, location[1] + h)
    cv.rectangle(img2, location, bottom_right, 255, 5 )
    cv.imshow("Img2",img2)
    cv.waitKey(0)
    cv.destroyAllWindows



