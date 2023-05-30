import github3
import json
from datetime import datetime


class Github:
    def __init__(self):
        f = open("configuration.json")
        data = json.load(f)
        self.config = data["github_code_runner"]
        f.close()
        self.__connect_to_repo()

    def __connect_to_repo(self):
        sess = github3.login(token=self.config["access_token"])
        self.repo = sess.repository(self.config["repo_owner"], self.config["repo_name"])
        print("Connected to repository!")

    def save_to_repo(self, file_name, file_content):
        try:
            print("Saving to repository...")
            self.repo.create_file(file_name, "Added " + file_name, file_content)
        except Exception as e:
            print(e)
