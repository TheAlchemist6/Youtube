import sqlite3
import sqlite_vss
import numpy as np
import json

# db = sqlite3.connect(':memory:')
db = sqlite3.connect('./test.db')
db.enable_load_extension(True)
sqlite_vss.load(db)
db.enable_load_extension(False)

version, = db.execute('select vss_version()').fetchone()
print(version)


# Create the table



db.execute('''
    CREATE TABLE IF NOT EXISTS documents (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        content TEXT NOT NULL
    );
''')


document_name = "TEST DOCUMENT"
document_content = "I LIKE PIE"
db.execute("INSERT INTO documents (name, content) VALUES (?, ?)", (document_name, document_content))

test_result = db.execute("""
    select count(*) from documents;
""").fetchall()


test_result = db.execute("""
    select * from documents;
""").fetchall()
print(test_result)

db.execute("""
create virtual table vss_demo using vss0(
  a(3)
);
""")


embedding = [0.1, 0.2, 0.3]
db.execute("insert into vss_demo(a) values (?)", [json.dumps(embedding)])

test_result = db.execute("""
select
  rowid,
  distance
from vss_demo
where vss_search(a, json('[2.0, 2.0, 2.0]'))
limit 3;
""").fetchall()
print(test_result)