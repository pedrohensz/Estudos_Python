"""
A rede de hotelaria HotelPlus te contratou para criar um pequeno sistema de cadastro de usuários. A priori você precisa criar uma tabela chamada usuarios com os seguintes campos:

id (inteiro, chave primária)

nome (texto)

email (texto)

Para testar o seu banco de dados, adicione 2 usuários na tabela usuarios e depois consulte todos os registros.

Se quiser saber mais sobre como realizar essa atividade, clique na opinião da pessoa instrutora

"""
import sqlite3

conn = sqlite3.connect("Hotel.db")

cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios (
               ID INTEGER PRIMARY KEY,
               NOME TEXT,
               EMAIL VARCHAR(50)

               )""")

cursor.execute("""
                INSERT OR IGNORE INTO usuarios (ID, NOME, EMAIL)
               VALUES
               (1,"CARLOS","carlos@bol.com"),
               (2,"JOAO","joao@uol.com")

""")


conn.commit()
cursor.execute("SELECT * FROM usuarios")
print(cursor.fetchall())
conn.close()
