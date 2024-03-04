import os
import webbrowser
import time

CYPHER_STORE_URL = 'http://sana.dubbed.tech'
TEMPLE_FOLDER = 'sana_temple'
CYPHER_FOLDER = 'my_cyphers'


def print_slowly(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def check_folder(folder_path, file_extension='*.png', expected_count=1):
    files = [f for f in os.listdir(folder_path) if f.endswith(file_extension)]
    file_count = len(files)
    if file_count == expected_count:
        return True, files
    return False, files


def initialize_folders():
    clear_screen()
    print_slowly("Welcome to the world of Sana...")
    time.sleep(1.5)
    print_slowly("Loading...")
    clear_screen()
    print("____________________________")
    time.sleep(1)   
    print(" ___    __    _  _    __")
    time.sleep(1)   
    print("/ __)  /__\  ( \( )  /__\ ")  
    time.sleep(1)
    print("\__ \ /(__)\  )  (  /(__)\ ") 
    time.sleep(1)
    print("(___/(__)(__)(_)\_)(__)(__) ")
    time.sleep(1)   
    print("----------------------------")
    time.sleep(2)
    for folder in [TEMPLE_FOLDER, CYPHER_FOLDER]:
        os.makedirs(folder, exist_ok=True)


def onboarding_phase():
    # Custom introduction sequence
    print_intro_story()

    # Temple selection
    # while check_sana_temple_folder() != 1:
    #     input("Press Enter once you've made your selection.")
    #     valid, _ = check_folder(TEMPLE_FOLDER)
    #     if valid:
    #         break
    #     print_onboarding_error()
    # TODO: check sana temple folder

    print_slowly("Great, you've chosen your first temple...")
    # Continue with the story...
    # TODO: Cypher explanation
    input("Get your free cypher at sana.dubbed.tech. Press enter to open the browser.")
    webbrowser.open(CYPHER_STORE_URL)


def print_intro_story():
    print_slowly("Your eyes flutter open, each blink shedding a layer of the dreamworld.\n"
    "As clarity washes over you in the warm embrace of the sun's rays, you find\n"
    "yourself cradled by the earth, outside, under an expansive cerulean sky.\n"
    "The world around you is vibrant, alive. Before you, a trail carves a path\n"
    "through a lush, grassy valley, inviting you to wander. To your right, a forest\n"
    "of towering trees whispers ancient secrets, their leaves dancing in the light breeze.\n"
    "To the left, majestic mountains rise, their peaks touching the sky, a testament\n"
    "to the enduring beauty of nature. Above, a few wisps of clouds drift lazily,\n"
    "painting stories in the otherwise uninterrupted blue.\n"
    "At the trail's end, an enigmatic structure shaped like an egg beckons.\n"
    "With each step towards it, your curiosity deepens.\n"
    "What mysteries does the structure hold? What stories are etched into its walls?\n"
    "Imagine the structure. What form does it take in your mind's eye?\n"
    "Select an image from the 'sana_temple' folder that resonates with your vision.\n"
    "Feel free to delete the others, leaving only the one that speaks to you—or,\n"
    "if none capture the essence, replace them with one of your own creations.\n")
    pass


def print_onboarding_error():
    clear_screen()
    print("Please ensure there is only a single PNG file in the 'sana_temple' folder to continue.")
    # Include instructions for correcting the issue


def sanadex_phase():
    clear_screen()
    print_slowly("Welcome to your Sanadex.")
    valid, cyphers = check_folder(CYPHER_FOLDER, expected_count=0)  # 0 means don't check count
    if not valid:
        print("No Cyphers found. Please add some to your 'my_cyphers' folder.")
    else:
        print("Your Cyphers:")
        for i, cypher in enumerate(cyphers, start=1):
            print(f"{i}. {cypher}")
        # Optionally, let the user select a cypher to view more information


def main():
    initialize_folders()
    onboarding_phase()
    sanadex_phase()


if __name__ == "__main__":
    main()
