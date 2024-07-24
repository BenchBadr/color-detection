import cv2
from util import get_limits
from PIL import Image

# read webcam
webcam = cv2.VideoCapture(0)
color = [0, 255, 255]
# visualize webcam
while True:
    ret, frame = webcam.read()
    hsvImg = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV )
    lowerLimit, upperLimit = get_limits(color=color)
    mask = cv2.inRange(hsvImg, lowerLimit, upperLimit)
    mask_ = Image.fromarray(mask)
    bbox = mask_.getbbox()
    if bbox is not None:
        x1, y1, x2, y2 = bbox
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 5)
    cv2.imshow('Video Frame', frame)
    if cv2.waitKey(40) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()