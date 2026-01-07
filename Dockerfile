# 1. Usar 3.11 para garantir compatibilidade com versões novas do Pandas
FROM python:3.11-slim

# 2. Instalar dependências de sistema (necessário para compilar algumas libs de Python)
RUN apt-get update && apt-get install -y gcc && rm -rf /var/lib/apt/lists/*

# 3. Direcionar para a pasta do app
WORKDIR /app

# 4. Instalar as bibliotecas
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiar seus scripts (parser_estadao.py, app.py, etc.)
COPY . .

# 6. Executar o scraper
CMD ["python", "app.py"]
