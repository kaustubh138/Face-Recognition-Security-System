from cv2 import cv2
import imutils
from imutils.video import VideoStream
import time
import os
import numpy as np

name = input("Name: ")

print("[INFO] Getting Things Ready......")
net = cv2.dnn.readNetFromCaffe(
    "deploy.prototxt.txt", "res10_300x300_ssd_iter_140000.caffemodel")
vs = VideoStream(src=0).start()
time.sleep(2)

if "auth_dataset" in os.listdir():
    os.chdir("auth_dataset")
else:
    os.mkdirs("auth_dataset")
    os.chdir("auth_dataset")


def wait(t):
    while t:
        mins, secs = divmod(t, 60)
        print(f"[INFO] Capturing in {secs}(s)....", end="\r")
        time.sleep(1)
        t -= 1


# read the video stream frame by frame
sample_num = 0
run = True
while run:
    frame = vs.read()
    frame = imutils.resize(frame, width=400)
    frame = cv2.flip(frame, 1)
    (h, w) = frame.shape[:2]

    blob = cv2.dnn.blobFromImage(cv2.resize(
        frame, (300, 300)), 1, (300, 300), (104.0, 177.0, 123.0))

    net.setInput(blob)

    detections = net.forward()

    for i in range(0, detections.shape[2]):
        conf = detections[0, 0, i, 2]

        if conf > 0.5:
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")
            cv2.imwrite(f"{name}_{sample_num}.jpg",
                        frame[startX:endX, startY:endY])

    if sample_num == 20:
        print("[INFO] All Done..")
        run = False

    print(f"[INFO] Sample Dataset {sample_num}")
    wait(5)
    cv2.imshow("Cam", frame)
    sample_num = sample_num + 1

cv2.destroyAllWindows()
vs.stop()
