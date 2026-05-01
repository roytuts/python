import cv2
from PIL import Image
import pytesseract
import os
import glob
import argparse

# Configure path to Tesseract executable if needed (Windows users)
# Example: r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# Uncomment and set the path if required
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def preprocess_image(image_path: str) -> str:
    """
    Preprocess the image for better OCR accuracy.
    Converts to grayscale and applies thresholding.
    Returns the path to the processed image.
    """
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

    processed_path = "processed.png"
    cv2.imwrite(processed_path, thresh)
    return processed_path

def extract_text(image_path: str, lang: str = "eng") -> str:
    """
    Extract text from an image using Tesseract OCR.
    """
    processed_path = preprocess_image(image_path)
    text = pytesseract.image_to_string(Image.open(processed_path), lang=lang)
    return text

def save_text(image_path: str, text: str, output_dir: str = "outputs"):
    """
    Save extracted text into a separate file for each image.
    """
    os.makedirs(output_dir, exist_ok=True)
    base_name = os.path.splitext(os.path.basename(image_path))[0]
    output_file = os.path.join(output_dir, f"{base_name}.txt")
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Saved extracted text to {output_file}")

def process_path(path: str, lang: str = "eng"):
    """
    Handle both single image file and folder of images.
    """
    if os.path.isfile(path):
        text = extract_text(path, lang)
        save_text(path, text)
    elif os.path.isdir(path):
        files = glob.glob(os.path.join(path, "*.png")) + glob.glob(os.path.join(path, "*.jpg"))
        if not files:
            print(f"No images found in folder '{path}'.")
            return
        for file in files:
            text = extract_text(file, lang)
            save_text(file, text)
    else:
        print(f"Path '{path}' is not valid.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract text from images using OCR")
    parser.add_argument("path", help="Path to an image file or a folder containing images")
    parser.add_argument("--lang", default="eng", help="Language code for OCR (default: eng)")
    args = parser.parse_args()

    process_path(args.path, args.lang)
