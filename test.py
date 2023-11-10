import cv2
cap = cv2.VideoCapture("rtsp://admin:admin@192.168.0.101:8554/live")
while (cap.isOpened()):
    ret,frame=cap.read()
    cv2.imshow('show',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break