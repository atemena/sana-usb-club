import os
import webbrowser
import time
import user_profile
import platform

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
    if platform.system() == 'Windows':
        os.system('cls')
    # For macOS and Linux
    else:
        os.system('clear')

# Get the directory of the script
script_dir = os.path.dirname(os.path.realpath(__file__))
sana_temple_dir = os.path.join(script_dir, 'sana_temple')
cyphers_dir = os.path.join(script_dir, 'cyphers')

# Function to check the sana_temple folder
def num_files_in_sana_temple_folder():
    png_files = [f for f in os.listdir(sana_temple_dir) if f.endswith('.png')]
    return len(png_files)

def get_temple_path():
    for file in os.listdir(sana_temple_dir):
        if file.endswith('.png'):
            return os.path.join('sana_temple', file)
    return None

def save_cyphers_to_profile():
    # Get the list of PNG files in the 'cyphers' folder
    cypher_files = [f for f in os.listdir(cyphers_dir) if f.endswith('.png')]

    # Create a list of cyphers
    cyphers = []
    for file in cypher_files:
        # Prompt the user to input a name and species for the cypher
        name = input(f"Enter a name for Cypher '{file}': ")
        species = input(f"Enter a species for the Cypher '{file}': ")

        # Create a dictionary for the cypher
        cypher = {
            'name': name,
            'species': species,
            'path': os.path.join(script_dir,'cyphers', file)
        }
        cyphers.append(cypher)

    # Save the list of cyphers in the user profile
    user_profile.set_key('cyphers', cyphers)

def num_files_in_cyphers_folder():
    # Get the list of files in the 'cyphers' folder
    files = os.listdir(cyphers_dir)

    # Count the number of PNG files
    png_files = [f for f in files if f.endswith('.png')]

    return len(png_files)

def print_cypher_names(upper=True, new_line=True):
    # Get the list of cyphers from the user profile
    cyphers = user_profile.get_profile()['cyphers']

    # Print the name of each cypher in uppercase
    for cypher in cyphers:
        name = cypher['name'].upper() if upper else cypher['name']
        print(name, end='!\n') if new_line else print(name, end='. ')
        time.sleep(0.5)

def cypher_copy():
    # Get the list of cyphers from the user profile
    cyphers = user_profile.get_profile()['cyphers']

    # Print a message based on the number of cyphers
    if len(cyphers) == 1:
        return "Cypher appears"
    else:
        return "Cyphers appear"

def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


clear_screen()
print_slowly("Welcome to the world of Sana")
print_slowly("press control-c to exit at any time.")
print_slowly("Loading core memory...")
ensure_dir(sana_temple_dir)
ensure_dir(cyphers_dir)
time.sleep(1.5)
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
name = input("What is your name?\n")
user_profile.set_key('name', name)

clear_screen()
# Display a message

print_slowly("Your eyes flutter open, each blink shedding a layer of the dreamworld.\n"
"As clarity washes over you in the warm embrace of the sun's rays, you find\n"
"yourself cradled by the earth, outside, under an expansive cerulean sky.\n\n"
"The world around you is vibrant, alive. Before you, a trail carves a path\n"
"through a lush, grassy valley, inviting you to wander. To your right, a forest\n"
"of towering trees whispers ancient secrets, their leaves dancing in the light breeze.\n"
"To the left, majestic mountains rise, their peaks touching the sky, a testament\n"
"to the enduring beauty of nature. Above, a few wisps of clouds drift lazily,\n"
"painting stories in the otherwise uninterrupted blue.\n\n"
"At the trail's end, an enigmatic structure shaped like an egg beckons.\n"
"You feel your body move closer as if not under your own control.\n"
"With each step towards it, your curiosity deepens.\n"
"What mysteries does the structure hold? What stories are etched into its walls?\n\n"
)
time.sleep(0.5)
print_slowly("Imagine the structure. What form does it take in your mind's eye?\n"
"Select an image from the 'sana_temple' folder that resonates with your vision.\n"
"Feel free to delete the others, leaving only the one that speaks to you—or,\n"
"if none capture the essence, replace them with one of your own creation.\n")
input("Press Enter once you've made your selection.")
time.sleep(0.5)
print("Select one of the images in the 'temples' folder")
time.sleep(0.5) 
print("by deleting images (pngs) until the one you chose is the only one left.")
time.sleep(0.5)
print("Alternatively delete all of them and replace them with your own!")
time.sleep(0.5)
input("Press enter when you've selected your photo.")
 # Check the folder after user input
while True:
    num_photos = num_files_in_sana_temple_folder()
    if num_photos != 1:
        print("Please ensure there is only a single PNG file in the 'sana_temple' folder to continue.")
        time.sleep(2)
        print("Select one of the images in the 'temples' folder")
        time.sleep(0.5) 
        print("by deleting images until the one you chose is the only one left.")
        time.sleep(0.5)
        print("Alternatively delete all of them and replace them with your own!")
        time.sleep(0.5)
        input("Press enter when you've selected your temple.")
    else:
        # Get the path of the temple image
        temple_path = get_temple_path()

        # Save the temple path into the user profile
        user_profile.set_key('temple', temple_path)

        break
print_slowly("Great, you've chosen your first temple. Temples in Sana represent our heads and our hearts.")
print_slowly("Where our most hopeful ideas that are closest to our hearts reside and realize themselves into creatures called Cyphers.")
print_slowly("Cyphers grow and change with us as we share them with people.")
print_slowly("Who they are, what they grow into, and how they change is ultimately up to you.")
print_slowly("Get your free Cypher at sana.dubbed.tech and preserve it in your `cyphers` folder.")
input("Press enter to open the browser.\n")
webbrowser.open(CYPHER_STORE_URL)
input("Once you've preserved at least one Cypher, press enter to continue.")
clear_screen()

while True:
    if num_files_in_cyphers_folder() < 1:
        input("Please preserve a Cypher and add it into your `cyphers` folder to continue.")
    else:
        save_cyphers_to_profile()
        clear_screen()
        break

print_slowly("Suddenly you find yourself within the temple, you can feel it's familiar energy eminating from it's walls.")
print_slowly("A ray of light shines from a circular hole where the very top of the structure would be.")
print_slowly("The singular almost spherical wall is covered in carvings that you've seen before but can't understand.")
print_slowly("Almost as if instinct has taken over your body, you call out into the empty room.")
print_cypher_names()
time.sleep(1)
print("\n")
print_slowly("The ray of light slowly intensifies as it begins to blind you.")
print_slowly(f"the light fades. You hear cries in the distance as your eyes adjust. In front of you your {cypher_copy()}.")
print_slowly("The Cypher's eyes meet yours as your mouth whispers their name.")
print_cypher_names(upper=False, new_line=False)
print_slowly("\nYou can feel how eager and ready they are for this new adventure, with you as their leader...")
input("Press enter to continue.")
time.sleep(1) 
print("____________________________")
time.sleep(0.5) 
print(" ___    __    _  _    __")
time.sleep(0.5)
print("/ __)  /__\  ( \( )  /__\ ")
time.sleep(0.5)
print("\__ \ /(__)\  )  (  /(__)\ ")
time.sleep(0.5)
print("(___/(__)(__)(_)\_)(__)(__) ")
time.sleep(0.5)
print("----------------------------")
time.sleep(0.5)

print_slowly(f"Congratulations {user_profile.get_profile()['name']}!\nYou've taken your first steps into the world of Sana.")
print_slowly("Your journey has only just begun.")
print_slowly("Your data lives in your `sana_profile.json` file.")
print_slowly("You can access your profile at any time or change it by going through this core memory again.")
print_slowly("Stay tuned for more ways to interact with Sana and your Cyphers soon!")


