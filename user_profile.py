import json
import os
import sys

# Get the directory of the executable
exe_dir = os.path.dirname(sys.executable)

# Construct the path to the JSON file
json_file = os.path.join(exe_dir, 'sana_profile.json')

def get_profile():
    try:
        with open(json_file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return None

def set_profile(user_profile):
    with open(json_file, 'w') as f:
        json.dump(user_profile, f)

def set_key(key, value):
    # Load the existing profile
    user_profile = get_profile()
    if user_profile is None:
        user_profile = {}

    # Update the key with the new value
    user_profile[key] = value

    # Save the profile back to the file
    set_profile(user_profile)