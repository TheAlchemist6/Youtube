from pprint import pprint
import numpy as np
import psycopg2
from pgvector.psycopg2 import register_vector
from schemas.schema_postgres import create_table_queries

db_url = "postgresql://postgres:postgres@127.0.0.1:5432/youtube_transcripts"
con = psycopg2.connect(dsn=db_url)
cur = con.cursor()
cur.execute('CREATE EXTENSION IF NOT EXISTS vector')
register_vector(con)
for tmp_query in create_table_queries:
    # pprint(tmp_query)
    cur.execute(tmp_query)
    con.commit()


cur.execute('CREATE TABLE items (id bigserial PRIMARY KEY, embedding vector(3))')
embedding = np.array([1, 2, 3])
cur.execute('INSERT INTO items (embedding) VALUES (%s)', (embedding,))

cur.execute('SELECT * FROM items ORDER BY embedding <-> %s LIMIT 5', (embedding,))
result = cur.fetchall()
pprint(result)
