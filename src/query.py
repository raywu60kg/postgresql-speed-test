import asyncpg


async def slow_query(database_uri:str, limit: int):

    conn = await asyncpg.connect(database_uri)
    
    # Execute a query to fetch all users
    rows = await conn.fetch('SELECT * FROM users')
    
    # Close the connection
    await conn.close()
    
    # Format the rows into a list of dictionaries
    users = [dict(row) for row in rows]
    res = []
    for user in users:
        res.append(user)
    
    return res[:limit] 

async def fast_query(database_uri:str, limit: int):

    conn = await asyncpg.connect(database_uri)
    
    # Execute a query to fetch all users
    rows = await conn.fetch(f'SELECT * FROM users limit {limit}')
    
    # Close the connection
    await conn.close()
    
    # Format the rows into a list of dictionaries
    return [dict(row) for row in rows]