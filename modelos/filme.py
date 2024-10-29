import sqlite3

from modelos.avaliacao import Avaliacao


class Filme:
    filmes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._assistido = False
        self._avaliacao = []
        Filme.filmes.append(self)
    
    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_filmes(cls):
        # print(f"{'Nome do Filme'.ljust(25)} | {'Categoria'.ljust(25)} | {'Assistido'.ljust(25)} | {'Nota'}")
        # for Filme in cls.filmes:
        #     print(f'{Filme._nome.ljust(25)} | {Filme._categoria.ljust(25)} | {Filme.assistido.ljust(25)} | {Filme.media_avaliacao}')

        banco = sqlite3.connect('banco.db')
        cursor = banco.cursor()
        cursor.execute("SELECT * FROM filmes")
        Filmes = cursor.fetchall()
        for Filme in Filmes:
            print(print(f'{Filme._nome.ljust(25)} | {Filme._categoria.ljust(25)} | {Filme.assistido.ljust(25)} | {Filme.media_avaliacao}'))
        
        banco.close()




    @property
    def assistido(self):
        return '☑' if self._assistido else '☐'
    
    def alternar_status(self):
        self._assistido = not self._assistido

    def avaliar(self, usuario, nota):
        avaliacao = Avaliacao(usuario, nota)
        self._avaliacao.append(avaliacao)

    @property
    def media_avaliacao(self):
        if not self._avaliacao:
            return '-'
        media_notas = '✩ ' * int(round(sum(avaliacao._nota for avaliacao in self._avaliacao) / len(self._avaliacao),1))
        return media_notas
    