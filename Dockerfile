# Use a imagem base do Python 3.9 slim
FROM python:3.9-slim

# Instale os pacotes necessários
RUN apt-get update && apt-get install -y \
    curl \
    gnupg \
    apt-transport-https \
    dos2unix \
    && rm -rf /var/lib/apt/lists/*

# Defina o diretório de trabalho
WORKDIR /app

# Copie o arquivo de dependências para o contêiner
COPY requirements.txt .

# Instale as dependências listadas no requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copie todo o conteúdo do diretório atual para o contêiner
COPY . .

# Copie o arquivo de chave do Google Cloud para o contêiner
COPY key.json /app/key.json

# Converta os arquivos de script para o formato Unix, se necessário
RUN dos2unix entrypoint.sh src/utils/download_file.py

# Defina a variável de ambiente GOOGLE_APPLICATION_CREDENTIALS
ENV GOOGLE_APPLICATION_CREDENTIALS="/app/key.json"

# Torne o script entrypoint executável
RUN chmod +x entrypoint.sh

# Exponha a porta 5000 para o servidor
EXPOSE 5000

# Defina o script entrypoint para ser executado quando o contêiner iniciar
ENTRYPOINT ["./entrypoint.sh"]
