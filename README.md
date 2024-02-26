# SecureFaceAccess with Arduino Uno Documentation

## Overview
SecureFaceAccess is a face recognition system implemented with Python using the OpenCV and face_recognition libraries. The system is designed to run on an Arduino Uno board along with a camera module. The program captures and recognizes faces in real-time, and if a recognized face is in the database, it opens a connected door via the Arduino Uno.

## Requirements
- Python 3.x
- OpenCV (`cv2`) library
- face_recognition library
- Arduino Uno board
- Camera module compatible with OpenCV
- Serial communication between Python and Arduino

## Installation
Make sure you have Python installed on your system. Install the required libraries using the following command:
```bash
pip install opencv-python face-recognition
```

## Usage
1. Connect your Arduino Uno board to your computer.
2. Update the `arduino_port` variable in the `main` function with the correct serial port of your Arduino (e.g., 'COM3').
3. Run the Python script using the command:
   ```bash
   python secure_face_access.py
   ```
4. The system will capture faces in the camera feed and compare them against the known faces in the 'images' folder.
5. If a recognized face is found, the system opens the door by sending the character 'O' to the Arduino.
6. The Serial number of the recognized face is displayed on the video feed.

## Functions

### 1. `capture_image(camera, person_serial)`
- Captures an image from the camera feed.
- Saves the image in the 'images' folder with the filename as the person's serial number.
- Returns the path to the saved image.

### 2. `load_known_faces()`
- Loads known faces and their serial numbers from images stored in the 'images' folder.
- Utilizes the `face_recognition` library to encode facial features.

### 3. `generate_serial()`
- Generates a unique serial number based on the current date and time, along with a random 3-digit number.

### 4. `main()`
- The main function that initializes the camera, loads known faces, and starts the real-time face recognition loop.
- Communicates with the Arduino Uno to open the door upon face recognition.

## Arduino Communication
The script communicates with the Arduino Uno over a serial connection. It sends the character 'O' to instruct the Arduino to open the door.

## Dependencies
- Python 3.x
- OpenCV (`cv2`) library
- `face_recognition` library

## Notes
- Ensure that the camera is correctly connected and accessible by OpenCV.
- Customize the `arduino_port` variable to match the serial port of your Arduino.
- Adjust the waiting time in the `time.sleep` function after opening the door based on the door's response time.

## Troubleshooting
- If the Arduino is not responding, check the correct serial port and make sure the Arduino is connected.
- Ensure that the required Python libraries are installed.

## Disclaimer
This project is intended for educational purposes. Ensure compliance with local laws and ethical considerations when implementing security-related systems.

**Note:** Keep your Python environment and dependencies up-to-date for optimal performance.
