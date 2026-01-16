import re
import pytesseract
from PIL import Image
from config import TESSERACT_CMD

pytesseract.pytesseract.tesseract_cmd = TESSERACT_CMD

def invoice_jpg_details(extracted_text):
    # Regex para extrair dados do OCR
    invoice_no = re.search(r"Invoice\s*(?:#\s*)?(\d+)", extracted_text)
    invoice_date = re.search(r"(\d{4}-\d{2}-\d{2})", extracted_text)
    company_name = re.search(r"(.*?)\s+INVOICE", extracted_text)
    total_due = re.search(r"Total\s+([\d,.]+)", extracted_text)

    return (
        invoice_no.group(1) if invoice_no else None,
        invoice_date.group(1) if invoice_date else None,
        company_name.group(1).strip() if company_name else None,
        total_due.group(1) if total_due else None
    )

def process_image_ocr(image_path):
    img = Image.open(image_path)
    extracted_text = pytesseract.image_to_string(img)
    return invoice_jpg_details(extracted_text)