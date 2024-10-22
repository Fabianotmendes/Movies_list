from modelos.filme import Filme


filme_praca = Filme('praça', 'Gourmet')


def main():
    filme_praca.listar_filmes
    print(filme_praca)


if __name__ == '__main__':
    main()