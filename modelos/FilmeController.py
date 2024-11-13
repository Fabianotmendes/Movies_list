# modelos/FilmeController.py
from modelos.Banco import Banco

class FilmeController:
    @staticmethod
    def select_like(search_term):
        db = Banco('banco.db')
        query = "SELECT * FROM filmes WHERE nome LIKE ?"
        result = db.select(query, ('%' + search_term + '%',))
        db.close()
        return result
    
    @staticmethod
    def insert_filme(title, genre):
        db = Banco('banco.db')
        query = "INSERT INTO filmes (nome, categoria, assistido) VALUES (?, ?, ?)"
        db.insert(query, (title, genre, False))
        db.close()

    @staticmethod
    def update_filme(idfilme, title=None, genre=None, assistido=None):
        db = Banco('banco.db')
        query = "UPDATE filmes SET "
        params = []
        
        if title is not None:
            query += "nome = ?, "
            params.append(title)
        
        if genre is not None:
            query += "categoria = ?, "
            params.append(genre)
        
        if assistido is not None:
            query += "assistido = ?, "
            params.append(assistido)
        
        query = query.rstrip(', ')
        
        query += " WHERE idfilme = ?"
        params.append(idfilme)
        
        db.insert(query, params)
        db.close()  

    @staticmethod
    def delete_filme(idfilme):
        db = Banco('banco.db')
        query = "DELETE FROM filmes WHERE idfilme = ?"
        db.insert(query, (idfilme,))
        db.close()    