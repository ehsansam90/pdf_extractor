from transformers import pipeline
import numpy as np
import re

nlp_pipeline = pipeline("ner", model="dslim/bert-base-NER", aggregation_strategy="simple")

def extract_phone_numbers(text):
    phone_pattern = re.compile(r"\(?\b\d{3}[-.)\s]?\d{3}[-.\s]?\d{4}\b")
    return list(set(phone_pattern.findall(text)))  # Remove duplicates

def process_text(text):
    nlp_results = nlp_pipeline(text)

    formatted_results = []
    for entity in nlp_results:
        entity_data = {
            "Entity": entity["entity_group"],  # ORG, PER, LOC, MISC, etc.
            "Text": entity["word"],  # Extracted word
            "Score": round(float(entity["score"]), 4)  # Round the score
        }
        formatted_results.append(entity_data)

    phone_numbers = extract_phone_numbers(text)

    return formatted_results, phone_numbers
