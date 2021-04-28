import imutils
from imutils.video import VideoStream
from cv2 import cv2
import face_recognition
import pickle
import time
import os

print("[INFO] Loading Encodings....")
data = pickle.loads(open("encodings.pickle", "rb").read())

# intialize the video stream
print("[INFO] Starting Camera...")
vs = VideoStream(src=0).start()
# let the sensor warm up
time.sleep(2)


def saveIntruder():
    os.chdir("intruders")
    nameImg = "intruder"
    nameExt = ".jpg"
    name = nameImg + nameExt
    if name in list(os.listdir()):
        name = nameImg + "0" + nameExt
    cv2.imwrite(name, frame)

    # frame_width = int(vs.width)
    # frame_height = int(vs.height)
    # size = (frame_width, frame_height)
    # # now = dt.now()
    # # name = str(now.strftime("%H:%M:%S"))
    # result = cv2.VideoWriter('filename.avi',
    #                          cv2.VideoWriter_fourcc(*'MJPG'),
    #                          10, size)
    # intrusion_vid.write(frame)
    os.chdir("..")


run = True
while run:
    frame = vs.read()

    # convert the frame into BGR to RGB then resize
    # to have a width 750px (for speed procesing)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    rgb = imutils.resize(frame, width=750, height=750)
    r = frame.shape[1] / float(rgb.shape[1])

    # detect the (x, y) co-ordiinates of the bounding boxes
    # then compute facial embeddings for each face

    boxes = face_recognition.face_locations(rgb, model="hog")
    encodings = face_recognition.face_encodings(rgb, boxes)
    names = []

    for encoding in encodings:
        # attempt to match each face in the input image to
        # out known encodings
        matches = face_recognition.compare_faces(data["encodings"], encoding)

        name = "Unknown"

        # check to see if any matches were found
        if True in matches:
            # find the indexes of the matches
            color = (0, 255, 0)
            matchedIdxs = [i for (i, b) in enumerate(matches) if b]
            counts = {}

            # loop over all the matches and maintain a count
            for i in matchedIdxs:
                name = data["names"][i]
                counts[name] = counts.get(name, 0) + 1
                # determine the recognized face woth the largest number
                # of votes
                name = max(counts, key=counts.get)
        else:
            color = (0, 0, 255)
            print("[ALERT] Intrusion Detected...")
            saveIntruder()

        print("[INFO] Recognizing faces....")
        print(f"[INFO] Detected faces: {names}")
        names.append(name)

        # loop over recognized faces
        for ((top, right, bottom, left), name) in zip(boxes, names):
            # rescale the face coordinates
            top = int(top * r)
            right = int(right * r)
            bottom = int(bottom * r)
            left = int(left * r)

            # draw the predicted face names on the image
            cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
            y = top - 15 if top - 15 > 15 else top + 15
            cv2.putText(frame, name, (left, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.75, color, 2)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

cv2.destroyAllWindows()
vs.stop()
