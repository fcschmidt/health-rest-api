# Health Rest API Challenge :woman_health_worker: :man_health_worker: :pill:

Challenge for Python Developer.

## Preparando o Ambiente

**Download do Projeto via `git clone`:**

`$ git clone git@github.com:fcschmidt/health-rest-api.git`.

**Acesse a pasta do projeto:**

`$ cd health-rest-api`.

**Adicionando as variáveis de ambiente:**

**Criando um arquivo `.env`** ou renomeie o arquivo `.env_sample` para `.env`, com as informações abaixo.

```text
export FLASK_APP=manage.py
export FLASK_ENV=development
export FLASK_RUN_HOST='localhost'
export FLASK_RUN_PORT=5000
DEBUG=True
DATABASE_URL=postgresql+psycopg2://username:password@localhost:5432/prescriptions
```

Sobre as configurações do SQLAlchemy: [ https://docs.sqlalchemy.org/en/latest/core/engines.html#database-urls]( https://docs.sqlalchemy.org/en/latest/core/engines.html#database-urls)

Caso não seja inserido um caminho no path `DATABASE_URL` no arquivo `.env`. 
Por default ele irá criar uma base de dados usando SQLite, no caminho `sqlite:////var/tmp/prescriptions_dev.sqlite`.

**Chaves de Autorização:**

Renomeie o script de `authorization_keys.sample.py` para `authorization_keys_test.py`.

Foi necessário criar um arquivo separado, pois ao rodar os tests, ele não captura variáveis de ambiente do arquivo `.env`

```python
PHYSICIANS_AUTH = 'Adicione a chave de autorização do serviço'
CLINICS_AUTH = 'Adicione a chave de autorização do serviço'
PATIENTS_AUTH = 'Adicione a chave de autorização do serviço'
METRICS_AUTH = 'Adicione a chave de autorização do serviço'
```

**Crie um ambiente de desenvolvimento isolado com [virtualenv](https://virtualenv.pypa.io/en/latest/) ou [pip](https://pipenv.readthedocs.io/en/latest/)**

Prefiro o virtualenv.

`health-rest-api$ virtualenv -p python3.7 .venv`.

**Ativando o ambiente:**

`health-rest-api$ source .venv/bin/activate`.

**Acesse o pacote da aplicação:**

`health-rest-api$ cd health`.

**Instalando as dependências do projeto:**

`health-rest-api/health$ pip install -r requirements.txt`.


## Gerando as Migrações

```text
flask db init
flask db migrate -m "Created Migrations."
flask db upgrade
```

## Executando a aplicação

`health-rest-api/health$ flask run`.

Rodando na porta padrão, caso não seja alterado: [http://localhost:5000](http://localhost:5000).

Ao iniciar a aplicação, um arquivo de `log` será criado na pasta logs.

## RestAPI Resources

Algumas ferramentas e modulos para acessar os recurso da API:

Via terminal usando [curl](https://curl.haxx.se/).

Scripts em Python usando a lib [requests](http://docs.python-requests.org/en/master/).

Ou, aplicações para testar APIs, [Postman](https://www.getpostman.com/) e [Insomnia](https://insomnia.rest/?utm_content=bufferd23bb&utm_medium=social&utm_source=twitter.com&utm_campaign=buffer).

### Prescriptions API

|Method|URI|Status Code|Response|
|-------|-------|-------|-------|
|POST|http://localhost:5000/api/v2/prescriptions/id|201|json contendo os dados salvos.|

Caso algo dê errado um erro será retornado. Abaixo têm um exemplo de possível erro.


**Payload Post method:**

```json
{
	"clinic": {
    	"id": integer
    },
    "patients": {
    	"id": integer
    },
    "physicians": {
    	"id": integer
    },
    "text": string
}
```

**Exemplo de Requests usando Curl:**

```bash
curl -X POST \
  http://localhost:5000/v2/prescriptions \
  -H 'Content-Type: application/json' \
  -d '{
  "clinic": {
    "id": 1
  },
  "physician": {
    "id": 1
  },
  "patient": {
    "id": 1
  },
  "text": "Dipirona 1x ao dia"
}'
```

**Resposta:**

```json
{
  "data": {
    "id": 1,
    "clinic": {
      "id": 1
    },
    "physician": {
      "id": 1
    },
    "patient": {
      "id": 1
    },
    "text": "Dipirona 1x ao dia"
  }
}
```

**Exemplo de Erro:**

```json
{
  "error": {
    "message": "patient not found",
    "code": "03"
  }
}
```

### Tests

**Rodando testes:**

`$ pytest --verbose --cov=app --color=yes tests/`

**Gerando reports e cobertura dos testes em html:**

`$ coverage report html -d coverage_html`

Cobertura dos testes em 85%.


## License
[GNU Affero General Public License v3](https://www.gnu.org/licenses/agpl-3.0.en.html)