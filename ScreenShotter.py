import pyautogui
from Github import Github


def capture_screenshot():
    # Maak een schermafbeelding
    screenshot = pyautogui.screenshot()

    # Sla de schermafbeelding op als bestand
    screenshot.save("screenshot.png")
    print("Schermafbeelding gemaakt: screenshot.png")


def upload_to_github(file_path):
    # Maak een GitHub-instantie met behulp van het persoonlijke toegangstoken
    github = Github()

    # Upload het bestand naar het repository
    with open(file_path, "rb") as file:
        content = file.read()
        commit_message = f"Upload screenshot: {file_path}"
        print("Schermafbeelding geüpload naar GitHub")
        github.save_to_repo("screenshot.png", content)


# Roep de functie aan om een schermafbeelding te maken
capture_screenshot()
upload_to_github("screenshot.png")

# Upload de schermafbeelding naar GitHub
"""repo_owner = "gebruikersnaam"
repo_name = "repositorynaam"
file_path = "screenshot.png"
github_token = "jouw_persoonlijke_toegangstoken"
upload_to_github(repo_owner, repo_name, file_path, github_token)"""
