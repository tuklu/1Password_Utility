import subprocess
import re

def get_credentials_from_1password(item_uuid):
    try:
        result = subprocess.run(
            ["op", "item", "get", item_uuid, "--reveal"],
            capture_output=True,
            text=True,
            check=True,
        )
        username_match = re.search(r"username:\s+(.*)", result.stdout)
        password_match = re.search(r"password:\s+(.*)", result.stdout)

        if username_match and password_match:
            username = username_match.group(1)
            password = password_match.group(1)
            return username, password
        else:
            print("Failed to parse credentials from output.")
            return None, None

    except subprocess.CalledProcessError as e:
        print(f"Error retrieving credentials: {e}")
        return None, None
