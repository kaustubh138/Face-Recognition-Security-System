from cv2 import cv2
# import path
import face_recognition
import pickle
import os

try:
    os.chdir("auth_dataset")
except FileNotFoundError:
    pass

# grab the images from the authorized dataset folder
print("[INFO] Quantifying faces...")
imagePaths = list(os.listdir())

# initialize the list of known encodings and corrosponding names
knownEncodings = []
knownNames = []

for (i, imagePath) in enumerate(imagePaths):
    print(f"[INFO] Processing image {i}/{len(imagePaths)}")

    # extract the names from image path
    # name = imagePath.split(".")[-1]

    _ = imagePath.split(".")[-2]
    name = _.split("_")[0]

    # load the image in the opencv and convert it to rgb as dlib uses RGB encodings
    # contrary to BGR used by opencv.
    image = face_recognition.load_image_file(imagePath, mode="RGB")
    # recognize faces and return location of face
    # (i.e, the x, y coordinates of the boxes around them)
    boxes = face_recognition.face_locations(image, model="hog")
    # i used the "hog" method rather than "cnn" method
    # as it is faster (but less accurate)

    # now we extract the encodings form the face
    encodings = face_recognition.face_encodings(image, boxes)
    # this function returns a 128d vector
    # (128 real numbers corrosponding to facial characterstics)

    # append the encodings to knownEncodings list
    for encoding in encodings:
        knownEncodings.append(encoding)
        knownNames.append(name)

# dump the encodings and corrosponding names into a dictionary
# and store the encodings in a pickle file for future use
print("[INFO] Arranging data....")

data = {"encodings": knownEncodings, "names": knownNames}

os.chdir("..")
with open("encodings.pickle", mode="wb") as f:
    f.write(pickle.dumps(data))
