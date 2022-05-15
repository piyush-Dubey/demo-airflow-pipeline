from airflow.hooks.base import BaseHook
from sqlalchemy import Column, Integer, create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.types import TIMESTAMP

Base_x = declarative_base()
Base_y = declarative_base()

db_x_conn = BaseHook.get_connection("database_x")
db_y_conn = BaseHook.get_connection("database_y")
engine_y = create_engine(f"postgresql+psycopg2://airflow:{db_y_conn.get_password()}@{db_y_conn.host}:{db_y_conn.port}/airflow")

engine_x = create_engine(f"postgresql+psycopg2://airflow:{db_x_conn.get_password()}@{db_x_conn.host}:{db_x_conn.port}/airflow")
Base_x.metadata.create_all(engine_x)
Base_y.metadata.create_all(engine_y)


class SourceTable(Base_x):
    __tablename__ = "source_table"
    __table_args__ = {"schema": "public"}

    id = Column(Integer, primary_key=True)
    creation_date = Column(TIMESTAMP(timezone="UTC"))
    sale_value = Column(Integer)


class DestinationTable(Base_y):
    __tablename__ = "destination_table"
    __table_args__ = {"schema": "public"}

    id = Column(Integer, primary_key=True)
    creation_date = Column(TIMESTAMP(timezone="UTC"))
    sale_value = Column(Integer, nullable=False)
