# font-extractor

Extracts font characters from a font file using fontforge and saves them as images.

## Usage:

### 1. Setup

Set constants in the script:
```python
FONTFORGE_FILTER = False  # FontForge internal filter: font[glyph].isWorthOutputting()
WORKING_DIR = ""  # ABSOLUTE PATH IS RECOMMENDED
FONT_FILE = ""  # File name containing the font (I only tried: { "*.TTF" } files)
```

### 2. Run:

- #### In FontForge app:
  Download link: https://fontforge.org/en-US/downloads/  
  You need to open a font file and press `ctrl + .` to open python console.  
  Copy the script and paste it into the console.  
  Press `OK` to run the script.

- #### Build fontforge library from source:
  Download link: https://github.com/fontforge/fontforge
 
  > **Note:**  
  > Halt!  
  > Maybe you don't need to do this.  
  > There is a chance that you can install the library with pip.  
  > At the time of writing this, there is an opened issue on fontforge GitHub titled:  
  > `fontforge as a pip-installable Python module`  
  > Issue link: https://github.com/fontforge/fontforge/issues/4377  
  > If you are reading this, and the issue is closed, you can probably install the library with pip:

  Then run the script with python:

  - ##### Linux
    ```bash
    python3 main
    ```
    
  - ##### Windows
    ```cmd
    python main
    ```

### Notes

The uppercase characters are overwritten by lowercase ones. 
To solve this, I added count to the end of the name, and made everything lowercase.

FontForge doesn't show prints, you can write messages to file, but exceptions are conveniently shown in  
a warning window, hence the strange code of adding everything to a list and raising an error with a message.

Font file opening isn't done with context manager, because when it is closed FontForge closes.
