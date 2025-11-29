import sqlite3

conn = sqlite3.connect("Escola.db")

cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS alunos (
               ID INTEGER PRIMARY KEY,
               NOME TEXT,
               NOTA INTEGER

               )""")

cursor.execute("""
                INSERT OR IGNORE INTO alunos (ID, NOME, NOTA)
               VALUES
               (1,"CARLOS",10)

""")


cursor.execute("""CREATE TABLE IF NOT EXISTS disciplinas (
                NOME_DISCIPLINA TEXT,
                estudante_id INTEGER,
                FOREIGN KEY (estudante_id)\
                REFERENCES alunos(ID)
               )

""")
conn.commit()
cursor.execute("SELECT * FROM alunos")
print(cursor.fetchall())
conn.close()
