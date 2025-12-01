>
🎯 Motivação

Este projeto foi desenvolvido para aprimorar minhas habilidades em desenvolvimento backend, praticar criação de APIs REST e montar um projeto sólido para compor meu portfólio como desenvolvedor Python.

O objetivo é mostrar domínio em:

Estruturação de APIs

CRUD completo

Pydantic & validação de dados

SQLite para persistência

Boas práticas com FastAPI

Versionamento profissional no GitHub

🧠 O que você aprende com esse projeto?

✔ Criar um servidor FastAPI do zero
✔ montar rotas bem estruturadas
✔ conectar Python com SQLite
✔ validar entradas com Pydantic
✔ usar documentação automática Swagger
✔ boas práticas de organização

🎥 Demonstração (GIF)

Adicione aqui se quiser deixar ainda mais profissional:

![Demonstração](gif-do-projeto.gif)




📁 Estrutura do projeto
📦 API-de-Produtos-FastAPI
├── main.py              # Endpoints da API
├── database.py          # Conexão e operações no banco
├── requirements.txt     # Dependências do projeto
├── .gitignore           # Arquivos ignorados (inclui o banco)
└── README.md            # Documentação

⚙️ Instalação e execução
1️⃣ Clone o repositório
git clone https://github.com/Samuel098-b11/-API-de-Produtos---FastAPI.git

2️⃣ Acesse a pasta
cd -API-de-Produtos---FastAPI

3️⃣ Instale as dependências
pip install -r requirements.txt

4️⃣ Execute o servidor
uvicorn main:app --reload

5️⃣ Documentação automática

Swagger UI → http://localhost:8000/docs

Redoc → http://localhost:8000/redoc

🧪 Exemplos de requisições
➕ Criar produto
{
  "nome": "Teclado Mecânico",
  "preco": 299.90,
  "quantidade": 5
}

📄 Listar produtos

Retorno:

[
  {
    "id": 1,
    "nome": "Teclado Mecânico",
    "preco": 299.90,
    "quantidade": 5
  }
]

✏️ Atualizar produto
{
  "nome": "Teclado Mecânico RGB",
  "preco": 349.90,
  "quantidade": 6
}

🗑 Deletar produto
{"mensagem": "Produto removido com sucesso!"}

🚀 Próximos passos (melhorias futuras)

Planejo evoluir esta API com:

🔐 Autenticação JWT

🧑‍💼 Sistema de usuários

📦 Relacionamentos entre tabelas

🗄 Migração para PostgreSQL

🚀 Deploy na nuvem (Render / Railway)

🧭 Versionamento de rotas / v1 / v2

📊 Dashboard com Streamlit para gerenciar produtos

🧪 Testes automatizados com Pytest

Se quiser, posso te ajudar a implementar qualquer um desses itens.

🤝 Como contribuir

Se quiser contribuir:

git fork
git clone seu-fork
crie uma branch
faça suas alterações
git commit
git push
abra um Pull Request

📩 Contato

Samuel098-b11
📧 Email: ss4688046@gmail.com

## 📩 Contato & Perfil

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Conectar-blue?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/samuel-santos-4928822a0/)  
📧 E-mail: ss4688046@gmail.com  
🐙 GitHub: [Samuel098-b11](https://github.com/Samuel098-b11)


