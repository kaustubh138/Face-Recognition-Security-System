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
    </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

This is facial recognition based security system, which can be scaled to make an actuall survellince system.
Whenever, there is person in front of the camera, the system detects the face and compares it with the dataset that is provided by the user, if the face matches the dataset,i.e, authentication successfull, it does nothing.
But if it does not, then it updates the terminal with "[ALERT] Intrusion Detected.."

### Built With

* Python
* Caffe Neural Network
* Modules:
  * OpenCV Python
  * dlib
  * facial-recognition
  * pickle

### Caveats:
* dlib and facial recognition need Unix-like OS to work, so they won't work on Windows.
I worked on this project on windows, but used ubuntu (on WSL) to train (using trainner.py)

* make sure no other program is using the camera sensor while running the recognizer.py, in that case it will thorugh an error.

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/kaustubh138/Face-Recognition-Security-System
   ```
2. Install required packages
   ```sh
   pip install -r requirments.txt
   ```
3. Paste your facial images in the auth_dataset directory
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
