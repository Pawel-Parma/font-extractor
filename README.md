# font-extractor
Extracts font characters from a font file and saves them as images

## Usage:

### 1. Setup
Set constants in the script
```python
FONTFORGE_FILTER = False  # FontForge internal filter: font[glyph].isWorthOutputting()
WORKING_DIR = ""  # ABSOLUTE PATH IS RECOMMENDED
FONT_FILE = ""  # File name containing the font (I only tried: { "*.TTF" } files)
```

### 2. Run:

#### — in FontForge app:
Download link: https://fontforge.org/en-US/downloads/  
You need to open a font file and press `ctrl + .` to open python console.
#### — build fontforge library from source:
Download link: https://github.com/fontforge/fontforge
Then run the script with python:

##### - Linux
```bash
python3 main
```
##### - Windows
```cmd
python main
```

### Notes

The uppercase characters are overwritten by lowercase ones. 
To solve this, I added count to the end of the name, and made everything lowercase

FontForge doesn't show prints, you can write messages to file, but exceptions are conveniently shown in  
a warning window, hence the strange code of adding everything to a list and raising an error with the list as a message.

Font file opening isn't done with context manager, because when it is closed FontForge closes
