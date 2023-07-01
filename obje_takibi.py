import cv2 as cv
import time
import mediapipe as mp

cap = cv.VideoCapture(0)

mpHand = mp.solutions.hands
hands = mpHand.Hands() # ellerin tespiti ve konulandırılması için
mpdraw = mp.solutions.drawing_utils #çizim

pTime = 0
cTime = 0

while True:
    control, capture = cap.read()
    results = hands.process(capture)

    print(results.multi_hand_landmarks) # el tespiti kordinatları

    if results.multi_hand_landmarks:
        for handlms in results.multi_hand_landmarks:
            mpdraw.draw_landmarks(capture,handlms, mpHand.HAND_CONNECTIONS)

            for number, lm in enumerate(handlms.landmark):
                print(number,lm) #number eklem numarası, lm => x,y,z koordinatları
                h,w,c = capture.shape
                cx,cy = int(lm.x*w),int(lm.y*h)


                #işaret parmağının tespiti
                if ((number==4) | (number==8) | (number==12) | (number==16) | (number==20)):
                    cv.circle(capture,(cx,cy),20,(255,0,0),cv.FILLED)


    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime=cTime

    cv.putText(capture,"FPS: "+str(int(fps)),(10,75),cv.FONT_HERSHEY_PLAIN,3,(255,0,0),5)
    
    cv.imshow("capture",capture)

    if cv.waitKey(1) & 0XFF == ord("q"):
        break

cv.destroyAllWindows()

