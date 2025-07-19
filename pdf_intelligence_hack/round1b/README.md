# Round 1B: Persona‑Driven Ranking

## Overview
Rank and extract top sections from multiple PDFs given a persona and job-to-be-done.

## Usage
```bash
export PERSONA="PhD researcher in comp-bio"
export TASK="Prepare literature review on genome editing"
mkdir -p output
docker build -t pdf-ranker:1.0 .
docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output pdf-ranker:1.0
