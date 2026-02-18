# -*- coding: utf-8 -*-
# @Author: Carlos Galeano
# @Date:   2026-02-06 15:09:07
# @Last Modified by:   Carlos Galeano
# @Last Modified time: 2026-02-06 16:16:05

from fastapi import FastAPI, Depends
from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine
import urllib.parse
import os

app = FastAPI()

def get_engine() -> Engine:
    # Variables de entorno (ajústalas en tu compose/run)
    server = os.getenv("MSSQL_SERVER", "10.51.128.85,1433")
    db     = os.getenv("MSSQL_DB", "FullStar_Data")
    user   = os.getenv("MSSQL_USER", "cellstaradm")
    pwd    = os.getenv("MSSQL_PWD", "cellstaradm")
    # DRIVER debe existir en /etc/odbcinst.ini tras instalar msodbcsql17
    odbc_str = (
        f"DRIVER=ODBC Driver 17 for SQL Server;"
        f"SERVER={server};DATABASE={db};UID={user};PWD={pwd};"
        "Encrypt=yes;TrustServerCertificate=yes;"
    )
    params = urllib.parse.quote_plus(odbc_str)
    return create_engine(f"mssql+pyodbc:///?odbc_connect={params}", pool_pre_ping=True)

engine = get_engine()

@app.get("/health")
def health():
    return {"status": "ok",
            "datos":{
                "info": "Application is running correctly"
            }
           }

@app.get("/version")
def sql_version():
    with engine.connect() as conn:
        v = conn.execute(text("SELECT @@VERSION AS v")).scalar()
    return {"version": v}