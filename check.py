import pytesseract
import re
from PIL import Image

# Set the path to the Tesseract executable (modify this to match your system)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

# Load the image
image = Image.open('id.jpg')

# Use Tesseract to extract text from the image
extracted_text = pytesseract.image_to_string(image)

print(extracted_text)
# Define a regular expression pattern to match the desired format (ignore case)
pattern = r'BL\s*[._\-\s]*EN\s*[._\-\s]*([a-zA-Z0-9]{10})'

# Use regular expressions to find the matching pattern in the extracted text (case-insensitive)
matches = re.findall(pattern, extracted_text, re.IGNORECASE)

if matches:
    print("Found matching strings:")
    for match in matches:
        # Convert the match to lowercase
        match = match.lower()
        print("bl.en." + match)
else:
    print("No matching strings were found in the text.")