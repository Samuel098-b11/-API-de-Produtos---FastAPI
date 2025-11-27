from databases import Database
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float

DATABASE_URL ="sqlite:///./meubanco.db"

database = Database(DATABASE_URL)
metadata = MetaData()

produtos = Table(
    "produtos",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("nome", String, nullable=False),
    Column("preco", Float, nullable=False),
    Column("quantidade", Integer, nullable=False),
)

engine = create_engine(DATABASE_URL)
metadata.create_all(engine)

