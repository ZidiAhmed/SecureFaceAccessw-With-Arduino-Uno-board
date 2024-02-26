import cv2
import face_recognition
import os
from datetime import datetime
import random
import serial
import time

# Create the images folder if it doesn't exist
if not os.path.exists('images'):
    os.makedirs('images')

def capture_image(camera, person_serial):
    ret, frame = camera.read()
    if ret:
        image_path = f"images/{person_serial}.jpg"
        cv2.imwrite(image_path, frame)
        print(f"Image saved: {image_path}")
        return image_path
    return None

def load_known_faces():
    known_faces = []
    known_serials = []
    
    for file_name in os.listdir('images'):
        if file_name.endswith('.jpg'):
            image_path = os.path.join('images', file_name)
            person_serial = os.path.splitext(file_name)[0]
            
            try:
                known_image = face_recognition.load_image_file(image_path)
                known_encoding = face_recognition.face_encodings(known_image)[0]
                known_faces.append(known_encoding)
                known_serials.append(person_serial)
            except Exception as e:
                print(f"Error loading image {image_path}: {e}")

    return known_faces, known_serials

def generate_serial():
    now = datetime.now()
    serial_number = now.strftime("%Y%m%d%H%M%S") + str(random.randint(100, 999))
    return serial_number

def main():
    camera = cv2.VideoCapture(0)
    known_face_encodings, known_face_serials = load_known_faces()

    # Open serial connection to Arduino
    arduino_port = 'COM3'  # Change to your Arduino's serial port
    ser = serial.Serial(arduino_port, 9600, timeout=1)

    while True:
        ret, frame = camera.read()

        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)

        for face_encoding, face_location in zip(face_encodings, face_locations):
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            face_serial = "Unknown"

            if True in matches:
                first_match_index = matches.index(True)
                face_serial = known_face_serials[first_match_index]
            else:
                face_serial = generate_serial()
                capture_result = capture_image(camera, face_serial)

                if capture_result:
                    known_face_encodings.append(face_encoding)
                    known_face_serials.append(face_serial)
                    
                    # Send 'O' to Arduino to open the door
                    ser.write(b'O')
                    print("Opening the door for Serial:", face_serial)
                    time.sleep(2)  # Allow time for the door to open (adjust as needed)

                    # Display "Welcome" message on the screen
                    print("Welcome!")

            top, right, bottom, left = face_location
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, f"Serial: {face_serial}", (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

        cv2.imshow('Face Recognition System', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()
    ser.close()

if __name__ == "__main__":
    main()
