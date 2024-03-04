import os
import webbrowser
import time

CYPHER_STORE_URL='http://sana.dubbed.tech'

# Function to print each letter with a delay
def print_slowly(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # Move to the next line after the message

# Clear the screen
def clear_screen():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For macOS and Linux
    else:
        os.system('clear')

# Function to check the sana_temple folder
def check_sana_temple_folder():
    folder_path = 'sana_temple'
    png_files = [f for f in os.listdir(folder_path) if f.endswith('.png')]
    if len(png_files) == 0:
        clear_screen()
        print("")
    elif len(png_files) > 1:
        clear_screen()
        print("It seems like you've chosen more than one temple.")
        print("Please leave only a single PNG file in the sana_temple folder to continue.")
        print("You may change you temple at any time.")
    else:
        file_path = os.path.join(folder_path, png_files[0])
        clear_screen()
        if os.path.isfile(file_path):
            print(f"Excellent choice.")
        else:
            print("Please ensure the selected file is a PNG.")
    return len(png_files)

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

# Ask the user to press Enter
input("To continue, please type your name then press enter")

clear_screen()
# Display a message

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
"if none capture the essence, replace them with one of your own creation.\n")
input("Press Enter once you've made your selection.")
time.sleep(0.5)
print("Select one of the images in the 'temples' folder")
time.sleep(0.5) 
print("by deleting images until the one you chose is the only one left.")
time.sleep(0.5)
print("Alternatively delete all of them and replace them with your own!")
time.sleep(0.5)
input("Press enter when you've selected your photo.")
 # Check the folder after user input
while check_sana_temple_folder() != 1:
  print("Please ensure there is only a single PNG file in the 'sana_temple' folder to continue.")
  time.sleep(2)
  print("Select one of the images in the 'temples' folder")
  time.sleep(0.5) 
  print("by deleting images until the one you chose is the only one left.")
  time.sleep(0.5)
  print("Alternatively delete all of them and replace them with one of your own!")
  time.sleep(0.5)
  input("Press enter when you've selected your photo.")
print_slowly("Great, you've chosen your first temple. Temples in the Sana realm represent our heads and our hearts.")
print_slowly("Where our most hopeful ideas that are closest to our hearts reside and realize themselves into creatures called Cyphers.")
print_slowly("Cyphers grow and change with us as we share them with people.")
print_slowly("Who they are, what they grow into, and how they change is ultimately up to you.")
input("Get your free cypher at sana.dubbed.tech. Press enter to open the browser.")
webbrowser.open(CYPHER_STORE_URL)

# Check if the folder exists
if not os.path.exists('my_cyphers'):
    # Create the folder
    os.makedirs('my_cyphers')
# If the folder exists, do nothing

while check_sana_temple_folder() < 1:
  input("Please collect a cypher and add it into your my_cyphers folder to continue.")





