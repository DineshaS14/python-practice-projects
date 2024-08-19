# Import the Figlet class from the pyfiglet module
from pyfiglet import Figlet

# Install the pyfiglet module using pip: pip install pyfiglet

# Import additional modules
import random
import sys

# Create a Figlet object to use for generating ASCII art
figlet = Figlet()

# Handle command-line arguments
if len(sys.argv) == 1:
    # If no arguments are provided, use a random font
    font_name = random.choice(figlet.getFonts())
elif len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font'):
    # If the user provides a font name, use it
    font_name = sys.argv[2]
    # Check if the font is available
    if font_name not in figlet.getFonts():
        print("Invalid usage")
        sys.exit(1)
else:
    print("Invalid usage")
    sys.exit(1)

# Set the font for the Figlet object
figlet.setFont(font=font_name)

# Prompt the user to enter text
text = input("Enter text: ")

# Generate and print the ASCII art
print(figlet.renderText(text))