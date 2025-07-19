import argparse
import json
from PyPDF2 import PdfReader
def extract_outline(pdf_path):
    reader = PdfReader(pdf_path)
    title = reader.metadata.title or ""
    outline = []
    for i, page in enumerate(reader.pages, start=1):
        text = page.extract_text().splitlines()
        for line in text:
            if line.isupper():  
                outline.append({"level": "H1", "text": line, "page": i})
    return {"title": title, "outline": outline}
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
