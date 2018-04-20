from PIL import ImageGrab
import numpy as np
import cv2
import time
import pyautogui  ##workaround for window scaling problem

last_time = time.time()

while(True):
    img = ImageGrab.grab(bbox=(10,40,1920,1120)) #bbox specifies specific region (bbox= x,y,width,height)
    img_np = np.array(img)
    img = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)

    print('loop took {} seconds'.format(time.time()-last_time))
    last_time = time.time()
    
    cv2.imshow('GTAV_OpenCV_Output', np.array(img))
    cv2.waitKey(25) & 0xFF == ord('q')
cv2.destroyAllWindows()