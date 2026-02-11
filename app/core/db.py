import asyncpg

async def run():
    conn = await asyncpg.connect('postgresql://postgres@PostgreSQL 18/TaskFlow')
    await conn.execute('''
        CREATE TABLE test(
            id serial PRIMARY KEY,
            text text NOT NULL,
            is_done boolean NOT NULL,
        )
    ''')
    await conn.close()