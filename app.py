from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
restaurante_japones = Restaurante('Japa', 'Japonesa')

restaurante_praca.receber_avaliacao('Tigo', 3)
restaurante_praca.receber_avaliacao('Du', 5)
restaurante_mexicano.receber_avaliacao('Nene', 5)
restaurante_mexicano.receber_avaliacao('stef', 2)


restaurante_praca.alternar_estado()
restaurante_mexicano.alternar_estado()

def main():
    Restaurante.listar_restaurantes()


if __name__ == '__main__':
    main()
