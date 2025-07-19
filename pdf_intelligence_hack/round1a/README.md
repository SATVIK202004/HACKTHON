# Round 1A: PDF Outline Extraction

## Overview
Extract title and headings (H1, H2, H3) from PDFs into JSON.

## Usage
```bash
mkdir -p output
docker build -t pdf-outline:1.0 .
docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output pdf-outline:1.0
