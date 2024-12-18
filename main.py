import pytesseract
from PIL import Image
import cv2
import numpy as np

def extract_text_from_image(image_path):
    """
    Extracts text from an image using pytesseract.  Includes preprocessing steps.

    Args:
        image_path: Path to the image file.

    Returns:
        The extracted text as a string, or None if extraction fails.
    """
    try:
        # 1. Load the image
        img = cv2.imread(image_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # pytesseract expects RGB

        # 2. Preprocessing (Optional but often necessary for noisy images)
        #  (Experiment with these steps to find what works best for your image)
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)  # Reduce noise
        thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1] #Binarization


        # 3. Use pytesseract to perform OCR
        text = pytesseract.image_to_string(thresh) #Pass the preprocessed image

        return text.strip()  # Remove leading/trailing whitespace

    except Exception as e:
        print(f"Error extracting text: {e}")
        return None


# Example usage:
image_path = "capcha.png"  # Replace with the actual path to your image
extracted_text = extract_text_from_image(image_path)

if extracted_text:
    print(f"Extracted text:\n{extracted_text}")
else:
    print("Text extraction failed.")