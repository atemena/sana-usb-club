import json

def get_profile():
    try:
        with open('sana_profile.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return None

def set_profile(user_profile):
    with open('sana_profile.json', 'w') as f:
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