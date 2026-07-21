import cv2 as cv

def draw_rectangle(img, pt1, pt2, color=(0,0,255), thickness=2):
    cv.rectangle(img, pt1, pt2, color, thickness)

def draw_circle(img, center, radius, color=(0,0,255), thickness=3):
    cv.circle(img, center, radius, color, thickness)

def draw_line(img, pt1, pt2, color=(0,255,255), thickness=5):
    cv.line(img, pt1, pt2, color, thickness)

def put_text(img, text, position, color=(0,255,255), thickness=2, scale=1.0):
    cv.putText(img, text, position, cv.FONT_HERSHEY_TRIPLEX, scale, color, thickness)
