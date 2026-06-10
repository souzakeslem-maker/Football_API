# ⚽ API de Estatísticas de Futebol

Aplicação Full Stack desenvolvida com FastAPI, Python e React para consulta e visualização de estatísticas de futebol em tempo real, utilizando dados da API Football-Data.

## 🚀 Funcionalidades

* Consulta de campeonatos de futebol
* Listagem de equipes participantes
* Exibição da tabela de classificação
* Consulta de partidas
* Exibição de resultados e placares
* Consumo de API externa (Football-Data)
* Interface web desenvolvida em React
* API REST documentada automaticamente pelo Swagger

## 🛠️ Tecnologias Utilizadas

### Backend

* Python
* FastAPI
* Requests
* Pydantic
* Uvicorn

### Frontend

* React
* JavaScript
* HTML5
* CSS3

### APIs Externas

* Football-Data.org

### Versionamento

* Git
* GitHub

## 📋 Endpoints Disponíveis
GET /times/{liga}
Retorna os times participantes da competição.

GET /partidas/{liga}
Retorna as partidas da competição.

GET /artilheiros/{liga}
Retorna os principais artilheiros da competição.

## ⚙️ Como Executar o Projeto

### Clonar o repositório

```bash
git clone https://github.com/souzakeslem-maker
```

### Entrar na pasta

```bash
cd futebol-stats
```

### Criar ambiente virtual

```bash
python -m venv venv
```

### Ativar ambiente virtual

Windows:

```bash
venv\Scripts\activate
```

### Instalar dependências

```bash
pip install -r requirements.txt
```

### Configurar chave da API

Crie um arquivo `.env` contendo:

```env
API_KEY=SUA_CHAVE_DA_FOOTBALL_DATA
```

### Executar o servidor

```bash
uvicorn main:app --reload
```

## 📚 Aprendizados
Durante o desenvolvimento deste projeto foram praticados conceitos como:

* Consumo de APIs externas
* Tratamento de respostas JSON
* Criação de APIs REST
* Integração Frontend e Backend
* Gerenciamento de variáveis de ambiente
* Estruturação de aplicações FastAPI
* Desenvolvimento de interfaces com React

## 🎯 Objetivo do Projeto
Projeto desenvolvido para consolidar conhecimentos em:

* FastAPI
* React
* Consumo de APIs
* Integração entre sistemas
* Manipulação de dados em JSON
* Desenvolvimento Full Stack

## 👨‍💻 Autor
Keslem Souza
GitHub: https://github.com/souzakeslem-maker
LinkedIn: https://www.linkedin.com/in/keslemsouza-tecnologo/
