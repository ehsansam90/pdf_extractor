from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
from extractor import extract_text_from_pdf
from model import process_text  # Now returns both entities and phone numbers

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        if "file" not in request.files:
            return "No file part"

        file = request.files["file"]
        if file.filename == "":
            return "No selected file"

        filename = secure_filename(file.filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path)

        # Extract text from PDF
        extracted_text = extract_text_from_pdf(file_path)

        # Process text using ML model (NER) and extract phone numbers
        ner_results, phone_numbers = process_text(extracted_text)

        return render_template("index.html", extracted_text=extracted_text, ner_results=ner_results, phone_numbers=phone_numbers)

    return render_template("index.html", extracted_text=None, ner_results=None, phone_numbers=None)

if __name__ == "__main__":
    app.run(debug=True)
