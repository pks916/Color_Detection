import numpy as np
import cv2

def get_limits(color):

    c = np.uint8([[color]])
    hsvC = cv2.cvtColor(c,cv2.COLOR_BGR2HSV)

    lwr_limit = hsvC[0][0][0] - 10, 100, 100
    upr_limit = hsvC[0][0][0] + 10, 255, 255

    lwr_limit = np.array(lwr_limit, dtype=np.uint8)
    upr_limit = np.array(upr_limit, dtype=np.uint8)
    
    return lwr_limit, upr_limit