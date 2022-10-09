from PIL import Image, ImageGrab
import pytesseract
from googletrans import Translator
from pathlib import Path

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

# img = Image.open(Path(rootdir, 'Annotation 2022-10-08 232023.png'))

# # OCR
# result = pytesseract.image_to_string(img)

# # Translation
# translator = Translator()
# trans = translator.translate(result, dest='english')
# result_translated = str(trans.text)


while True:
    input("Press [Enter] to translate clipboard:")
    print("\n -------------------------------------------------------------------")
    print(translate_img_from_clipboard())
    print("\n -------------------------------------------------------------------")