import asyncpg

async def drop_user_table(database_uri):

    # Connect to the database
    conn = await asyncpg.connect(database_uri)
    
    # Drop the users table if it exists
    await conn.execute('''
        DROP TABLE IF EXISTS users
    ''')
    
    # Close the connection
    await conn.close()

