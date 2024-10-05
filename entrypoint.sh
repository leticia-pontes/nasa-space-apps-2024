#!/bin/bash

echo "Baixando arquivo..."
python download_file.py

if [ $? -ne 0 ]; then
    echo "Erro ao baixar arquivo. Saindo..."
    exit 1
fi

echo "Iniciando o servidor..."
python app.py
