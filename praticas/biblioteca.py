from exercicios import Livro

livro1 = Livro('A batalha do Apocalipse'.ljust(36), 'Chrys Prattson'.ljust(25), 2007)
livro2 = Livro('O guia do Mochileiro das Galáxias'.ljust(36), 'Douglas Adams'.ljust(25), 1983)
livro3 = Livro('Biblia sagrada'.ljust(36), 'Zilhoes de Pessoas'.ljust(25), -0.000)
livro4 = Livro('E Não houve Juízo final'.ljust(36), 'Tiago Pereira'.ljust(25), 2020)

livro1.emprestar()

ano_especifico = 2020
livros_disponiveis_ano = Livro.verificar_disponibilidade(ano_especifico)
print(f"Livros disponíveis em {ano_especifico}: {livros_disponiveis_ano}")


def main():
    Livro.listar_livros()

if __name__ == '__main__':
    main()
    