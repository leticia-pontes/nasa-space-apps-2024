# NASA Space Apps Project 2024

Este projeto é uma aplicação interativa de visualização de dados usando Dash e Plotly, que apresenta um mapa interativo com dados de cidades e suas populações.

## Tecnologias Utilizadas

- Python 3.9
- Dash
- Plotly
- Pandas
- Docker

## Pré-requisitos

Antes de executar o projeto, verifique se você tem o seguinte instalado:

- [Docker](https://www.docker.com/get-started)
- [WSL](https://docs.microsoft.com/en-us/windows/wsl/install) (se estiver usando Windows)

## Configuração

1. **Clone o repositório**:
   ```bash
   git clone <URL-do-repositório>
   cd <nome-do-repositório>
   ```

2. **Construir a Imagem Docker**:
   Na raiz do projeto, execute o comando abaixo para construir a imagem Docker:
   ```bash
   docker build -t nasa-project-2024 .
   ```

3. **Executar o Container**:
   Após a construção da imagem, execute o container com o comando:
   ```bash
   docker run -d -p 8050:8050 --name nasa-project-container nasa-project-2024
   ```

## Acessar a Aplicação

Após executar o container, você pode acessar a aplicação interativa no seu navegador em:
```
http://localhost:8050/
```

## Estrutura do Projeto

```plaintext
.
├── Dockerfile
├── README.md
├── __pycache__
├── app.py
├── assets
├── entrypoint.sh
├── image_processor.py
└── utils
    └── download_file.py
```

## Como Funciona

1. **Entrypoint**: O `entrypoint.sh` é o script de inicialização que baixa dados necessários antes de iniciar a aplicação.

2. **Aplicação Dash**: O `app.py` configura a aplicação Dash, define o layout e os callbacks para interação com o usuário.

3. **Dependências**: As dependências são instaladas no container durante o processo de build através do `Dockerfile`.

## Contribuição

Se você quiser contribuir para este projeto, sinta-se à vontade para fazer um fork e enviar um pull request.

## Licença

Este projeto está licenciado sob a MIT License - consulte o arquivo [LICENSE](LICENSE) para mais detalhes.
```

### Personalizações

- **URL do repositório**: Substitua `<URL-do-repositório>` pela URL real do seu repositório Git.
- **Nome do repositório**: Altere `<nome-do-repositório>` para o nome do diretório do seu projeto.

Sinta-se à vontade para ajustar o conteúdo conforme necessário!
