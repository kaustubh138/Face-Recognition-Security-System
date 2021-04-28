# Security System Based on Facial Recognition

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#caveats">Caveats</a>
    </li>
    <li>
      <a href="#installation">Installation</a>
    </li>
    <li>
      <a href="#demo">Demo</a>
    </li>
    </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

This is facial recognition based security system, which can be scaled to make an actuall survellince system.
Whenever, there is person in front of the camera, the system detects the face and compares it with the dataset that is provided by the user, if the face matches the dataset,i.e, authentication successfull, it does nothing.
But if it does not, then it updates the terminal with "[ALERT] Intrusion Detected.." and the image is saved in the intruder folder.

### Built With

* Python
* Caffe Neural Network
* Modules:
  * OpenCV Python
  * dlib - [How to install dlib?](https://www.pyimagesearch.com/2017/03/27/how-to-install-dlib/)
  * facial-recognition
  * pickle

### Caveats:
* dlib and facial recognition need Unix-like OS to work, so they won't work on Windows.
I worked on this project on windows, but used ubuntu (on WSL) to train (using trainner.py)

* make sure no other program is using the camera sensor while running the recognizer.py, in that case it will thorugh an error.

* The frame rate of video output is really choppy beacuse there is a lot that goes on behind each frame captured from the camera.

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/kaustubh138/Face-Recognition-Security-System.git
   ```
2. Install required packages
   ```sh
   pip install -r requirments.txt
   ```
3. Paste your facial images in the auth_dataset directory, and rename them in sequence, if you are too lazy to do that run the renamer.py changing the name Kaustubh to           YourName or the name you want.
   * NOTE: run the renamer.py only inside the auth_dataset file, else it will delete everything in the folder from which it is run
4. Run gen_dataset.py:
   ```sh
   python -m gen_dataset.py
   ```
5. Run trainner.py
   ```sh
   python -m trainner.py
   ```
6. Finally run the recognizer.py
   ```sh
   python -m recognizer.py
   ```
   
### Demo
* Detects the authorized faces:
![Authorized Face Detection](https://github.com/kaustubh138/Face-Recognition-Security-System/blob/main/demo/auth_face_rec.jpg)

* Also recognizes the unauthorized faces:
![Un-authorized Face Detection](https://github.com/kaustubh138/Face-Recognition-Security-System/blob/main/demo/unauth_face_rec.jpg)

* Gives you an alert
![Alert](https://github.com/kaustubh138/Face-Recognition-Security-System/blob/main/demo/alert.jpg)

* Saves the images in the intruder folder
![Intruder Folder](https://github.com/kaustubh138/Face-Recognition-Security-System/blob/main/demo/intrusion_foler_screenshot.jpg)
![Intruder](https://github.com/kaustubh138/Face-Recognition-Security-System/blob/main/demo/intruder_image_sample.jpg)
    
