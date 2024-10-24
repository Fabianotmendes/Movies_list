from modelos.filme import Filme


filme_name = Filme('Rogue', 'ação')
filme_name1 = Filme('Os Mercenários', 'ação')
filme_name2 = Filme('Top Gun: Maverick', 'ação')
filme_name3 = Filme('Velocidade Máxima', 'ação')

filme_name.alternar_status()
filme_name1.alternar_status()

filme_name.avaliar('Fabiano', 4)
filme_name1.avaliar('Fabiano', 3) 

def main():
    Filme.listar_filmes()


if __name__ == '__main__':
    main()