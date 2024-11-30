import spacy
import json

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Load scraped data
with open("data.json") as f:
    products = json.load(f)

# Define attributes to extract
attributes = ["color", "material", "pattern"]

# Predefined keywords for simplicity (extend this list)
keywords = {
    "color": ["red", "blue", "green", "yellow", "black", "white"],
    "material": ["cotton", "silk", "wool", "leather"],
    "pattern": ["striped", "polka dot", "floral", "plain"],
}

def extract_features(description):
    doc = nlp(description)
    extracted = {attr: [] for attr in attributes}
    for token in doc:
        for attr, values in keywords.items():
            if token.text.lower() in values:
                extracted[attr].append(token.text.lower())
    return extracted

# Enrich product data with features
for product in products:
    if product["description"]:
        product["features"] = extract_features(product["description"])

# Save enriched data
with open("enriched_data.json", "w") as f:
    json.dump(products, f, indent=4)

