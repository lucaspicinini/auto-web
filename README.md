# RX Auto Web

Ferramenta de automação para operações da Rexpeita - v0.1.0:

- Geração automática de logística reversa nos correios
- Mais funções em futuras versões


## Configuração do Ambiente

### Opção 1: Usando Poetry (Recomendado)

1. Instale o Poetry:
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. Clone o repositório:
   ```bash
   git clone https://github.com/lucaspicinini/auto-web.git
   cd auto-web
   ```

3. Instale as dependências:
   ```bash
   poetry install
   ```

4. Ative o ambiente virtual:
   ```bash
   poetry shell
   ```

### Opção 2: Usando pip e venv

1. Clone o repositório:
   ```bash
   git clone https://github.com/lucaspicinini/auto-web.git
   cd auto-web
   ```

2. Crie um ambiente virtual:
   ```bash
   python -m venv .venv
   ```

3. Ative o ambiente virtual:
   - No Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - No macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Configuração das Variáveis de Ambiente

1. Copie o arquivo `.env.example` para criar seu próprio arquivo `.env`:
   ```bash
   cp .env.example .env
   ```

2. Edite o arquivo `.env` com suas credenciais e configurações:
   ```
   # Credentials
   OPENCART_USERNAME=seu_usuario_opencart
   OPENCART_PASSWORD=sua_senha_opencart
   CORREIOS_USERNAME=seu_email@exemplo.com
   CORREIOS_PASSWORD=sua_senha_correios
   CORREIOS_ADMIN_CODE=seu_codigo_admin_correios

   # Sender configuration
   SENDER_CITY=sua_cidade
   SENDER_POSTCARD=seu_codigo_postal
   SENDER_POSTCODE=seu_cep
   SENDER_LABEL=seu_nome_ou_empresa
   SENDER_ADDRESS_NUMBER=seu_numero
   SENDER_DDD=seu_ddd
   SENDER_TELEPHONE=seu_telefone
   ```

## Estrutura do Projeto

- `config.py`: Carrega as configurações do arquivo `.env`
- `.env`: Armazena credenciais e configurações sensíveis (não versionado)
- `.env.example`: Exemplo das variáveis de ambiente necessárias (versionado)
- `requirements.txt`: Lista de dependências para pip
- `pyproject.toml`: Configuração para Poetry e outras ferramentas


## Desenvolvimento

### Testes

Se você estiver usando Poetry:
```bash
poetry run pytest
```

Se estiver usando venv:
```bash
pytest
```

### Formatação de Código

Com Poetry:
```bash
poetry run black .
```

Com venv:
```bash
black .
```
