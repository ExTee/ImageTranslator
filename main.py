from PIL import Image, ImageGrab
import pytesseract
from googletrans import Translator
from pathlib import Path
import glob
import os.path

rootdir = Path(__file__).parent.resolve()

def translate_img_from_clipboard():
    # Read Clipboard
    img = ImageGrab.grabclipboard()
    
    # OCR
    result = pytesseract.image_to_string(img)

    # Translation
    translator = Translator()
    trans = translator.translate(result, dest='english')
    result_translated = str(trans.text)

    return result_translated


def get_latest_png_in_folder(folder_path='~/Desktop'):
    file_type = r'/*.png'
    files = glob.glob(folder_path + file_type)
    max_file = max(files, key=os.path.getctime)
    print(max_file)


while True:
    input("Press [Enter] to translate clipboard:")
    print("\n -------------------------------------------------------------------")
    print(translate_img_from_clipboard())
    print("\n -------------------------------------------------------------------")