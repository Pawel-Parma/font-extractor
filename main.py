# Run in FontForge app: (You need to open a font and press 'ctrl + .')
# https://fontforge.org/en-US/downloads/
# or build fontforge library from source:
# https://github.com/fontforge/fontforge
from fontforge import *


FONTFORGE_FILTER = False  # FontForge internal filter: font[glyph].isWorthOutputting()
WORKING_DIR = ""  # ABSOLUTE PATH IS RECOMMENDED
FONT_FILE = ""  # File name containing the font (I only tried: { "*.TTF" } files)

font_folder = "extracted_fonts"
extension = ".png"
source = f"{WORKING_DIR}/{FONT_FILE}"
dest = f"{WORKING_DIR}/{font_folder}/{'{}'}{extension}"

# The uppercase characters are overwritten by lowercase ones.
# To solve this, I added count to the end of the name, and made everything lowercase.
dict_count = {}
# FontForge doesn't show prints, you can write messages to file, but exceptions are conveniently shown in
# a warning window, hence the strange code of adding everything to a list and raising an error with a message.
message_list = ["\nMessage:\n"]
counter = 0

# Font file opening isn't done with context manager, because when it is closed, FontForge closes.
font = open(source)
for glyph in font:
    if not font[glyph].isWorthOutputting() or FONTFORGE_FILTER:
        continue

    name = font[glyph].glyphname.lower()

    if name in dict_count:
        dict_count[name] += 1

    else:
        dict_count[name] = 0

    name += f"_{dict_count[name]}"
    font[glyph].export(dest.format(name))
    message_list += [f"{counter} - {name}"]

    counter += 1

# "print" message
message_list.append("End of message\n")
real_message = "\n".join(message_list)
raise Exception(real_message)
