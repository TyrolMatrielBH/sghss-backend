SGHSS (Sistema de Gestão Hospitalar e de Serviços de Saúde)

# 🏥 !SGHSS - Sistema de Gestão Hospitalar e de Serviços de Saúde!

Este projeto é um sistema backend desenvolvido em **Python com Flask**, que simula o funcionamento de um sistema de gestão hospitalar, permitindo o gerenciamento de pacientes, profissionais da saúde e agendamento de consultas.

---

## 📌 Objetivos do Projeto

O projeto tem como foco:

- Aplicar os conceitos de **desenvolvimento back-end com Flask**
- Implementar **rotas RESTful** para diferentes entidades (Paciente, Profissional, Consulta)
- Aplicar boas práticas de organização em camadas (Modelos, Rotas, Testes)
- Realizar **testes integrados** simulando o fluxo completo da aplicação

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.11+**
- **Flask** (Framework Web)
- **Flask SQLAlchemy** (ORM para banco de dados)
- **SQLite** (Banco de dados leve)
- **unittest** (Módulo de testes do Python)
- **Postman** (para testes de rotas)
- **Java** (para login/e teste de JWT)

---

## 🗃️ Estrutura de Diretórios

sghss-backend/

├── .idea/ # Configurações do PyCharm
├── instance/ # Arquivo do banco SQLite (sghss.db)
├── login-java-springboot/ # Login feito em Java para testes com JWT
├── README.md # Este arquivo
├── app.py # Arquivo principal que inicia a aplicação Flask
├── config.py # Configurações da aplicação
├── consultas.py # Rotas e lógica de consultas médicas
├── limparconsultas.py # Script para limpar registros de consultas (opcional)
├── models.py # Definição das entidades do banco (Paciente, Profissional, etc.)
├── pacientes.py # Código referente às rotas ou lógica de pacientes (se usado)
├── profissional/ # Diretório contendo as rotas e lógica dos profissionais de saúde
├── routes.py # Outras rotas gerais da aplicação
└── sghss.db # Banco de dados SQLite


🔐 Módulo de Login (Java)
O sistema SGHSS conta com um módulo de autenticação/login desenvolvido separadamente utilizando a linguagem Java.
Esse módulo está localizado na pasta:

bash
Copiar
Editar
/login-java
Informações adicionais:
A autenticação é baseada em JWT (JSON Web Token).

Essa implementação visa demonstrar o funcionamento da segurança e separação de responsabilidades entre o backend principal (Python/Flask) e a autenticação.

A integração entre os módulos pode ser feita futuramente via APIs ou gateways.

markdown
Copiar
Editar

---

## 🧩 Funcionalidades Implementadas

### 📁 Pacientes

- `GET /pacientes` - Lista todos os pacientes
- `POST /pacientes` - Cria um novo paciente
- `PUT /pacientes/<id>` - Atualiza um paciente existente
- `DELETE /pacientes/<id>` - Remove um paciente

### 👩‍⚕️ Profissionais

- `GET /profissionais` - Lista os profissionais da saúde
- `POST /profissionais` - Cria um novo profissional

### 📆 Consultas

- `POST /consultas` - Agenda uma nova consulta entre paciente e profissional

---

## 🧪 Testes Automatizados

O arquivo `test_integrado.py` realiza um **teste de fluxo completo**, que:

1. Cria um paciente
2. Cria um profissional
3. Agenda uma consulta entre os dois
4. Verifica se tudo foi executado com sucesso (códigos HTTP e dados retornados)

> ✔ Para rodar os testes:
```bash
python test_integrado.py
🔁 Padrão de Projeto Utilizado
O projeto segue os princípios de orientação a objetos, com separação de responsabilidades por arquivos:

Modelos (ORM) no models.py

Lógica de negócio nas rotas (como se fossem controllers simplificados)

Camada de testes em test_integrado.py

🧑‍💻 Como Executar o Projeto
Clone este repositório:

bash
Copiar
Editar
git clone https://github.com/seu-usuario/sghss-backend.git
cd sghss-backend
Crie e ative um ambiente virtual:

bash
Copiar
Editar
python -m venv venv
.\venv\Scripts\activate   # No Windows
Instale as dependências:

bash
Copiar
Editar
pip install flask flask_sqlalchemy
Execute o servidor:

bash
Copiar
Editar
python app.py
🧼 Observações
O projeto utiliza SQLite por simplicidade, ideal para testes locais.

As datas devem ser enviadas no formato "YYYY-MM-DD" ou "YYYY-MM-DD HH:MM" conforme exigido pela rota.

🤝 Contribuições
Esse projeto foi desenvolvido como parte do curso de Análise e Desenvolvimento de Sistemas com foco no módulo de Projeto Multidisciplinar.

📅 Autor
Matheus Vitor Lourenço
Desenvolvedor Back-End | Estudante de ADS
Belo Horizonte - MG