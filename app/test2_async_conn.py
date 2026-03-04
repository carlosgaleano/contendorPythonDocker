
import asyncio, asyncpg, os
host=os.getenv("POSTGRES_HOST","db")
port=int(os.getenv("POSTGRES_PORT","5432"))
user=os.getenv("POSTGRES_USER","app")
pwd=os.getenv("POSTGRES_PASSWORD","app")
db =os.getenv("POSTGRES_DB","appdb")

async def main():
    print(f"Intentando conectar a {user}@{host}:{port}/{db}")
    try:
        conn = await asyncpg.connect(user=user, password=pwd, host=host, port=port, database=db)
        print("✅ Conectado OK con asyncpg.")
        await conn.close()
    except Exception as e:
        print("❌ Error de conexión:", repr(e))

asyncio.run(main())
