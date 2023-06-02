import cv2
import time
cap = cv2.VideoCapture('cam_video.mp4')
while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    ret, thresh = cv2.threshold(gray, 105, 255, cv2.THRESH_BINARY_INV)

    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    if len(contours) >0:
        h1, w1, _ = frame.shape # определние ширины и высоты изображения
        c = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(c)
        x1 = x+w//2 # коодината центра по горизонтали
        y1 = y+h//2 # коодината центра по вертикали

        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        cv2.line(frame, (x1-w1, y1), (x1+w1, y1), (0, 255, 0), 2) #построение горизонтальной линии
        cv2.line(frame, (x1, y1-h1), (x1, y1+h1), (0, 255, 0), 2) #построение вертикальной линии



    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    time.sleep(0.001)
cap.release()
cv2.destroyAllWindows()
