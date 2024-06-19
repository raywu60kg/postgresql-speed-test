from fastapi import FastAPI, HTTPException, Query
import asyncpg
from .drop_table import drop_user_table
from .create_and_insert import create_table_and_batch_insert_data,CreateTableInput
from .query import slow_query, fast_query
app = FastAPI()


# Database configuration
DATABASE_URI = "postgresql://pst:pst@localhost/pst"

@app.delete("/table")
async def drop_table():
   await drop_user_table(database_uri=DATABASE_URI)

@app.post("/table")
async def create_table(create_table_input: CreateTableInput):
   await create_table_and_batch_insert_data(database_uri= DATABASE_URI,record_number=create_table_input.record_number,username_len=create_table_input.username_len)

@app.get("/slow-query")
async def slow_query_users(limit: int = Query(default=10)):
    return await slow_query(database_uri=DATABASE_URI,limit=limit)

@app.get("/fast-query")
async def fast_query_users(limit: int = Query(default=10)):
    return await fast_query(database_uri=DATABASE_URI,limit=limit)