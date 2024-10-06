FROM python:3.9-slim
RUN apt-get update && apt-get install -y \
    dos2unix \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN dos2unix entrypoint.sh utils/download_file.py
RUN chmod +x entrypoint.sh
EXPOSE 8050
ENTRYPOINT ["./entrypoint.sh"]
