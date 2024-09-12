import os
from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante1 = Restaurante('Praca', 'Gourmet')
restaurante2 = Restaurante('Mexican Food', 'Mexicana')
restaurante3 = Restaurante('Japa', 'Japones')

restaurante1.receber_avaliacao('Laura', 10)
restaurante1.receber_avaliacao('Helena', 5)
restaurante1.receber_avaliacao('Pituca', 6)

Restaurante.alternar_status(restaurante2)

prato1 = Prato('Macarronada', 14.9, 'Massa em camadas a bolhonhesa')
bebida1 = Bebida('Suco de manga', 5.0, '300ml')


def main():
    os.system('cls')
    Restaurante.listar_restaurantes()
    print(prato1)
    print(bebida1)
    

if __name__ == '__main__':
    main()