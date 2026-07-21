import cv2 as cv
import numpy as np
import Day7_image_utils as iu

blank = np.zeros((500, 500, 3), dtype='uint8')
center = (blank.shape[1]//2, blank.shape[0]//2)

iu.draw_rectangle(blank, (0,0), center)
iu.draw_circle(blank, center, 40)
iu.draw_line(blank, (0,0), center)
iu.put_text(blank, "Day 7", (210,225))

cv.imshow("Day 7", blank)
cv.waitKey(0)
