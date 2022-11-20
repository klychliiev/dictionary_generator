import sqlite3
from word_definitions import data
from text_processing import pos_tagger
from inflected_forms import new1

conn = sqlite3.connect('my_db.db')

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS words(
    word_id INT PRIMARY KEY,
    word TEXT,
    lemma TEXT,
    definition TEXT,
    pos_type TEXT);
    """)

cur.execute("""CREATE TABLE IF NOT EXISTS pos(
    pos_type TEXT)
    """)

cur.execute("""CREATE TABLE IF NOT EXISTS inflections(
    word_id INT,
    inflected_form TEXT,
    FOREIGN KEY (word_id) REFERENCES words(word_id))
    """)


cur.executemany("INSERT INTO pos VALUES(?);", pos_tagger)

for g in data:
    cur.execute("INSERT INTO words VALUES(?, ?, ?, ?, ?)", g)

i = 1
for k in new1:
    for j in k:
        cur.execute("INSERT INTO inflections VALUES(?, ?)", (i, j))
    i += 1

cur.execute("""UPDATE words SET definition=NULL WHERE definition='nun'""")

conn.commit()

conn.close()



