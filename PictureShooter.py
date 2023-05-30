import cv2
from Github import Github


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
            commit_message = "Add picture"
            print("Picture uploaded successfully")
            github.save_to_repo("picture.png", content)
    except Exception as e:
        print(f"Failed to upload picture: {str(e)}")


# Capture a picture and upload it to GitHub
capture_and_upload_picture()
