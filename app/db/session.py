import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker

POSTGRES_USER = "postgres"
POSTGRES_PASSWORD = "784512"
POSTGRES_DB = "mydatabase"
POSTGRES_HOST = "localhost"
POSTGRES_PORT = "5432"

DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base: DeclarativeMeta = declarative_base()

from app.db.models import cliente, configuracao_cliente, aprovadores_cliente, tipos_rating_cliente, alcadas_cliente

# Função para criar tabelas
def create_tables():
    Base.metadata.create_all(bind=engine)
    print('Criouuu')

# Se a execução do script é feita diretamente, então chame a função
if __name__ == "__main__":
    create_tables()