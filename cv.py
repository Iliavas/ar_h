import numpy as np
import cv2
frame = None
cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()

    blurred = cv2.blur(frame, (10, 10))
    low = np.array((0, 150, 0))
    high = np.array((100, 254, 100))
    mask = cv2.inRange(blurred, low, high)

    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    print(contours, hierarchy)
    if contours:
        counter = 0
        l = []
        for i in contours:
            counter+=1
            (x, y, w, h) = cv2.boundingRect(i)
            l.append((x, y, w, h))
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 0), 3)
        max_x, max_y, max_x1, max_y1 = 0, 0, 0, 0
        for i in range(len(l)):
            if l[i][0] > max_x:
                max_x = l[i][0]
            if l[i][1] > max_y:
                max_y = l[i][1]
            if l[i][2] > max_x1:
                max_x1 = l[i][2]
            if l[i][3] > max_y1:
                max_y1 = l[i][3]
        cv2.rectangle(frame, (max_x, max_y), (max_x1, max_y1), (255, 255, 0), 3)
    try:
        cv2.imshow('mask', mask)
        cv2.imwrite('frame.jpg', frame)
        cv2.imshow('frame', frame)
    except: pass
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
