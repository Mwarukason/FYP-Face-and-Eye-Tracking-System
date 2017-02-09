#Import Libraries 
import cv2
import pyautogui
import win32api
import numpy as np

#main body











        k = cv2.waitKey(10) & 0xFF
        if k == 27:
            break
        elif k == ord('f'):
            cv2.imwrite("frame.png", frame)
            cv2.flip(frame, frame, 1)
    cv2.destroyAllWindows()
    
    
    
 if __name__ == '__main__':
        main()
