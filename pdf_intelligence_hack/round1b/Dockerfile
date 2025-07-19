---

## round1b/Dockerfile  
```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY rank_sections.py ./
ENTRYPOINT ["python", "rank_sections.py", "--input", "/app/input", "--persona", "${PERSONA}", "--task", "${TASK}"]
