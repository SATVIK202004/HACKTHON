import argparse
import json
from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer

def load_documents(input_dir):
    return []

def rank_by_tfidf(sections, persona, task):
    return []

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--persona", required=True)
    parser.add_argument("--task", required=True)
    args = parser.parse_args()
    docs = load_documents(args.input)
    ranked = rank_by_tfidf(docs, args.persona, args.task)
    print(json.dumps(ranked, indent=2))
