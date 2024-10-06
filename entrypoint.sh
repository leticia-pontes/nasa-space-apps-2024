#!/bin/bash

set -e

echo "Diretório atual: $(pwd)"

if [ -d "src/utils/" ]; then
    cd src/utils/
else
    echo "O diretório src/utils/ não existe. Saindo..."
    exit 1
fi

if [ -f "download_file.py" ]; then
    python download_file.py
else
    echo "O arquivo download_file.py não foi encontrado no diretório src/utils/. Saindo..."
    exit 1
fi

echo "Arquivo baixado com sucesso."

cd ../..

echo "Iniciando o servidor..."
python src/app.py
