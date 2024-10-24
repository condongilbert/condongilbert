import requests
import os
from dotenv import load_dotenv

load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
# Define your GitHub username
GITHUB_USERNAME = "condongilbert"  # Replace with your actual GitHub username

def get_followers():
    token = os.getenv("GITHUB_TOKEN")  # Make sure your token is stored in the .env file
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    url = f"https://api.github.com/users/{GITHUB_USERNAME}/followers"  # Use your username here
    
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        followers = response.json()
        return followers
    else:
        print("Error fetching followers:", response.status_code)
        return []

def update_readme(followers):
    try:
        # Load the current README content
        with open("README.md", "r") as file:
            content = file.readlines()

        # Find the line where you want to insert followers (e.g., a specific section)
        for index, line in enumerate(content):
            if "## Latest Followers" in line:
                start_index = index + 1
                break
        else:
            # If the section doesn't exist, add it at the end
            start_index = len(content)

        # Create the followers string
        followers_list = [f"- {follower['login']}" for follower in followers]
        followers_string = "\n".join(followers_list)

        # Update the README content
        content[start_index:start_index] = [f"## Latest Followers\n{followers_string}\n"]

        # Write the updated content back to the README file
        with open("README.md", "w") as file:
            file.writelines(content)

    except Exception as e:
        print(f"Error updating README: {e}")

# Example of using the functions
if __name__ == "__main__":
    followers = get_followers()
    if followers:
        update_readme(followers)