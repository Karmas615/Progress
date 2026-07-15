#Photo
import cv2 as cv

img = cv.imread('CV/Photos/download.webp')

cv.imshow('Image', img)
cv.waitKey(0)  # Wait for a key press to close the window

#video
import cv2 as cv

capture = cv.VideoCapture('CV/Videos/learn.mp4')
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'): #press d to break"
        break  
capture.release()
cv.destroyAllWindows()



