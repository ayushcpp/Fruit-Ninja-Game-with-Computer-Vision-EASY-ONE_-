import  cv2
from cvzone.HandTrackingModule import HandDetector
import mouse
import numpy as np
import pyautogui

cap=cv2.VideoCapture(0)
cam_w,cam_h=640,480
cap.set(3,cam_w)
cap.set(4,cam_h)
frame_Reduction=50 # Frame Reduction is the another method of solving Jittering like smoothing
detector = HandDetector(detectionCon=0.8, maxHands=1)
dragging=False
screen_w, screen_h = pyautogui.size()

while True:
    success,img=cap.read()
    if not success:
        break
    img=cv2.flip(img,1)
    hands,img=detector.findHands(img)
    cv2.rectangle(img,(frame_Reduction,frame_Reduction),(cam_w -frame_Reduction,cam_h-frame_Reduction),(255,0,255),2)
    if hands:
        lmlist=hands[0]['lmList']
        ind_x,ind_y=lmlist[8][0],lmlist[8][1]
        cv2.circle(img,(ind_x,ind_y),5,(0,255,255),2)
        conv_x=int(np.interp(ind_x,(frame_Reduction,cam_w-frame_Reduction),(0,screen_w-1)))
        conv_y=int(np.interp(ind_y,(frame_Reduction,cam_h-frame_Reduction),(0,screen_h-1)))
        mouse.move(conv_x,conv_y)
        fingers=detector.fingersUp(hands[0]) # return an array of fingers
        only_index_up = (fingers[1] == 1 and
                         fingers[0] == 0 and
                         fingers[2] == 0 and
                         fingers[3] == 0 and
                         fingers[4] == 0)

        if only_index_up:
            if not dragging:
                pyautogui.mouseDown()
                dragging = True
        else:
            if dragging:
                pyautogui.mouseUp()
                dragging = False



    cv2.imshow("HAHA",img)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()