FROM python:3.12-slim

# Instala o Poetry
RUN pip install poetry

WORKDIR /app

# Copia os arquivos de dependências
COPY pyproject.toml poetry.lock* ./

# Configura o Poetry para não criar ambiente virtual dentro do container
RUN poetry config virtualenvs.create false && poetry install --no-root

# Copia o código
COPY . .