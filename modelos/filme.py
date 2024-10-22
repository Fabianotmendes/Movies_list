
class Filme:
    filmes = [  {'nome':'A Lista de Schindler', 'categoria':'Drama', 'assistido':False}, 
            {'nome':'Forrest Gump', 'categoria':'Romance', 'assistido':False},
            {'nome':'O Rei Leão', 'categoria':'Família', 'assistido':False},
            {'nome':'O Senhor dos Anéis', 'categoria':'assistido', 'assistido':False},
            {'nome':'Batman', 'categoria':'Acao', 'assistido':False},
            {'nome':'Vingadores', 'categoria':'Acao', 'assistido':True}
            ]

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._assistido = False
        Filme.filmes.append(self)
    
    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_filmes(cls):
        print(f"{'Nome do Filme'.ljust(25)} | {'Categoria'.ljust(25)} |{'Assistido'}")
        for Filme in cls.filmes:
            print(f'{Filme._nome.ljust(25)} | {Filme._categoria.ljust(25)} | {Filme.assistido}')

    # @property
    # def assistido(self):
    #     return '⌧' if self._assistido else '☐'
    
    # def alternar_estado(self):
    #     self._assistido = not self._assistido




   