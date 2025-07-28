# 🏥 SGHSS - Sistema de Gestão Hospitalar e de Serviços de Saúde

Este projeto é um sistema backend desenvolvido em **Python com Flask**, que simula o funcionamento de um sistema de gestão hospitalar, permitindo o gerenciamento de pacientes, profissionais da saúde e agendamento de consultas.

---

## 📌 Objetivos do Projeto

- Aplicar conceitos de **desenvolvimento back-end com Flask**
- Implementar **rotas RESTful** para diferentes entidades (Paciente, Profissional, Consulta)
- Aplicar boas práticas de organização em camadas (Modelos, Rotas, Testes)
- Realizar **testes integrados** simulando o fluxo completo da aplicação

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.11+**
- **Flask** (framework web)
- **Flask SQLAlchemy** (ORM para banco de dados)
- **SQLite** (banco de dados leve e local)
- **unittest** (módulo de testes do Python)
- **Postman** (para testes manuais das rotas)
- **Java (Spring Boot)** – usado para implementação de autenticação via JWT

---

## 🗃️ Estrutura de Diretórios
```
sghss-backend/
├── .idea/                    # Configurações do PyCharm
├── instance/                 # Arquivo do banco SQLite (sghss.db)
├── login-java-springboot/   # Login feito em Java para testes com JWT
├── README.md                 # Este arquivo
├── app.py                   # Arquivo principal que inicia a aplicação Flask
├── config.py                # Configurações da aplicação
├── consultas.py             # Rotas e lógica de consultas médicas
├── criar_tabelas.py         # Novas tabelas
├── limparconsultas.py       # Script para limpar registros de consultas
├── models.py                # Definição das entidades do banco
├── pacientes.py             # Código das rotas de pacientes
├── profissional/            # Rotas e lógica dos profissionais de saúde
├── routes.py                # Rotas gerais da aplicação
└── sghss.db                 # Banco de dados SQLite
```


---

## 🔐 Módulo de Login (Java)

O sistema SGHSS conta com um módulo de autenticação/login desenvolvido separadamente em **Java com Spring Boot**, localizado na pasta:

/login-java-springboot



- A autenticação é baseada em **JWT (JSON Web Token)**
- Essa implementação visa demonstrar o funcionamento da segurança e a separação entre o backend principal (Python/Flask) e a autenticação
- A integração entre os módulos poderá ser feita futuramente via APIs ou gateways

---

⚙️ Como Executar Localmente
1. Clone o repositório

git clone https://github.com/seu-usuario/sghss-backend.git
cd sghss-backend
2. Crie um ambiente virtual

python -m venv venv
# Linux/macOS
source venv/bin/activate
# Windows
venv\Scripts\activate
3. Instale as dependências
Arquivo requirements tem todas as dependecias usadas.

pip install -r requirements.txt
4. Execute o servidor

python app.py
O servidor estará disponível em:
📍 http://127.0.0.1:5000

🧪 Testando com Postman
🔐 Requisições protegidas por JWT
Algumas rotas exigem autenticação via JWT, gerado por um serviço em Java. Adicione o token no cabeçalho:


Authorization: Bearer SEU_TOKEN_JWT
📌 Criar um Paciente
Endpoint: POST /pacientes
Headers:


Content-Type: application/json
Authorization: Bearer <seu_token>
Corpo da requisição:


{
  "nome": "Maria Silva",
  "cpf": "12345678900",
  "data_nascimento": "1990-05-10"
}
📌 Consultar todos os pacientes
Endpoint: GET /pacientes

📌 Atualizar paciente
Endpoint: PUT /pacientes/<id>
Corpo exemplo:


{
  "nome": "Maria S. Oliveira",
  "cpf": "12345678900",
  "data_nascimento": "1990-05-12"
}
📌 Deletar paciente
Endpoint: DELETE /pacientes/<id>

📌 Adicionar histórico clínico
Endpoint: POST /pacientes/<id>/historico
Exemplo: POST /pacientes/1/historico

Corpo:


{
  "descricao": "Paciente apresentou sintomas de gripe leve."
}
📌 Consultar histórico clínico do paciente
Endpoint: GET /pacientes/<id>/historico


👨‍💻 Autor
Desenvolvido por Matheus Vitor
Curso de Análise e Desenvolvimento de Sistemas - UNINTER
