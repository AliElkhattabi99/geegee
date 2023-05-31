import pyautogui
import socket
import os
from datetime import datetime
from Github import Github


class ScreenShotter:
    def capture_screenshot():
        screenshot = pyautogui.screenshot()

        screenshot.save("screenshot.png")
        print("Schermafbeelding gemaakt: screenshot.png")

    def upload_to_github():
        github = Github()

        with open("screenshot.png", "rb") as file:
            content = file.read()
            print("Schermafbeelding geüpload naar GitHub")
            name = (
                socket.gethostname()
                + datetime.today().strftime("%Y-%m-%d %H:%M:%S")
                + ".png"
            )
            github.save_to_repo("Screens/" + name, content)
        os.remove("screenshot.png")


ScreenShotter.capture_screenshot()
ScreenShotter.upload_to_github()
