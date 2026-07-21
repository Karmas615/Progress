#video
import cv2 as cv

#image, video, live video
def rescaleFrame(frame,scale = .75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

#live video
def changeRes(width, height):
    capture.set(3,width)
    capture.set(4,height)

#video
capture = cv.VideoCapture('CV/Videos/dog_video.mp4')
while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame, scale = .3)
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'): #press d to break"
        break  
capture.release()
cv.destroyAllWindows()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import numpy as np

#blank.shape returns the dimensions of the image, which is a tuple of (height, width, channels). The height is the number of rows in the image, the width is the number of columns in the image, and the channels is the number of color channels in the image (3 for a color image and 1 for a grayscale image).
blank = np.zeros((500,500,3),dtype='uint8') #uint8 is a data type that can store values from 0 to 255, which is the range of pixel values for an 8-bit image.
#cv.imshow('Blank',blank)

#paint image a certrain color
#blank[0:500, 0:500] = 0,255,0 #first is height, second is width, third is color in BGR format
#cv.imshow('Green',blank)

#draw a rectangle
cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,0,255),thickness=2) #draws a rectangle on the image, with the top-left corner at (0,0) and the bottom-right corner at (blank.shape[1]//2,blank.shape[0]//2), with a color of (0,0,255) in BGR format and a thickness of cv.FILLED, which means the rectangle will be filled with color.
cv.imshow('Rectangle',blank)

#draw a circle
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,0,255),thickness=3) #draws a circle on the image, with the center at (blank.shape[1]//2,blank.shape[0]//2) and a radius of 40 pixels, with a color of (0,0,255) in BGR format and a thickness of 3 pixels.
cv.imshow('Circle',blank)

#draw a line
cv.line(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(255,255,255),thickness=5) #draws a line on the image, with the starting point at (0,0) and the ending point at (blank.shape[1]//2,blank.shape[0]//2), with a color of (255,255,255) in BGR format and a thickness of 5 pixels.
cv.imshow('Line',blank)

#write a text
cv.putText(blank,'Hello World',(175,225),cv.FONT_HERSHEY_TRIPLEX,1.0,(255,255,255),thickness=2) #draws text on the image, with the text 'Hello World' starting at the position (175,225), using the font cv.FONT_HERSHEY_TRIPLEX, with a font scale of 1.0, a color of (255,255,255) in BGR format and a thickness of 2 pixels.
cv.imshow("Text",blank)

cv.waitKey(0)  


 