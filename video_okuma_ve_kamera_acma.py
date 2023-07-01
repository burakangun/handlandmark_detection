import cv2 as cv
import time
import mediapipe as mp

def video_capture(bfr):
    capture = cv.VideoCapture(bfr)

    while True:
        kontrol, frame = capture.read()
        cv.imshow("frame",frame)

        if cv.waitKey(30) & 0xFF == ord("q"): #q tuşu ile çıkış işlemi gerçekleştirilir.
            break

    cv.destroyAllWindows()

if __name__ == "__main__":

    bfr = 0
    video_capture(bfr)

