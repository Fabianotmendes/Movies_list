import sqlite3

banco = sqlite3.connect('banco.db')

cursor = banco.cursor()

# cursor.execute("CREATE TABLE filmes (nome text,categoria text,assistido bool)")

#insert
# cursor.execute("INSERT INTO filmes VALUES ('Rogue', 'ação', true)")
# cursor.execute("INSERT INTO filmes VALUES ('Os Mercenários', 'ação', true)")
# cursor.execute("INSERT INTO filmes VALUES ('Top Gun: Maverick', 'ação', false)")
# cursor.execute("INSERT INTO filmes VALUES ('Velocidade Máxima', 'ação', true)")

# banco.commit()

#select
cursor.execute("SELECT * FROM filmes")
print(cursor.fetchall())

#delete
# cursor.execute("DELETE FROM filmes where assistido = true")
# banco.commit()

#update
# cursor.execute("UPDATE filmes SET assistido = true WHERE nome = 'Rogue'")
# banco.commit()

# cursor.execute("SELECT * FROM filmes")
# print(cursor.fetchall())


# nome = input('digite o nome do filme: ' )
# categoria = input('digite a categoria do filme: ' )
# print(nome)
# print(categoria)

# cursor.execute(f"INSERT INTO filmes VALUES ('{nome}', '{categoria}', false)")
# banco.commit()

# banco.close()
