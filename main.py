from fastapi import FastAPI
from pydantic import BaseModel
from database import database, produtos

app = FastAPI()

class ProdutoModel(BaseModel):
   nome: str
   preco: float
   quantidade: int

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.post("/produtos/", response_model=ProdutoModel)
async def criar_produto(produto: ProdutoModel):
    query = produtos.insert().values(
        nome=produto.nome,
        preco=produto.preco,
        quantidade=produto.quantidade
    )
    last_record_id = await database.execute(query)
    return {**produto.dict(), "id": last_record_id}

@app.get("/produtos/", response_model=list[ProdutoModel])
async def listar_produto():
    query = produtos.select()
    return await database.fetch_all(query)
    return results

@app.put("/produtos/", response_model=ProdutoModel)
async def atualizar_produto(produto_id: int, produto: ProdutoModel):
    query = produtos.update().where(produtos.c.id == produto_id).values(
        nome=produto.nome,
        preco=produto.preco,
        quanatidade=produto.quantidade
    )
    await database.execute(query)
    return {**produto.dict(), "id": produto_id}

@app.delete("/produtos/{produto_id}")
async def deletar_produto(produto_id: int):
    query = produtos.delete().where(produtos.c.id == produto_id)
    await database.execute(query)
    return {"message": "Produto deletado com sucesso"}

