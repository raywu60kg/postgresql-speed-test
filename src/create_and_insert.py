import asyncpg
import random
import string
from pydantic import BaseModel 

class CreateTableInput(BaseModel):
    record_number: int 
    username_len: int

def generate_random_username(username_len):
    return ''.join(random.choice(string.ascii_letters) for _ in range(username_len))

# Function to create a table and batch insert data
async def create_table_and_batch_insert_data(database_uri,record_number, username_len):

    # Connect to the database
    conn = await asyncpg.connect(database_uri)
    
    # Create a table if not exists
    await conn.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username TEXT 
        )
    ''')

    usernames = [generate_random_username(username_len) for _ in range(record_number)]
    
    # Batch insert data into the table
    async with conn.transaction():
        await conn.executemany('''
            INSERT INTO users (username) VALUES ($1)
        ''', [(username,) for username in usernames])
    
    # Close the connection
    await conn.close()
