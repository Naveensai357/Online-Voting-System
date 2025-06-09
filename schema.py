# export_schema.py

from db import Base, engine
from sqlalchemy.schema import CreateTable

with open("schema.sql", "w") as f:
    for table in Base.metadata.sorted_tables:
        sql = str(CreateTable(table).compile(dialect=engine.dialect))
        f.write(sql + ";\n\n")
