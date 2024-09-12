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

prato1 = Prato('Macarronada', 14.9, 'Espaguete bolonhesa')
bebida1 = Bebida('Suco de manga', 5.0, '300ml')
bebida2 = Bebida('Coca-cola', 4.00, 'lata 350ml')
prato2 = Prato('Lasanha', 19.90, 'Massa em camadas a bolonhesa')

restaurante1.adicionar_no_cardapio(bebida1)
restaurante1.adicionar_no_cardapio(prato1)
restaurante1.adicionar_no_cardapio(bebida2)
restaurante1.adicionar_no_cardapio(prato2)

def main():
    os.system('cls')
    restaurante1.exibir_cardapio
    

if __name__ == '__main__':
    main()