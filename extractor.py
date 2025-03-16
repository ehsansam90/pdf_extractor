import pdfplumber
import re

def extract_text_from_pdf(pdf_path):
    """Extracts and cleans text from a PDF file."""
    extracted_text = []

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                cleaned_text = clean_text(text)
                extracted_text.append(cleaned_text)

    return "\n".join(extracted_text)

def clean_text(text):
    """Cleans extracted text by removing unnecessary characters and formatting."""
    text = re.sub(r'\s+', ' ', text)  # Remove extra spaces and newlines
    text = re.sub(r'[^a-zA-Z0-9.,!?\'\" ]', '', text)  # Keep only readable characters
    text = text.strip()  # Trim leading and trailing spaces
    return text
